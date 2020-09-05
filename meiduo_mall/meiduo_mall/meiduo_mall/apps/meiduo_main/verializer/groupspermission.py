from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group
class GroupPermssionSerialzier(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'