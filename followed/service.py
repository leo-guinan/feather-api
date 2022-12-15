from datetime import datetime

from client.models import Client
from enhancer.service import enhance_twitter_account_with_summary
from followed.config import CLIENT_NAME
from followed.models import Subscriber, FollowerReport
from twitter.service import get_twitter_account
from twitter_api.twitter_api import TwitterAPI
from mail.service import send_email
CLIENT = Client.objects.filter(name=CLIENT_NAME).first()


def create_follower_record_for_subscriber(subscriber_id):
    twitter_api = TwitterAPI(client=CLIENT)
    subscriber = Subscriber.objects.filter(id=subscriber_id).first()
    if not subscriber:
        return None
    twitter_id = subscriber.client_account.twitter_account.twitter_id
    client_account_id = subscriber.client_account.id
    follower_report = FollowerReport()
    follower_report.subscriber = subscriber
    follower_report.date = datetime.now()
    follower_report.save()
    followers = twitter_api.get_users_following_account(twitter_id=twitter_id, client_account_id=client_account_id)
    for user in followers:
        twitter_account = get_twitter_account(user.id, client_account_id)
        follower_report.followers.add(twitter_account)
    follower_report.save()


def get_report_difference_and_email(subscriber_id):
    subscriber = Subscriber.objects.filter(id=subscriber_id).first()
    if not subscriber:
        return
    reports = subscriber.reports.exclude(followers=None).all()
    if len(reports) < 2:
        return
    message = ""
    current_report = reports[len(reports) - 1]
    previous_report = reports[len(reports) - 2]
    subject = f"Follower report for {previous_report.date} to {current_report.date}:\n"
    message += subject
    message += "-"*50
    message += "\n"

    current_followers = [{"id": follower.twitter_id, "name": follower.twitter_username, "bio": follower.twitter_bio} for follower in current_report.followers.all() ]
    previous_followers = [{"id": follower.twitter_id, "name": follower.twitter_username, "bio": follower.twitter_bio} for follower in previous_report.followers.all()]
    new_followers = [follower for follower in current_followers if follower not in previous_followers]
    lost_followers = [follower for follower in previous_followers if follower not in current_followers]
    message += f"Number of new followers: {len(new_followers)}\n"
    message += f"Number of lost followers: {len(lost_followers)}\n"
    message += "-"*25
    message += "\n"
    message += "New followers:\n"
    if len(new_followers) > 0:
        for follower in new_followers:
            enhanced_twitter_account = enhance_twitter_account_with_summary(follower["id"], subscriber.client_account.id)
            message += f"Profile: https://twitter.com/{enhanced_twitter_account.twitter_account.twitter_username}\n"
            message += f"Name: {enhanced_twitter_account.twitter_account.twitter_name}\n"
            message += f"Bio: {enhanced_twitter_account.twitter_account.twitter_bio}\n"
            message += f"Account summary: {enhanced_twitter_account.summary}\n"
            message += "-"*25
            message += "\n"

    send_email(subscriber.client_account.email, message, subject)
    send_email('leo@definet.dev', message, f"Followed Report for {subscriber.client_account.twitter_account.twitter_username}: {subject}")


