from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification
from meiduo_main.verializer.skuSerializer import SkuSerializer

from meiduo_main.utils import PageUnm


class SkuViewSet(ModelViewSet):
    parser_classes = [IsAdminUser]
    queryset = SPUSpecification.objects.all()
    serializer_class = SkuSerializer
    pagination_class = PageUnm