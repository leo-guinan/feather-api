# Generated by Django 3.2.13 on 2022-07-17 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_betaaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='betaaccount',
            name='messaged',
            field=models.BooleanField(default=False, verbose_name='did we send the dm?'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='refresh_token',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='twitter oauth2 refresh token'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='token',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='twitter oauth2 token'),
        ),
    ]
