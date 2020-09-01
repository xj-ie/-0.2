from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from goods.models import SKU

from goods.models import GoodsVisitCount

from goods.models import GoodsCategory

from goods.models import SPUSpecification

from goods.models import SpecificationOption


class SkuSerializer(ModelSerializer):


    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'


class GoodsVisitSerializer(ModelSerializer):
    class Meta:
        model = GoodsCategory

        fields = "__all__"


class SpecificationOptionSerializer(ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = '__all__'
class SPUSpecificationSerializer(ModelSerializer):
    options =  SpecificationOptionSerializer(many=True)
    # specificationoption_set = SpecificationOptionSerializer(many=True)
    class Meta:
        model = SPUSpecification
        fields = '__all__'