# Generated by Django 3.2.13 on 2022-07-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_clientaccount_refreshed'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='access_secret',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Access secret'),
        ),
        migrations.AddField(
            model_name='client',
            name='access_token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Access token'),
        ),
        migrations.AddField(
            model_name='client',
            name='consumer_key',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='consumer key'),
        ),
        migrations.AddField(
            model_name='client',
            name='consumer_secret',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='consumer secret'),
        ),
    ]
