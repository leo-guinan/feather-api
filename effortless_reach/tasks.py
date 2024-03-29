import logging
import os
from datetime import datetime
from os.path import splitext

import requests
from decouple import config
from pydub import AudioSegment

from backend.celery import app
from effortless_reach.models import RssFeed, Podcast, PodcastEpisode, Transcript, TranscriptRequest, TranscriptChunk
from effortless_reach.service import process_channel, process_entry, transcribe_episode, \
    create_embeddings_for_podcast_episode, save_embeddings, get_embeddings, split, summarize, get_keypoints
from rss.service import parse_feed
from s3.s3_client import S3Client

logger = logging.getLogger(__name__)



@app.task(name="effortless_reach.process_rss_feed")
def process_rss_feed(feed_id):
    feed = RssFeed.objects.get(id=feed_id)
    parsed_feed = parse_feed(feed.url)
    logger.debug(parsed_feed)
    channel = parsed_feed.channel
    logger.debug(channel)
    feed_generator = channel.generator if hasattr(channel, 'generator') else ''

    podcast = process_channel(channel, feed)
    entries = parsed_feed.entries
    for entry in entries:
        logger.debug(entry)
        process_entry(entry, podcast, feed_generator)
    feed.processed = True
    feed.processed_at = datetime.now()
    feed.save()

@app.task(name="effortless_reach.transcribe_podcast")
def transcribe_podcast(podcast_episode_id):
    transcribe_episode(podcast_episode_id)
    create_embeddings_for_episode.delay(podcast_episode_id)


@app.task(name="effortless_reach.transcribe_all_podcasts")
def transcribe_all_podcasts():
    transcription_requests = TranscriptRequest.objects.filter(status=TranscriptRequest.RequestStatus.PENDING, podcast_episode__transformed_link__isnull=False).all()
    for request in transcription_requests:
        transcribe_podcast.apply_async([request.podcast_episode.id,], queue='bot' )
        request.status = TranscriptRequest.RequestStatus.PROCESSING
        request.save()

@app.task(name="effortless_reach.create_embeddings_for_episode")
def create_embeddings_for_episode(podcast_episode_id):
    create_embeddings_for_podcast_episode(podcast_episode_id)

@app.task(name="effortless_reach.get_image_for_podcasts")
def get_image_for_podcasts():
    podcasts = Podcast.objects.filter(image=None).all()
    for podcast in podcasts:
        rss_feed = podcast.rss_feed
        parsed_feed = parse_feed(rss_feed.url)
        channel = parsed_feed.channel
        podcast.image = channel.image.href
        podcast.save()


@app.task(name="effortless_reach.convert_file")
def convert_file(episode_id):

    episode = PodcastEpisode.objects.get(id=episode_id)
    if episode.transformed_link:
        return
    url = episode.download_link
    file_name = url.split("/")[-1]
    file_name = file_name.split("?")[0]
    r = requests.get(url)
    # get the file name

    with open(file_name, "wb") as f:
        f.write(r.content)
    logger.info("Converting podcast to flac")
    converted_filename = "%s.flac" % splitext(file_name)[0]
    try:

        files = [('files', open(file_name, 'rb'))]
        response = requests.post(config('CONVERT_URL'), files=files)
        open(converted_filename, 'wb').write(response.content)
        s3 = S3Client()
        s3.upload_file(converted_filename, 'effortless-reach', f'flac/{episode.id}/{converted_filename}')
        episode.transformed_link = converted_filename
        episode.save()
    except Exception as e:
        logger.error(e)
    finally:
        os.remove(file_name)
        os.remove(converted_filename)

@app.task(name="effortless_reach.convert_needed_files")
def convert_needed_files():
    # find all episodes that have blank transcripts
    episodes = PodcastEpisode.objects.filter(transcript=None).all()
    for episode in episodes:
        convert_file.delay(episode.id)

    episodes = PodcastEpisode.objects.filter(transcript__text='').all()
    for episode in episodes:
        convert_file.delay(episode.id)


@app.task(name="effortless_reach_get_episode_summary")
def get_episode_summary(episode_id):
    summarize(episode_id)

@app.task(name="effortless_reach_get_episode_keypoints")
def get_episode_keypoints(episode_id):
    get_keypoints(episode_id)

@app.task(name="effortless_reach.save_embeddings")
def save_embeddings_task(episode_id):
    save_embeddings(episode_id)

@app.task(name="effortless_reach.save_needed_embeddings")
def save_needed_embeddings():
    chunks = TranscriptChunk.objects.filter(embeddings_saved=False).all()
    for chunk in chunks:
        save_embeddings_task.delay(chunk.id)