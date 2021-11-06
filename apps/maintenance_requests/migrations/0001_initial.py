# Generated by Django 3.2.5 on 2021-10-21 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0002_clientdevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Maintenance request',
                'verbose_name_plural': 'Maintenance requests',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceRequestDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_notes', models.TextField(blank=True, null=True, verbose_name='Supervisor notes')),
                ('status', models.CharField(blank=True, max_length=350, null=True, verbose_name='Status')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientdevice', verbose_name='Device')),
                ('engineer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Engineer')),
                ('maintenance_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_requests.maintenancerequest', verbose_name='Maintenance request')),
            ],
            options={
                'verbose_name': 'Maintenance request device',
                'verbose_name_plural': 'Maintenance requests devices',
            },
        ),
    ]