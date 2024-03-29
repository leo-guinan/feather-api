# Generated by Django 3.2.15 on 2022-10-05 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0018_alter_clientaccount_twitter_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_location', models.CharField(max_length=1024, verbose_name='location of the feed')),
                ('name', models.CharField(max_length=1024, verbose_name='name of the feed')),
            ],
        ),
        migrations.CreateModel(
            name='ContentFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1024, verbose_name='link to the content')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_feeds', to='client.clientaccount')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='gardens.contentsource')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1024, verbose_name='link to the content')),
                ('title', models.CharField(blank=True, max_length=1024, null=True, verbose_name='title of the content')),
                ('summary', models.CharField(blank=True, max_length=4096, null=True, verbose_name='summary of the content')),
                ('published', models.DateTimeField(blank=True, null=True, verbose_name='time the content was published')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='gardens.contentfeed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_items', to='client.clientaccount')),
            ],
        ),
    ]
