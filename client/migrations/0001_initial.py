# Generated by Django 3.2.13 on 2022-06-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('twitter', '0001_initial'),
        ('rest_framework_api_key', '0005_auto_20220110_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name of the client')),
                ('api_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_framework_api_key.apikey')),
            ],
        ),
        migrations.CreateModel(
            name='ClientAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, verbose_name='twitter oauth2 token')),
                ('email', models.CharField(max_length=255, verbose_name='account email address')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='client.client')),
                ('twitter_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_accounts', to='twitter.twitteraccount')),
            ],
        ),
    ]
