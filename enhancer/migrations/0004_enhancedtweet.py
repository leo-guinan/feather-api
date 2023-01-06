# Generated by Django 3.2.16 on 2022-12-30 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_includedlink'),
        ('enhancer', '0003_enhancedtwitteraccount_likely_spam'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnhancedTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embeddings', models.JSONField(blank=True, null=True)),
                ('enhancement_run_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OK', 'Okay'), ('ER', 'Error')], default='OK', max_length=2)),
                ('categories', models.CharField(blank=True, max_length=255, null=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.tweet')),
            ],
        ),
    ]