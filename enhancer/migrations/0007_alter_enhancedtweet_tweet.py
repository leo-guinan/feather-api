# Generated by Django 3.2.16 on 2023-01-02 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_includedlink'),
        ('enhancer', '0006_enhancedtweet_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enhancedtweet',
            name='tweet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='twitter.tweet'),
        ),
    ]
