from django.db import models
from accounts.models import User
from configurations.models import ItemCategory

# Create your models here.
class Warehouse(models.Model):
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Assigned to"
    )
    warehouse_name = models.CharField(max_length=350, verbose_name="Name")
    cash_drawer = models.FloatField(default=0.00, verbose_name="Cash drawer")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"

    def __str__(self):
        return self.warehouse_name


class Item(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse"
    )
    category = models.ForeignKey(
        ItemCategory, on_delete=models.CASCADE, verbose_name="Category"
    )
    item_name = models.CharField(max_length=350, verbose_name="Item name")
    item_img = models.ImageField(
        upload_to="uploads/items_uploads",
        verbose_name="Item image",
        null=True,
        blank=True,
    )
    qty = models.IntegerField(verbose_name="QTY")
    ppu = models.FloatField(verbose_name="Price per unit")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name
