from django.urls import path
from . import handlers

urlpatterns = [
    path("warehouses", handlers.warehouses_handler),
    path("items", handlers.items_handler),
]
