from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from goods.models import SPUSpecification

from goods.models import SPU


class SkuSerializer(ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = '__all__'

class SpuSerializer(ModelSerializer):
    name = serializers.CharField(read_only=True)
    class Meta:
        model = SPU
        fields = ("id","name")