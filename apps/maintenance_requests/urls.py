from django.urls import path
from . import handlers


urlpatterns = [
    path("maintenance-requests-data", handlers.maintenance_requests_handler),
    path(
        "user-maintenance-requests-data/<int:user_id>",
        handlers.user_maintenance_requests_finder,
    ),
    path(
        "maintenance-request-devices/<int:maintenance_request_id>",
        handlers.maintenanceRequestDevicesHandler,
    ),
]
