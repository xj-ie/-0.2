from rest_framework.serializers import ModelSerializer

from goods.models import SKUImage

from goods.models import SKU


class IamgeSerializer(ModelSerializer):
   class Meta:
       model = SKUImage
       fields = '__all__'

class SkuSerializer(ModelSerializer):
    class Meta:
        model = SKU
        fields = ('id', 'name')