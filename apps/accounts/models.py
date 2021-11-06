from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gov_id = models.CharField(max_length=350, verbose_name="GOV ID")
    phone_number = models.CharField(max_length=350, verbose_name="Phone number")
    address = models.CharField(max_length=350, verbose_name="Address")
    profile_pic = models.ImageField(
        upload_to="uploads/users_profile_pics", verbose_name="Profile pic"
    )
    role = models.CharField(max_length=350, verbose_name="Role")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
