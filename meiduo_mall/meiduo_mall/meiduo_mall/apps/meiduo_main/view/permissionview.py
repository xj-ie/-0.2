from django.contrib.auth.models import Permission, ContentType
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from meiduo_main.utils import PageUnm
from meiduo_main.verializer.permissionserialzier import PrermissionSeriazer,ContentTypeSerializer


class PermissionView(ModelViewSet):
    queryset = Permission.objects.all()
    pagination_class = PageUnm
    serializer_class = PrermissionSeriazer
    permission_classes = [IsAdminUser]
    def content_daty(self, request):
        data = ContentType.objects.all()
        res = ContentTypeSerializer(data,many=True)
        return Response(res.data)

