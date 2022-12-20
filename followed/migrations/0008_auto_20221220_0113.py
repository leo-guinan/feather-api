# Generated by Django 3.2.16 on 2022-12-20 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followed', '0007_differencereport'),
    ]

    operations = [
        migrations.AddField(
            model_name='differencereport',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='message of email'),
        ),
        migrations.AddField(
            model_name='differencereport',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='subject of email'),
        ),
    ]
