from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=350, verbose_name="Client name")
    address = models.CharField(max_length=350, verbose_name="Address")
    phone_number_1 = models.CharField(max_length=350, verbose_name="Phone number 1")
    phone_number_2 = models.CharField(
        max_length=350, verbose_name="Phone number 2", null=True, blank=True
    )
    fax = models.CharField(max_length=350, verbose_name="Fax", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.client_name


class ClientDevice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    model = models.CharField(max_length=350, verbose_name="Model")
    serial_number = models.CharField(max_length=350, verbose_name="Serial number")
    img = models.ImageField(upload_to="uploads/clients_devices", null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Added at")

    class Meta:
        verbose_name = "Client device"
        verbose_name_plural = "Client devices"

    def __str__(self):
        return self.serial_number
