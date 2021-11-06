# Generated by Django 3.2.5 on 2021-10-29 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_requests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system_requests', '0003_sparepartrequest_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeMaintenanceRequestDeviceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(verbose_name='Notes')),
                ('status', models.CharField(blank=True, max_length=350, null=True, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('maintenance_request_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_requests.maintenancerequestdevice', verbose_name='Maintenance request device')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Requested by')),
            ],
            options={
                'verbose_name': 'Change maintenace request device',
                'verbose_name_plural': 'Change maintenace request devices',
            },
        ),
    ]
