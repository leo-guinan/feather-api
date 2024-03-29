# Generated by Django 3.2.13 on 2022-07-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20220624_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='refresh_token',
            field=models.CharField(default='', max_length=255, verbose_name='twitter oauth2 refresh token'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='token',
            field=models.CharField(default='', max_length=255, verbose_name='twitter oauth2 token'),
        ),
    ]
