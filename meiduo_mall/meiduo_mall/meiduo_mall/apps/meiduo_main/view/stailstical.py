# import time
from datetime import date
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from users.models import User


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