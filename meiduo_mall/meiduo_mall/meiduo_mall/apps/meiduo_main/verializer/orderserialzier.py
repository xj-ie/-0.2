from rest_framework.serializers import ModelSerializer

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods


class SKUSerialzier(ModelSerializer):
    class Meta:
        model = SKU
        fields = ("name","default_image")

class OrderGoodsSerialzier(ModelSerializer):
    sku = SKUSerialzier(read_only=True)
    class Meta:
        model = OrderGoods
        fields = ('count','price','sku')
class OrderSeriazlier(ModelSerializer):

    skus=OrderGoodsSerialzier(read_only=True,many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'