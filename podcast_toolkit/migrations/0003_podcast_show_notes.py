# Generated by Django 3.2.16 on 2022-12-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_toolkit', '0002_auto_20221217_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='show_notes',
            field=models.TextField(null=True),
        ),
    ]
