from django.urls import path
from . import handlers

urlpatterns = [path("items-categories", handlers.items_categories_handler)]
