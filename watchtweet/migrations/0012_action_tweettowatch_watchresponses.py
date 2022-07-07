# Generated by Django 3.2.13 on 2022-06-28 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_twitteraccount_most_recent_tweet'),
        ('watchtweet', '0011_alter_watchtweet_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of action')),
            ],
        ),
        migrations.CreateModel(
            name='TweetToWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_to_take', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets_to_act_on', to='watchtweet.action')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watches_requested', to='twitter.twitteraccount')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watches', to='twitter.tweet')),
            ],
        ),
        migrations.CreateModel(
            name='WatchResponses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_taken', models.BooleanField(default=False, verbose_name='was the action taken?')),
                ('ignored', models.BooleanField(default=False, verbose_name='should this response be ignored?')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_responses', to='twitter.tweet')),
                ('watched_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses_to_tweet', to='watchtweet.tweettowatch')),
            ],
        ),
    ]
