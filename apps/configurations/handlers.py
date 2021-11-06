from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import models, serializers

# Create your views here.


@api_view(["GET"])
def items_categories_handler(request):
    items_categories = models.ItemCategory.objects.all()
    items_categories_serializer = serializers.ItemCategorySerializer(
        items_categories, many=True
    )
    return Response(status=status.HTTP_200_OK, data=items_categories_serializer.data)
