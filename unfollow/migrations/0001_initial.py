# Generated by Django 4.0.4 on 2022-05-14 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.CharField(max_length=512, unique=True, verbose_name='Twitter ID')),
                ('twitter_username', models.CharField(max_length=255, null=True, verbose_name='Twitter Username')),
                ('twitter_name', models.CharField(max_length=255, null=True, verbose_name='Twitter Name')),
                ('last_tweet_date', models.DateTimeField(null=True, verbose_name='date of last tweet')),
            ],
        ),
        migrations.CreateModel(
            name='FollowingRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='follows', to='unfollow.twitteraccount')),
                ('twitter_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='main', to='unfollow.twitteraccount')),
            ],
        ),
    ]
