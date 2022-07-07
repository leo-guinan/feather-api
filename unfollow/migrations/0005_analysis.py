# Generated by Django 3.2.13 on 2022-07-06 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20220628_0138'),
        ('unfollow', '0004_analysisreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('RE', 'Requested'), ('ST', 'Started'), ('IP', 'In progress'), ('CP', 'Complete'), ('ER', 'Error')], default='RE', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Date updated')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis', to='twitter.twitteraccount')),
            ],
        ),
    ]
