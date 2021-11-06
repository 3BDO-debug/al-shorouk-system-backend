from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.models import User
from storage.models import Item
from maintenance_requests.models import MaintenanceRequestDevice
from clients.models import Client
from . import models, serializers

# Create your views here.
@api_view(["GET", "POST", "PUT"])
def spareparts_requests_handler(request):

    if request.method == "POST":
        maintenance_request_device = MaintenanceRequestDevice.objects.get(
            id=int(request.data.get("deviceId"))
        )
        requested_by = User.objects.get(id=request.user.id)
        sparepart = Item.objects.get(id=int(request.data.get("sparepart")))

        models.SparepartRequest.objects.create(
            maintenance_request_device=maintenance_request_device,
            requested_by=requested_by,
            sparepart=sparepart,
            qty=int(request.data.get("qty")),
        )

    elif request.method == "PUT":
        sparepart_request = models.SparepartRequest.objects.get(
            id=int(request.data.get("sparepartRequestId"))
        )

        sparepart_request.supervisor_proceeded = (
            True
            if request.data.get("proceedSupervisor")
            else sparepart_request.supervisor_proceeded
        )

        sparepart_request.warehouse_proceeded = (
            True
            if request.data.get("proceedWarehouse")
            else sparepart_request.warehouse_proceeded
        )

        sparepart_request.save()

        if request.data.get("supervisorRejected"):

            sparepart_request.delete()

    spareparts_requests = models.SparepartRequest.objects.all().order_by("-created_at")
    spareparts_requests_serializer = serializers.SparepartRequestSerializer(
        spareparts_requests, many=True
    )

    return Response(status=status.HTTP_200_OK, data=spareparts_requests_serializer.data)


@api_view(["GET", "POST", "PUT"])
def change_maintenance_request_devices_status_handler(request, maintenance_request_id):

    if request.method == "POST":
        models.ChangeMaintenanceRequestDeviceStatus.objects.create(
            maintenance_request_device=MaintenanceRequestDevice.objects.get(
                id=int(request.data.get("deviceId"))
            ),
            requested_by=User.objects.get(id=request.user.id),
            requested_status=request.data.get("requestedStatus"),
            notes=request.data.get("notes"),
        ).save()

    elif request.method == "PUT":
        change_maintenance_request_device_status = (
            models.ChangeMaintenanceRequestDeviceStatus.objects.get(
                id=int(request.data.get("requestId"))
            )
        )

        change_maintenance_request_device_status.is_proceeded = True

        change_maintenance_request_device_status.save()

    maintenance_request_devices_requests = (
        models.ChangeMaintenanceRequestDeviceStatus.objects.filter(
            is_proceeded=True,
        )
    ).delete()

    maintenance_request_devices_requests = (
        models.ChangeMaintenanceRequestDeviceStatus.objects.filter(
            maintenance_request_device__maintenance_request__id=maintenance_request_id,
        )
    ).order_by("-created_at")
    maintenance_request_devices_requests_serializer = (
        serializers.ChangeMaintenanceRequestDeviceStatusSerializer(
            maintenance_request_devices_requests, many=True
        )
    )

    return Response(
        status=status.HTTP_200_OK,
        data=maintenance_request_devices_requests_serializer.data,
    )


@api_view(["GET", "POST"])
def supply_requests_handlers(request):

    if request.method == "POST":
        client = Client.objects.get(id=int(request.data.get("clientId")))
        item = Item.objects.get(id=int(request.data.get("itemId")))
        qty = int(request.data.get("qty"))

        models.SupplyRequest.objects.create(
            client=client, item=item, qty=qty, total=float(qty) * item.ppu
        ).save()

    supply_requests = models.SupplyRequest.objects.all().order_by("-created_at")
    supply_requests_serializer = serializers.SupplyRequestSerializer(
        supply_requests, many=True
    )
    return Response(status=status.HTTP_200_OK, data=supply_requests_serializer.data)


@api_view(["GET", "POST"])
def system_logs_handler(request):

    if request.method == "POST":
        action_by = User.objects.get(id=request.user.id)

        models.SystemLog.objects.create(
            action_by=action_by, action=request.data.get("action")
        ).save()

    system_logs = models.SystemLog.objects.all().order_by("-created_at")
    system_logs_serializer = serializers.SystemLogSerializer(system_logs, many=True)
    return Response(status=status.HTTP_200_OK, data=system_logs_serializer.data)


@api_view(["GET", "POST"])
def maintenace_request_logs_handler(request):

    if request.method == "POST":
        maintenance_request = models.MaintenanceRequest.objects.get(
            id=int(request.data.get("maintenanceRequestId"))
        )
        action_by = User.objects.get(id=request.user.id)

        models.MaintenanceRequestLog.objects.create(
            maintenance_request=maintenance_request,
            action_by=action_by,
            action=request.data.get("action"),
        ).save()

    maintenace_requests_logs = models.MaintenanceRequestLog.objects.all().order_by(
        "-created_at"
    )
    maintenace_requests_logs_serializer = serializers.MaintenaceRequestLog(
        maintenace_requests_logs, many=True
    )
    return Response(
        status=status.HTTP_200_OK, data=maintenace_requests_logs_serializer.data
    )
