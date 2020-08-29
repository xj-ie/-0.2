from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from goods.models import SPUSpecification

class SkuSerializer(ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = '__all__'
