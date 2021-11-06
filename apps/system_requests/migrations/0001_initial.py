# Generated by Django 3.2.5 on 2021-10-27 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparepartRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='QTY')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Requested by')),
                ('sparepart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.item', verbose_name='Sparepart')),
            ],
            options={
                'verbose_name': 'Sparepart request',
                'verbose_name_plural': 'Spareparts requests',
            },
        ),
    ]
