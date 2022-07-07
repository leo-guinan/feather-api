from datetime import datetime, timedelta

import tweepy
from celery import group
from pytz import utc

from backend.celery import app
from twitter.models import TwitterAccount
from twitter_api.twitter_api import TwitterAPI
from unfollow.models import AnalysisReport


@app.task(name="lookup_twitter_user", autoretry_for=(tweepy.errors.TooManyRequests,), retry_backoff=60,
          retry_kwargs={'max_retries': 8})
def lookup_twitter_user(token, twitter_id_to_check):
    twitter_api = TwitterAPI()
    current_user = TwitterAccount.objects.filter(twitter_id=twitter_id_to_check).first()
    if not current_user:
        user_data = twitter_api.lookup_user(twitter_id=twitter_id_to_check, token=token)
        if not user_data:
            return None
        current_user = TwitterAccount(twitter_id=twitter_id_to_check, twitter_username=user_data.username,
                                      twitter_name=user_data.name)
        current_user.token = token
        current_user.save()
    followers = twitter_api.get_following_for_user(twitter_id=twitter_id_to_check, token=token)
    user_lookup_tasks = []
    user_follows_account_tasks = []
    for user in followers:
        twitter_account = TwitterAccount.objects.filter(twitter_id=user.id).first()
        if not twitter_account:
            twitter_account = TwitterAccount(twitter_id=user.id, twitter_username=user.username,
                                             twitter_name=user.name
                                             )
            twitter_account.save()
        user_follows_account_tasks.append(user_follows_account.s(twitter_id_to_check, user.id))
        user_lookup_tasks.append(get_most_recent_tweet_for_account.s(twitter_id_to_check, user.id))
    user_lookup_group = group(user_lookup_tasks)
    user_follows_account_group = group(user_follows_account_tasks)
    follows_result = user_follows_account_group()
    lookup_result = user_lookup_group()
    while not lookup_result.successful() or not follows_result.successful():
        pass



@app.task(name="lookup_twitter_user_nologin", autoretry_for=(tweepy.errors.TooManyRequests,), retry_backoff=60,
          retry_kwargs={'max_retries': 8})
def lookup_twitter_user_as_admin(twitter_id_to_check):
    twitter_api = TwitterAPI()
    current_user = TwitterAccount.objects.filter(twitter_id=twitter_id_to_check).first()
    if not current_user:
        user_data = twitter_api.lookup_user_as_admin(twitter_id=twitter_id_to_check)
        if not user_data:
            return None
        current_user = TwitterAccount(twitter_id=twitter_id_to_check, twitter_username=user_data.username,
                                      twitter_name=user_data.name)
        current_user.save()
    followers = twitter_api.get_following_for_user_admin(twitter_id=twitter_id_to_check)
    user_lookup_tasks = []
    user_follows_account_tasks = []
    for user in followers:
        twitter_account = TwitterAccount.objects.filter(twitter_id=user.id).first()
        if not twitter_account:
            twitter_account = TwitterAccount(twitter_id=user.id, twitter_username=user.username,
                                             twitter_name=user.name
                                             )
            twitter_account.save()
        user_follows_account_tasks.append(user_follows_account.s(twitter_id_to_check, user.id))
        user_lookup_tasks.append(get_most_recent_tweet_for_account_as_admin.s(user.id))
    user_lookup_group = group(user_lookup_tasks)
    user_follows_account_group = group(user_follows_account_tasks)
    follows = user_follows_account_group()
    res = user_lookup_group()
    while not res.successful() or not follows.successful():
        pass

    report_to_account.delay(current_user.twitter_id)


@app.task(name="get_most_recent_tweet", autoretry_for=(tweepy.errors.TooManyRequests,), retry_backoff=60,
          retry_kwargs={'max_retries': 8})
def get_most_recent_tweet_for_account(logged_in_twitter_id, account_id):
    twitter_api = TwitterAPI()
    logged_in_account = TwitterAccount.objects.filter(twitter_id=logged_in_twitter_id).first()
    twitter_account = TwitterAccount.objects.filter(twitter_id=account_id).first()
    if (twitter_account.last_tweet_date and twitter_account.last_tweet_date > (
            utc.localize(datetime.now() - timedelta(days=90)))):
        return
    most_recent_tweet = twitter_api.get_most_recent_tweet_for_user(account_id, token=logged_in_account.token)
    if most_recent_tweet is not None:
        twitter_account.last_tweet_date = most_recent_tweet.created_at
        twitter_account.save()
    else:
        # when no tweet, just set last tweet date to 5 years ago
        twitter_account.last_tweet_date = utc.localize(datetime.now() - timedelta(weeks=52 * 5))
        twitter_account.save()


@app.task(name="get_most_recent_tweet_nologin", autoretry_for=(tweepy.errors.TooManyRequests,), retry_backoff=60,
          retry_kwargs={'max_retries': 8})
def get_most_recent_tweet_for_account_as_admin(account_id):
    twitter_api = TwitterAPI()
    twitter_account = TwitterAccount.objects.filter(twitter_id=account_id).first()
    if (twitter_account.last_tweet_date and twitter_account.last_tweet_date > (
            utc.localize(datetime.now() - timedelta(days=90)))):
        return
    most_recent_tweet = twitter_api.get_most_recent_tweet_for_user_as_admin(account_id)
    if most_recent_tweet is not None:
        twitter_account.last_tweet_date = most_recent_tweet.created_at
        twitter_account.save()
    else:
        # when no tweet, just set last tweet date to 5 years ago
        twitter_account.last_tweet_date = utc.localize(datetime.now() - timedelta(weeks=52 * 5))
        twitter_account.save()


@app.task(name="user_follows_account")
def user_follows_account(user_id, follows_id):
    relationship = TwitterAccount.objects.filter(twitter_id=user_id,
                                                 follows__twitter_id=follows_id).first()
    if not relationship:
        current_user = TwitterAccount.objects.filter(twitter_id=user_id).first()
        twitter_account = TwitterAccount.objects.filter(twitter_id=follows_id).first()
        current_user.follows.add(twitter_account)
        current_user.save()


@app.task(name="send_analysis_to_account")
def report_to_account(twitter_id_to_check):
    twitter_api = TwitterAPI()
    date_to_compare_against = utc.localize(datetime.now() - timedelta(days=90))
    results = []
    current_user = TwitterAccount.objects.filter(twitter_id=twitter_id_to_check).first()
    print("Checking relationships...")
    for user_to_check in current_user.follows.all():

        if user_to_check and user_to_check.last_tweet_date:
            if user_to_check.last_tweet_date < date_to_compare_against:
                results.append(user_to_check)

    message = f".@{current_user.twitter_username} you follow {len(results)} accounts that haven't tweeted in the last three months"
    twitter_api.send_tweet(message)
    report = AnalysisReport(account=current_user, dormant_count=len(results), following_count=current_user.follows.count())
    report.save()
