# Generated by Django 3.2.13 on 2022-07-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20220706_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaccount',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='account email address'),
        ),
    ]
