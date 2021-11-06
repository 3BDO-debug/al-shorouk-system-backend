from django.urls import path
from . import handlers


urlpatterns = [
    path("clients-data", handlers.clients_handler),
    path("client-devices/<int:client_id>", handlers.client_devices_handler),
]
