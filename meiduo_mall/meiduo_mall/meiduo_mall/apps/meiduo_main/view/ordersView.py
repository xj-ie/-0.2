from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser

from meiduo_main.utils import PageUnm
from meiduo_main.verializer.orderserialzier import OrderSeriazlier
from orders.models import OrderInfo


class OrdersView(ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = OrderSeriazlier
    pagination_class = PageUnm

    def get_queryset(self):
        if not self.request.query_params.get('keyword'):
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=self.request.query_params.get('keyword'))
    @action(methods=["put"], detail=True,)
    def status(self, request, pk):
        try:
            order = OrderInfo.objects.get(OrderInfo_id=pk)
        except Exception as e:
            raise e
        status = request.data.get("status")
        order.status = status
        order.save()

        return Response({"pk":pk,"status":status})


