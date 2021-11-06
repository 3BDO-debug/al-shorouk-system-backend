from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    category_name = models.CharField(max_length=350, verbose_name="Category name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Item category"
        verbose_name_plural = "Item categories"

    def __str__(self):
        return self.category_name
