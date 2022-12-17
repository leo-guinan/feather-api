# Generated by Django 3.2.16 on 2022-12-17 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_toolkit', '0003_podcast_show_notes'),
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcriptrequestemail',
            name='podcast',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='podcast_toolkit.podcast'),
        ),
    ]