# Generated by Django 3.2.15 on 2022-12-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_includedlink'),
        ('followed', '0003_auto_20221203_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerreport',
            name='date',
            field=models.DateTimeField(auto_created=True, verbose_name='date of report'),
        ),
        migrations.RemoveField(
            model_name='followerreport',
            name='followers',
        ),
        migrations.AddField(
            model_name='followerreport',
            name='followers',
            field=models.ManyToManyField(related_name='subscribed_following', to='twitter.TwitterAccount'),
        ),
    ]
