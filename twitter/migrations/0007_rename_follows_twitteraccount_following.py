# Generated by Django 3.2.13 on 2022-07-23 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_twitteraccount_last_checked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twitteraccount',
            old_name='follows',
            new_name='following',
        ),
    ]
