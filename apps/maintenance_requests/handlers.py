from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ast import literal_eval
from clients import models as clients_models
from accounts.models import User
from . import models, serializers

# Create your views here.
@api_view(["GET", "POST", "PUT"])
def maintenance_requests_handler(request):

    if request.method == "POST":
        client = clients_models.Client.objects.get(id=int(request.data.get("clientId")))
        devices = clients_models.ClientDevice.objects.filter(
            id__in=literal_eval(request.data.get("devices"))
        )

        maintenance_request = models.MaintenanceRequest.objects.create(
            client=client, created_by=request.user
        )
        maintenance_request_serializer = serializers.MaintenanceRequestSerializer(
            maintenance_request, many=False
        )

        for device in devices:
            client_device = clients_models.ClientDevice.objects.get(id=device.id)
            models.MaintenanceRequestDevice.objects.create(
                maintenance_request=maintenance_request,
                device=client_device,
                status="في الصيانة",
            ).save()

        return Response(
            status=status.HTTP_201_CREATED, data=maintenance_request_serializer.data
        )

    elif request.method == "GET":
        maintenance_requests = models.MaintenanceRequest.objects.all().order_by(
            "-created_at"
        )
        maintenance_requests_serializer = serializers.MaintenanceRequestSerializer(
            maintenance_requests, many=True
        )

        return Response(
            status=status.HTTP_200_OK, data=maintenance_requests_serializer.data
        )

    elif request.method == "PUT":
        maintenance_request = models.MaintenanceRequest.objects.get(
            id=int(request.data.get("maintenanceRequestId"))
        )

        maintenance_request.is_closed = bool(
            request.data.get("closeMaintenanceRequest")
        )

        maintenance_request.save()

        maintenance_requests = models.MaintenanceRequest.objects.all().order_by(
            "-created_at"
        )
        maintenance_requests_serializer = serializers.MaintenanceRequestSerializer(
            maintenance_requests, many=True
        )

        return Response(
            status=status.HTTP_200_OK, data=maintenance_requests_serializer.data
        )


@api_view(["GET"])
def user_maintenance_requests_finder(request, user_id):
    user = User.objects.get(id=user_id)

    maintenance_request_devices = models.MaintenanceRequestDevice.objects.filter(
        engineer=user
    )

    maintenance_requests_ids = []

    for maintenance_request_device in maintenance_request_devices:
        if (
            maintenance_request_device.maintenance_request
            not in maintenance_requests_ids
        ):
            maintenance_requests_ids.append(
                maintenance_request_device.maintenance_request.id
            )
    maintenance_requests = models.MaintenanceRequest.objects.filter(
        id__in=maintenance_requests_ids
    ).order_by("-created_at")
    maintenance_requests_serializer = serializers.MaintenanceRequestSerializer(
        maintenance_requests, many=True
    )

    return Response(
        status=status.HTTP_200_OK, data=maintenance_requests_serializer.data
    )


@api_view(["GET", "PUT"])
def maintenanceRequestDevicesHandler(request, maintenance_request_id):

    if request.method == "PUT":
        maintenance_request_device = models.MaintenanceRequestDevice.objects.get(
            id=int(request.data.get("deviceId"))
        )

        maintenance_request_device.supervisor_notes = (
            request.data.get("supervisorNotes")
            or maintenance_request_device.supervisor_notes
        )

        maintenance_request_device.engineer = (
            User.objects.get(id=int(request.data.get("engineerId")))
            if request.data.get("engineerId")
            else maintenance_request_device.engineer
        )

        maintenance_request_device.status = (
            request.data.get("status") or maintenance_request_device.status
        )

        maintenance_request_device.save()

    maintenance_request = models.MaintenanceRequest.objects.get(
        id=maintenance_request_id
    )
    maintenance_request_devices = models.MaintenanceRequestDevice.objects.filter(
        maintenance_request=maintenance_request
    )
    maintenance_request_devices_serializer = (
        serializers.MaintenanceRequestsDeviceSerializer(
            maintenance_request_devices, many=True
        )
    )
    return Response(
        status=status.HTTP_200_OK, data=maintenance_request_devices_serializer.data
    )
