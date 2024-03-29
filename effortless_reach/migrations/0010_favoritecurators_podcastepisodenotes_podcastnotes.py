# Generated by Django 3.2.16 on 2023-03-05 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_curator'),
        ('effortless_reach', '0009_keypoints_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='PodcastNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('error', models.TextField(null=True)),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcast_notes', to='search.curator')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='effortless_reach.podcast')),
            ],
        ),
        migrations.CreateModel(
            name='PodcastEpisodeNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('error', models.TextField(null=True)),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcast_episode_notes', to='search.curator')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='effortless_reach.podcastepisode')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteCurators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_curators', to='search.curator')),
                ('favorite_curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curators', to='search.curator')),
            ],
        ),
    ]
