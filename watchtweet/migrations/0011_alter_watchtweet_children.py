# Generated by Django 3.2.13 on 2022-06-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchtweet', '0010_auto_20220618_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchtweet',
            name='children',
            field=models.ManyToManyField(blank=True, related_name='parent', to='watchtweet.WatchTweet'),
        ),
    ]
