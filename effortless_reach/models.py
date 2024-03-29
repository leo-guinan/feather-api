from django.db import models

from search.models import Curator


# Create your models here.
class RssFeed(models.Model):
    url = models.CharField(max_length=512)
    processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('client.ClientAccount', on_delete=models.CASCADE, related_name="rss_feeds", null=True)


class Podcast(models.Model):
    title = models.CharField(max_length=512)
    link = models.CharField(max_length=512)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rss_feed = models.OneToOneField(RssFeed, related_name="podcast", on_delete=models.CASCADE)
    image = models.CharField(max_length=512, null=True, blank=True)

class PodcastEpisode(models.Model):
    title = models.CharField(max_length=512)
    link = models.CharField(max_length=512)
    download_link = models.CharField(max_length=512, null=True)
    transformed_link = models.CharField(max_length=512, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    podcast = models.ForeignKey(Podcast, related_name="episodes", on_delete=models.CASCADE)
    image = models.CharField(max_length=512, null=True, blank=True)

class Transcript(models.Model):
    class TranscriptStatus(models.TextChoices):
        REQUESTED = 'RE', ('Requested')
        PROCESSING = 'PR', ('Processing')
        COMPLETED = 'CO', ('Completed')
        FAILED = 'FA', ('Failed')

    status = models.CharField(max_length=2, choices=TranscriptStatus.choices, default=TranscriptStatus.REQUESTED)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    episode = models.OneToOneField(PodcastEpisode, related_name="transcript", on_delete=models.CASCADE)
    error = models.TextField(null=True)
    hash = models.CharField(max_length=512, null=True)


class TranscriptRequest(models.Model):
    class RequestStatus(models.TextChoices):
        PENDING = 'PE', ('Pending')
        PROCESSING = 'PR', ('Processing')
        COMPLETED = 'CO', ('Completed')
        FAILED = 'FA', ('Failed')

    status = models.CharField(max_length=2, choices=RequestStatus.choices, default=RequestStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    podcast_episode = models.OneToOneField(PodcastEpisode, related_name="transcript_requested", on_delete=models.CASCADE)
    error = models.TextField(null=True)


class TranscriptChunk(models.Model):
    transcript = models.ForeignKey('effortless_reach.Transcript', related_name='chunks', on_delete=models.CASCADE)
    text = models.TextField()
    embeddings = models.JSONField(null=True, blank=True)
    embeddings_saved = models.BooleanField(default=False)
    chunk_id = models.CharField(max_length=255, unique=True)


class Summary(models.Model):
    text = models.TextField()
    episode = models.OneToOneField(PodcastEpisode, related_name="summary", on_delete=models.CASCADE)
    error = models.TextField(null=True)

class KeyPoints(models.Model):
    text = models.TextField()
    episode = models.OneToOneField(PodcastEpisode, related_name="key_points", on_delete=models.CASCADE)
    error = models.TextField(null=True)


class PodcastNotes(models.Model):
    text = models.TextField()
    episode = models.ForeignKey(Podcast, related_name="notes", on_delete=models.CASCADE)
    curator = models.ForeignKey(Curator, related_name="podcast_notes", on_delete=models.CASCADE)
    error = models.TextField(null=True)

class PodcastEpisodeNotes(models.Model):
    text = models.TextField()
    episode = models.ForeignKey(PodcastEpisode, related_name="notes", on_delete=models.CASCADE)
    curator = models.ForeignKey(Curator, related_name="podcast_episode_notes", on_delete=models.CASCADE)
    error = models.TextField(null=True)


class FavoriteCurators(models.Model):
    curator = models.ForeignKey(Curator, related_name="favorite_curators", on_delete=models.CASCADE)
    favorite_curator = models.ForeignKey(Curator, related_name="curators", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)