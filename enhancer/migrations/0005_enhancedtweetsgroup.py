# Generated by Django 3.2.16 on 2022-12-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enhancer', '0004_enhancedtweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnhancedTweetsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True, null=True)),
                ('enhancement_run_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OK', 'Okay'), ('ER', 'Error')], default='OK', max_length=2)),
                ('enhanced_tweets', models.ManyToManyField(related_name='enhanced_tweets_groups', to='enhancer.EnhancedTweet')),
            ],
        ),
    ]
