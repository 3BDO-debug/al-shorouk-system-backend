# Generated by Django 3.2.5 on 2021-10-19 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=350, verbose_name='Model')),
                ('serial_number', models.CharField(max_length=350, verbose_name='Serial number')),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads/clients_devices')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Added at')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Client device',
                'verbose_name_plural': 'Client devices',
            },
        ),
    ]
