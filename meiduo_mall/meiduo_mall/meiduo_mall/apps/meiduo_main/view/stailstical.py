# import time
from datetime import date,timedelta
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from users.models import User

from goods.models import GoodsVisitCount

from meiduo_main.utils import GoodsDaySerializer


class UserCountView(APIView):
    """
    权限指定
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZW1haWwiOiIxQDEuY29tIiwiZXhwIjoxNTk4NjEyMzkwLCJ1c2VyX2lkIjoyfQ.34V2MoK4ELOwlWRCr49pjO6JoOccxT2VI68ipESJRj4"
    """
    parser_classes = [IsAdminUser]
    def get(self, reqest):
        """
            用户总量统计
        :param reqest:
        :return:
        """
        now_date = date.today()
        user = User.objects.all().count()

        context = {"count":user,
                   "date":now_date}
        return Response(context)

class UserDayCountView(APIView):
    """
    权限指定
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZW1haWwiOiIxQDEuY29tIiwiZXhwIjoxNTk4NjEyMzkwLCJ1c2VyX2lkIjoyfQ.34V2MoK4ELOwlWRCr49pjO6JoOccxT2VI68ipESJRj4"
    """
    parser_classes = [IsAdminUser]
    def get(self, request):
        now_date = date.today()
        user = User.objects.filter(date_joined__gte=now_date).count()
        context = {"count":user,
                   "date":now_date}
        return Response(context)

class UserDayActivateCountView(APIView):
    parser_classes = [IsAdminUser]
    def get(self, request):
        new_date = date.today()
        user_count = User.objects.filter(last_login__gte=new_date).count()
        context = {
            'count':user_count,
            "date":new_date

        }
        return Response(context)

class UserDayOrderCountView(APIView):
    parser_classes = [IsAdminUser]
    def get(self, request):
        new_date = date.today()
        user_count = len(set(User.objects.filter(orders__create_time__gte=new_date)))
        # user_count=User.objects.filter(orders__create_time__gte=new_date).count()

                                               # orders__create_time__gte = now_date
        context = {
            'count':user_count,
            'date':new_date
        }
        return Response(context)
class UserMonthCountView(APIView):
    # 指定管理员权限
    parser_classes = [IsAdminUser]

    def get(self, request):
        new_date = date.today()
        new_ee_date = new_date - timedelta(30)
        new_date_i = []
        for i in range(30):
            new_ee_date += timedelta(1)
            new_date_i.append(new_ee_date)
        context = [{'count':User.objects.filter(date_joined__gte=dates,date_joined__lt=dates+timedelta(1)).count(),
            'date':dates} for dates in new_date_i]
        return Response(context)

class GoodsDayView(APIView):
    parser_classes = [IsAdminUser]
    def get(self, request):
        new_date = date.today()
        goods = GoodsVisitCount.objects.filter(date__gte=new_date)
        res = GoodsDaySerializer(goods, many=True)

        return Response(res.data)