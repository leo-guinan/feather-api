# Generated by Django 3.2.13 on 2022-07-04 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20220628_0138'),
        ('unfollow', '0003_auto_20220605_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dormant_count', models.IntegerField(verbose_name='number of accounts followed that are dormant')),
                ('following_count', models.IntegerField(verbose_name='number of accounts followed')),
                ('date_of_report', models.DateField(auto_now_add=True, verbose_name='Date report was created')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_reports', to='twitter.twitteraccount')),
            ],
        ),
    ]