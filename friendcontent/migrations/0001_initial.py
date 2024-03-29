# Generated by Django 3.2.13 on 2022-07-19 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('twitter', '0005_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('BL', 'Blog'), ('PC', 'Podcast'), ('YT', 'Youtube'), ('TT', 'TikTok'), ('IG', 'Instagram')], default='PC', max_length=2)),
                ('url', models.CharField(max_length=1024, verbose_name='link to the content')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_content', to='twitter.twitteraccount')),
            ],
        ),
    ]
