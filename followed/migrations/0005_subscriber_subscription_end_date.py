# Generated by Django 3.2.15 on 2022-12-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followed', '0004_auto_20221203_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='subscription_end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='subscription end date'),
        ),
    ]
