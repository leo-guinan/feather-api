# Generated by Django 3.2.13 on 2022-06-28 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_twitteraccount_most_recent_tweet'),
        ('watchtweet', '0012_action_tweettowatch_watchresponses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WatchResponses',
            new_name='WatchResponse',
        ),
    ]
