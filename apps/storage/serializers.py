from . import models
from rest_framework.serializers import ModelSerializer


class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = "__all__"

    def to_representation(self, instance):
        data = super(WarehouseSerializer, self).to_representation(instance)
        data[
            "assigned_to_name"
        ] = f"{instance.assigned_to.first_name} {instance.assigned_to.last_name}"
        data["assigned_to_profile_pic"] = instance.assigned_to.profile_pic.name

        return data


class ItemSerializer(ModelSerializer):
    class Meta:
        model = models.Item
        fields = "__all__"

    def to_representation(self, instance):
        data = super(ItemSerializer, self).to_representation(instance)
        data["warehouse_name"] = instance.warehouse.warehouse_name
        data["category_name"] = instance.category.category_name
        return data
