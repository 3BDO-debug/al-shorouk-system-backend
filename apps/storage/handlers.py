import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import models, serializers
from accounts.models import User
from configurations.models import ItemCategory


@api_view(["GET", "POST"])
def warehouses_handler(request):
    if request.method == "POST":
        assigned_to = User.objects.get(id=int(request.data.get("assignTo")))
        models.Warehouse.objects.create(
            assigned_to=assigned_to, warehouse_name=request.data.get("warehouseName")
        ).save()

    warehouses = models.Warehouse.objects.all()
    warehouses_serializer = serializers.WarehouseSerializer(warehouses, many=True)
    return Response(status=status.HTTP_200_OK, data=warehouses_serializer.data)


@api_view(["GET", "POST", "PUT"])
def items_handler(request):

    if request.method == "POST":

        related_warehouse = models.Warehouse.objects.get(
            id=int(request.GET.get("warehouseId"))
        )
        request_data = json.loads(request.data.get("values"))
        request_files = request.data.get("files")
        related_category = ItemCategory.objects.get(
            id=int(request_data["category"]["id"])
        )

        models.Item.objects.create(
            warehouse=related_warehouse,
            category=related_category,
            item_name=request_data["itemName"],
            item_img=request_files,
            qty=int(request_data["qty"]),
            ppu=float(request_data["ppu"]),
        ).save()

    elif request.method == "PUT":
        item = models.Item.objects.get(id=int(request.data.get("itemId")))
        item.qty = int(request.data.get("qty"))
        item.save()

    items = models.Item.objects.all()
    items_serializer = serializers.ItemSerializer(items, many=True)
    return Response(status=status.HTTP_200_OK, data=items_serializer.data)
