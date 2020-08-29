"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .view.stailstical import UserCountView,UserDayCountView, UserDayActivateCountView, UserDayOrderCountView,UserMonthCountView,GoodsDayView
from .view import users,skuView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$', UserCountView.as_view()),
    url(r'^statistical/day_increment/$', UserDayCountView.as_view()),
    url(r'^statistical/day_activate/$', UserDayActivateCountView.as_view()),
    url(r'^statistical/day_order/$', UserDayOrderCountView.as_view()),
    url(r'^statistical/month/$', UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$',GoodsDayView.as_view()),
    url(r'^User/showuser/$',users.UserView.as_view()),
    url(r'^goods/simplie/$',skuView.SkuViewSet.as_view({"get":"simplie"}))
]

routes = DefaultRouter()
routes.register("goods/specs",skuView.SkuViewSet,base_name='skuview')
print(routes.urls)
urlpatterns += routes.urls