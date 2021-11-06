from rest_framework.serializers import ModelSerializer
from . import models


class ItemCategorySerializer(ModelSerializer):
    class Meta:
        model = models.ItemCategory
        fields = "__all__"
