from django.db import models
from accounts.models import User
from storage.models import Item
from maintenance_requests.models import MaintenanceRequestDevice, MaintenanceRequest
from clients.models import Client

# Create your models here.
class SparepartRequest(models.Model):
    maintenance_request_device = models.ForeignKey(
        MaintenanceRequestDevice,
        on_delete=models.CASCADE,
        verbose_name="Maintenace request",
        null=True,
        blank=True,
    )
    requested_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Requested by"
    )
    sparepart = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name="Sparepart"
    )
    qty = models.IntegerField(verbose_name="QTY")
    warehouse_proceeded = models.BooleanField(
        default=False, verbose_name="Warehouse proceeded"
    )
    supervisor_proceeded = models.BooleanField(
        default=False, verbose_name="Supervisor proceeded"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Sparepart request"
        verbose_name_plural = "Spareparts requests"

    def __str__(self):
        return f"New sparepart request by {self.requested_by.first_name} {self.requested_by.last_name} for {self.sparepart.item_name}"


class ChangeMaintenanceRequestDeviceStatus(models.Model):
    maintenance_request_device = models.ForeignKey(
        MaintenanceRequestDevice,
        on_delete=models.CASCADE,
        verbose_name="Maintenance request device",
    )
    requested_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Requested by"
    )
    notes = models.TextField(verbose_name="Notes")
    requested_status = models.CharField(
        max_length=350, verbose_name="Requested status", null=True, blank=True
    )
    is_proceeded = models.BooleanField(default=False, verbose_name="Is proceeded")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Change maintenace request device"
        verbose_name_plural = "Change maintenace request devices"

    def __str__(self):
        return f"Change maintenace request device for {self.maintenance_request_device} by {self.requested_by}"


class SupplyRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Item")
    qty = models.IntegerField(verbose_name="QTY")
    total = models.FloatField(verbose_name="Total")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Supply request"
        verbose_name_plural = "Supply requests"

    def __str__(self):
        return (
            f"New supply request to - {self.client.client_name} - {self.item.item_name}"
        )


class SystemLog(models.Model):
    action_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Action by"
    )
    action = models.TextField(verbose_name="Action")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "System log"
        verbose_name_plural = "System logs"

    def __str__(self):
        return f"action - {self.action} by - {self.action_by.first_name} {self.action_by.last_name}"


class MaintenanceRequestLog(models.Model):
    maintenance_request = models.ForeignKey(
        MaintenanceRequest, on_delete=models.CASCADE, verbose_name="Maintenace request"
    )
    action_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Action by"
    )
    action = models.TextField(verbose_name="Action")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Maintenace request log"
        verbose_name_plural = "Maintenace request logs"

    def __str__(self):
        return f"action - {self.action} by - {self.action_by.first_name} {self.action_by.last_name}"
