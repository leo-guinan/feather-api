# Generated by Django 3.2.13 on 2022-06-17 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchtweet', '0006_alter_replytotweet_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchtweet',
            name='children',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='watchtweet.watchtweet'),
        ),
    ]