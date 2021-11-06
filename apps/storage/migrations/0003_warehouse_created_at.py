# Generated by Django 3.2.5 on 2021-10-15 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_rename_name_warehouse_warehouse_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
    ]
