# Generated by Django 3.2.13 on 2022-07-17 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unfollow', '0013_accountcheck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountcheck',
            name='state',
        ),
    ]