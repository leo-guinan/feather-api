# Generated by Django 3.2.13 on 2022-07-18 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_group'),
        ('client', '0010_auto_20220717_0158'),
        ('unfollow', '0012_auto_20220709_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_requested', models.DateTimeField(auto_now=True, verbose_name='last time requested')),
                ('last_analyzed', models.DateTimeField(null=True, verbose_name='last time analyzed')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account_check', to='twitter.twitteraccount')),
                ('requests', models.ManyToManyField(related_name='accounts_to_analyze', to='client.ClientAccount')),
            ],
        ),
    ]
