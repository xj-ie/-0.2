from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from users.models import User

from meiduo_main.verializer.users import UerShow

from meiduo_main.utils import PageUnm


class UserView(ListCreateAPIView):
    # parser_classes = [IsAdminUser]
    # queryset = User.objects.all()
    serializer_class = UerShow
    # 指定使用的序列化器
    pagination_class = PageUnm
    def get_queryset(self):
        if self.request.query_params.get('keyword') == None:
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=self.request.query_params.get('keyword'))
    # def get_serializer(self, *args, **kwargs):
    #     pass
