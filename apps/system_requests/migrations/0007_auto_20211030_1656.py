# Generated by Django 3.2.5 on 2021-10-30 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_requests', '0002_maintenancerequest_is_closed'),
        ('system_requests', '0006_auto_20211029_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparepartrequest',
            name='maintenance_request',
        ),
        migrations.AddField(
            model_name='sparepartrequest',
            name='maintenance_request_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance_requests.maintenancerequestdevice', verbose_name='Maintenace request'),
        ),
        migrations.AddField(
            model_name='sparepartrequest',
            name='supervisor_proceeded',
            field=models.BooleanField(default=False, verbose_name='Supervisor proceeded'),
        ),
        migrations.AddField(
            model_name='sparepartrequest',
            name='warehouse_proceeded',
            field=models.BooleanField(default=False, verbose_name='Warehouse proceeded'),
        ),
    ]
