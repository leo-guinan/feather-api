# Generated by Django 3.2.13 on 2022-07-17 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20220716_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetaAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beta_code', models.CharField(max_length=255, verbose_name='beta access code')),
                ('client_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beta', to='client.clientaccount')),
            ],
        ),
    ]