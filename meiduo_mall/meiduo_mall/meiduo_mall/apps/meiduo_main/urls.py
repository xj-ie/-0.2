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

from meiduo_main.view.ordersView import OrdersView
from meiduo_main.view.permissionview import PermissionView
from .view.stailstical import UserCountView,UserDayCountView, UserDayActivateCountView, UserDayOrderCountView,UserMonthCountView,GoodsDayView
from .view import users,skuView,SPUImageView,skuview
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$', UserCountView.as_view()),
    url(r'^statistical/day_increment/$', UserDayCountView.as_view()),
    url(r'^statistical/day_activate/$', UserDayActivateCountView.as_view()),
    url(r'^statistical/day_order/$', UserDayOrderCountView.as_view()),
    url(r'^statistical/month/$', UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$',GoodsDayView.as_view()),
    url(r'^users/$',users.UserView.as_view()),
    url(r'^goods/simple/$',skuView.SkuViewSet.as_view({"get":"simplie"})),
    url(r'^skus/images/$',SPUImageView.ImageView.as_view({"get":"get_image"})),
    url(r'^goods/(?P<pk>\d)/specs/$',skuview.SkuView.as_view({"get":"specs"})),
    url(r'^permission/content_types/$',PermissionView.as_view({"get":"content_daty"}))

    #WARNING basehttp 124 "GET /meiduo_admin/goods/2/specs/ HTTP/1.1" 404 14495

]

routes = DefaultRouter()
routes.register("goods/specs",skuView.SkuViewSet,base_name='skuview')
print("SKU",routes.urls)
urlpatterns += routes.urls

#
# class B(object):
#     pass
routes_image = DefaultRouter()
routes_image.register("skus/simple/",SPUImageView.ImageView,base_name='Iamge_view')
print("IMG:",routes_image.urls)
urlpatterns += routes_image.urls


route_sku = DefaultRouter()
route_sku.register('skus',skuview.SkuView, base_name='SKUVIEW')
print('SKU:',route_sku.urls)
urlpatterns += route_sku.urls



route_order = DefaultRouter()
route_order.register('orders',OrdersView, base_name="ORdersView")
print("order",route_order.urls)
urlpatterns += route_order.urls



route_permission = DefaultRouter()
route_permission.register('permission/perms',PermissionView,base_name="permissionview")
print('permssion:',route_permission.urls)
urlpatterns += route_permission.urls