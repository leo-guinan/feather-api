# Generated by Django 3.2.13 on 2022-07-03 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20220628_0138'),
        ('watchtweet', '0013_rename_watchresponses_watchresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountThatRespondedToWatchedTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responded_to_watches', to='twitter.twitteraccount')),
                ('watched_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts_that_responded', to='watchtweet.tweettowatch')),
            ],
        ),
        migrations.CreateModel(
            name='AccountsToIgnore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, verbose_name='the reason this account is ignored')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ignored_for', to='twitter.twitteraccount')),
            ],
        ),
    ]