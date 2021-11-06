from django.urls import path
from . import handlers


urlpatterns = [
    path("spareparts-requests", handlers.spareparts_requests_handler),
    path(
        "change-maintenance-request-device-status/<int:maintenance_request_id>",
        handlers.change_maintenance_request_devices_status_handler,
    ),
    path("supply-requests", handlers.supply_requests_handlers),
    path("system-logs", handlers.system_logs_handler),
    path("maintenance-request-logs", handlers.maintenace_request_logs_handler),
]
