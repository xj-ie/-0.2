from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKU

from meiduo_main.utils import PageUnm

from meiduo_main.verializer.skuserializer import SkuSerializer

from goods.models import GoodsCategory

from meiduo_main.verializer.skuserializer import GoodsVisitSerializer

from goods.models import SPU

from meiduo_main.verializer.skuserializer import SPUSpecificationSerializer


class SkuView(ModelViewSet):
    queryset = SKU.objects.all()
    pagination_class = PageUnm
    serializer_class = SkuSerializer
    # parser_classes = [IsAdminUser]
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        if not self.request.query_params.get('keyword'):
            return SKU.objects.all()

        else:
            return SKU.objects.filter(username__contains=self.request.query_params.get('keyword'))



    @action(methods=['GET'],detail=False)
    def categories(self, request):
        category = GoodsCategory.objects.filter(subs__id=None)
        res = GoodsVisitSerializer(category,many=True)
        return Response(res.data)

    def specs(self,reqest,pk):
       spu = SPU.objects.get(id=pk)
       data = spu.specs.all()
       ser = SPUSpecificationSerializer(data,many=True)
       return Response(ser.data)