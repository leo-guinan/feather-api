# Generated by Django 3.2.16 on 2023-01-02 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_includedlink'),
        ('enhancer', '0007_alter_enhancedtweet_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enhancedtweet',
            name='tweet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enhanced', to='twitter.tweet'),
        ),
    ]
