# Generated by Django 3.2.16 on 2022-12-19 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0018_alter_clientaccount_twitter_account'),
        ('webhooks', '0002_transcriptrequestemail_podcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcriptrequestemail',
            name='client_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='podcast_transcript_requests', to='client.clientaccount'),
        ),
    ]