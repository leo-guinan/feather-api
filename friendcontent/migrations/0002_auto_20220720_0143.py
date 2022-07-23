# Generated by Django 3.2.13 on 2022-07-20 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_group'),
        ('friendcontent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('BL', 'Blog'), ('PC', 'Podcast'), ('YT', 'Youtube'), ('TT', 'TikTok'), ('IG', 'Instagram'), ('HT', 'Hashtag')], default='PC', max_length=2),
        ),
        migrations.CreateModel(
            name='TriggerTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=280, null=True, verbose_name='action to take')),
                ('taken', models.BooleanField(default=False, verbose_name='has it been completed')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggers', to='twitter.tweet')),
            ],
        ),
    ]
