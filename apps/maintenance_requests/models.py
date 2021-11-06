from django.db import models
from clients import models as clients_models
from accounts.models import User

# Create your models here.
class MaintenanceRequest(models.Model):
    client = models.ForeignKey(
        clients_models.Client, on_delete=models.CASCADE, verbose_name="Client"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Created by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False, verbose_name="is closed")

    class Meta:
        verbose_name = "Maintenance request"
        verbose_name_plural = "Maintenance requests"

    def __str__(self):
        return f"{self.client.client_name}-{self.id}"


class MaintenanceRequestDevice(models.Model):
    maintenance_request = models.ForeignKey(
        MaintenanceRequest, on_delete=models.CASCADE, verbose_name="Maintenance request"
    )
    device = models.ForeignKey(
        clients_models.ClientDevice, on_delete=models.CASCADE, verbose_name="Device"
    )
    supervisor_notes = models.TextField(
        verbose_name="Supervisor notes", null=True, blank=True
    )
    status = models.CharField(
        max_length=350, verbose_name="Status", null=True, blank=True
    )
    engineer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Engineer", null=True, blank=True
    )

    class Meta:
        verbose_name = "Maintenance request device"
        verbose_name_plural = "Maintenance requests devices"

    def __str__(self):
        return f"{self.maintenance_request.id}-{self.device.id}"
