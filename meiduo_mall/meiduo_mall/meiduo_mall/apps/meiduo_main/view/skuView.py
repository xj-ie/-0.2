from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from goods.models import SPUSpecification
from meiduo_main.verializer.skuSerializer import SkuSerializer,SpuSerializer
from meiduo_main.utils import PageUnm
from goods.models import SPU




class SkuViewSet(ModelViewSet):
    parser_classes = [IsAdminUser]
    queryset = SPUSpecification.objects.all()
    serializer_class = SkuSerializer
    pagination_class = PageUnm

    def simplie(self, request):
        sup = SPU.objects.all()
        res = SpuSerializer(sup,many=True)
        return Response(res.data)
