# Generated by Django 3.2.5 on 2021-10-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_requests', '0004_changemaintenancerequestdevicestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='changemaintenancerequestdevicestatus',
            name='is_proceeded',
            field=models.BooleanField(default=False, verbose_name='Is proceeded'),
        ),
    ]
