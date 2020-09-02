
from rest_framework import serializers

from goods.models import GoodsVisitCount
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


class GoodsDaySerializer(serializers.Serializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GoodsVisitCount
        fields = ('count', 'category')


class PageUnm(PageNumberPagination):
    page_size = 5
    page_query_description = 'pagesize'
    max_page_size = 10
    def get_paginated_response(self, data):
        # return Response(OrderedDict([
        #     ('count', self.page.paginator.count),
        #     ('next', self.get_next_link()),
        #     ('previous', self.get_previous_link()),
        #     ('results', data)
        # ]))

        return Response({"count":self.page.paginator.count,
                        "lists":data,
                        "page":self.page.number,
                        "pages":self.page.paginator.num_pages,
                        "pagesize":self.max_page_size,
                        })
        # return Response({
        #     'count': self.page.paginator.count,  # 总数量
        #     'lists': data,  # 用户数据
        #     'page': self.page.number,  # 当前页数
        #     'pages': self.page.paginator.num_pages,  # 总页数
        #     'pagesize': self.page_size  # 后端指定的页容量
        #
        # })