from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from users.models import User

from meiduo_main.verializer.users import UerShow

from meiduo_main.utils import PageUnm


class UserView(ListAPIView):
    parser_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UerShow
    # 指定使用的序列化器
    pagination_class = PageUnm