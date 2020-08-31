from rest_framework.serializers import ModelSerializer

from goods.models import SKU

from goods.models import GoodsVisitCount

from goods.models import GoodsCategory


class SkuSerializer(ModelSerializer):


    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'


class GoodsVisitSerializer(ModelSerializer):
    class Meta:
        model = GoodsCategory

        fields = "__all__"