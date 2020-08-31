from django.conf import settings
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from fdfs_client.client import Fdfs_client

from goods.models import SKUImage,SKU

from meiduo_main.utils import PageUnm

from meiduo_main.verializer.SPUIamgeSerializer import IamgeSerializer

from meiduo_main.verializer.SPUIamgeSerializer import SkuSerializer


class ImageView(ModelViewSet):

    parser_classes = [IsAdminUser]
    queryset = SKUImage.objects.all()
    serializer_class = IamgeSerializer
    pagination_class = PageUnm
    def get_image(self,request):
        sku = SKU.objects.all()
        res = SkuSerializer(sku,many=True)
        return Response(res.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        ser =self.get_serializer(data=data)
        ser.is_valie()
        c = Fdfs_client(settings.FDFS_CONF_URL)
        filter = request.FILES.get("image")
        res = c.upload_appender_by_buffer(filter.read())
        # if filter
        image_url = res['Remote file_id']
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 保存图片
        img = SKUImage.objects.create(sku_id=sku_id, image=image_url)
        return img
    def update(self, request, *args, **kwargs):
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valie()
        c = Fdfs_client(settings.FDFS_CONF_URL)
        filter = request.FILES.get("image")
        res = c.upload_appender_by_buffer(filter.read())
        # if filter
        image_url = res['Remote file_id']
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        img = SKUImage.objects.get(id=kwargs['pk'])
        # 更新图片
        img.image = image_url
        img.save()
        return img