# Generated by Django 3.2.16 on 2023-01-21 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_contentchunk_chunk_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='fulltext',
            field=models.TextField(blank=True, null=True),
        ),
    ]