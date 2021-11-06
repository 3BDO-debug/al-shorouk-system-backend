from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.SparepartRequest)
admin.site.register(models.ChangeMaintenanceRequestDeviceStatus)
admin.site.register(models.SupplyRequest)
