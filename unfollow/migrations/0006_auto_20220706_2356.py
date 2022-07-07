# Generated by Django 3.2.13 on 2022-07-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unfollow', '0005_analysis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='twitteraccount',
            name='groups',
        ),
        migrations.AlterField(
            model_name='analysis',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.DeleteModel(
            name='FollowingRelationship',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='TwitterAccount',
        ),
    ]
