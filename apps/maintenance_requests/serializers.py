from rest_framework.serializers import ModelSerializer
from . import models


class MaintenanceRequestSerializer(ModelSerializer):
    class Meta:
        model = models.MaintenanceRequest
        fields = "__all__"

    def to_representation(self, instance):
        data = super(MaintenanceRequestSerializer, self).to_representation(instance)
        data["client_name"] = instance.client.client_name
        data[
            "created_by_full_name"
        ] = f"{instance.created_by.first_name} {instance.created_by.last_name}"
        return data


class MaintenanceRequestsDeviceSerializer(ModelSerializer):
    class Meta:
        model = models.MaintenanceRequestDevice
        fields = "__all__"

    def to_representation(self, instance):
        data = super(MaintenanceRequestsDeviceSerializer, self).to_representation(
            instance
        )
        data["model"] = instance.device.model
        data["serial_number"] = instance.device.serial_number
        if instance.engineer:
            data["assigned_engineer"] = {
                "name": f"{instance.engineer.first_name} {instance.engineer.last_name}",
                "profile_pic": instance.engineer.profile_pic.name,
            }
        return data
