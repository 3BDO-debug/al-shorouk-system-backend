from rest_framework.serializers import ModelSerializer
from . import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data["profile_pic_name"] = instance.profile_pic.name

        return data
