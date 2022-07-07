# Generated by Django 3.2.13 on 2022-07-06 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_group'),
        ('unfollow', '0006_auto_20220706_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis', to='twitter.twitteraccount', unique_for_date=True),
        ),
    ]
