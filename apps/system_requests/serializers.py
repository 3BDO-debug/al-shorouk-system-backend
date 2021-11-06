from rest_framework.serializers import ModelSerializer
from . import models


class SparepartRequestSerializer(ModelSerializer):
    class Meta:
        model = models.SparepartRequest
        fields = "__all__"

    def to_representation(self, instance):
        data = super(SparepartRequestSerializer, self).to_representation(instance)
        data[
            "requested_by_name"
        ] = f"{instance.requested_by.first_name} {instance.requested_by.last_name}"
        data["requested_by_profile_pic"] = instance.requested_by.profile_pic.name
        data["sparepart_name"] = instance.sparepart.item_name
        data["sparepart_img"] = instance.sparepart.item_img.name
        data["warehouse"] = instance.sparepart.warehouse.warehouse_name
        return data


class ChangeMaintenanceRequestDeviceStatusSerializer(ModelSerializer):
    class Meta:
        model = models.ChangeMaintenanceRequestDeviceStatus
        fields = "__all__"

    def to_representation(self, instance):
        data = super(
            ChangeMaintenanceRequestDeviceStatusSerializer, self
        ).to_representation(instance)
        data[
            "requested_by_name"
        ] = f"{instance.requested_by.first_name} {instance.requested_by.last_name}"
        data["requested_by_profile_pic"] = instance.requested_by.profile_pic.name
        return data


class SupplyRequestSerializer(ModelSerializer):
    class Meta:
        model = models.SupplyRequest
        fields = "__all__"

    def to_representation(self, instance):
        data = super(SupplyRequestSerializer, self).to_representation(instance)
        data["warehouse"] = instance.item.warehouse.warehouse_name
        data["client_name"] = instance.client.client_name
        data["item_name"] = instance.item.item_name
        return data


class SystemLogSerializer(ModelSerializer):
    class Meta:
        model = models.SystemLog
        fields = "__all__"

    def to_representation(self, instance):
        data = super(SystemLogSerializer, self).to_representation(instance)
        data[
            "action_by_name"
        ] = f"{instance.action_by.first_name} {instance.action_by.last_name}"
        return data


class MaintenaceRequestLog(ModelSerializer):
    class Meta:
        model = models.MaintenanceRequestLog
        fields = "__all__"

    def to_representation(self, instance):
        data = super(MaintenaceRequestLog, self).to_representation(instance)
        data[
            "action_by_name"
        ] = f"{instance.action_by.first_name} {instance.action_by.last_name}"
        data["action_by_profile_pic"] = instance.action_by.profile_pic.name
        return data
