# Generated by Django 3.2.13 on 2022-07-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_client_twitter_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='auth_version',
            field=models.CharField(choices=[('V1', 'Oauth V1'), ('V2', 'Oauth V2')], default='V1', max_length=2),
        ),
    ]
