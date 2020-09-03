from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Permission,ContentType

class PrermissionSeriazer(ModelSerializer):


    class Meta:


        model = Permission

        fields = "__all__"

class ContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ContentType
        fields = ("id","name")