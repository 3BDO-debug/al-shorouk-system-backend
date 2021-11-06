# Generated by Django 3.2.5 on 2021-11-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ppt',
            field=models.FloatField(default=0.0, verbose_name='Price per unit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warehouse',
            name='cash_drawer',
            field=models.FloatField(default=0.0, verbose_name='Cash drawer'),
            preserve_default=False,
        ),
    ]
