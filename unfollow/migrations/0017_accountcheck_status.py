# Generated by Django 3.2.13 on 2022-09-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unfollow', '0016_accountcheck_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountcheck',
            name='status',
            field=models.CharField(choices=[('RE', 'Requested'), ('IP', 'In progress'), ('CP', 'Complete'), ('ER', 'Error')], default='RE', max_length=2),
        ),
    ]
