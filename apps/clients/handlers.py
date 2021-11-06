import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

# Create your views here.


@api_view(["GET", "POST"])
def clients_handler(request):

    if request.method == "POST":
        request_data = json.loads(request.data.get("values"))
        models.Client.objects.create(
            client_name=request_data["clientName"],
            address=request_data["address"],
            phone_number_1=request_data["phoneNumber1"],
            phone_number_2=request_data["phoneNumber2"],
            fax=request_data["fax"],
        ).save()

    clients = models.Client.objects.all().order_by("-created_at")
    clients_serializer = serializers.ClientSerializer(clients, many=True)
    return Response(status=status.HTTP_200_OK, data=clients_serializer.data)


@api_view(["GET", "POST"])
def client_devices_handler(request, client_id):

    client = models.Client.objects.get(id=client_id)

    if request.method == "POST":

        request_data = json.loads(request.data.get("values"))
        request_files = request.data.get("files")

        models.ClientDevice.objects.create(
            client=client,
            model=request_data["model"],
            serial_number=request_data["serial"],
            img=request_files,
        ).save()

    client_devices = models.ClientDevice.objects.filter(client=client).order_by(
        "-added_at"
    )
    client_devices_serializer = serializers.ClientDeviceSerializer(
        client_devices, many=True
    )
    return Response(status=status.HTTP_200_OK, data=client_devices_serializer.data)
