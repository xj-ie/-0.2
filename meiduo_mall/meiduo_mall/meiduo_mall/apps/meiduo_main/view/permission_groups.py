# from openpyxl.pivot.cache import Groups
from requests import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Group,Permission

from meiduo_main.utils import PageUnm
from meiduo_main.verializer.groupspermission import GroupPermssionSerialzier
from meiduo_main.verializer.permissionserialzier import PrermissionSeriazer


class PermssionGroupsView(ModelViewSet):
    queryset = Group.objects.all()
    # permission_classes = [IsAdminUser]
    serializer_class = GroupPermssionSerialzier
    pagination_class = PageUnm

    def simple(self,request):
        data = Permission.objects.all()
        res = PrermissionSeriazer(data,many=True)
        return Response(res.data)