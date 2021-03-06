"""web URL Configuration

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
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^goodslist/$', views.goods_list, name='goods_list'),
    url(r'^goodslist/discount/$', views.goods_list_discount, name="goods_list_discount"),
    url(r'^goodslist/popluar/$', views.goods_list_popular, name="goods_list_popular"),
    url(r'^details/$', views.details, name='details'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^personal/$', views.personal, name='personal'),
    url(r'^user/edit/$', views.user_edit, name="user_edit"),

    # 购物车 和 订单
    url(r'^cart/add/$', views.cart_add, name='cart_add'),
    url(r'^cart/del$', views.cart_del, name='cart_del'),
    url(r'^cart/details/$', views.cart_details, name='cart_delall'),
    url(r'^cart/editnum/$', views.cart_editnum, name='cart_editnum'),
    url(r'^myorder/$', views.myorder, name='myorder'),
    url(r'^addres/add/', views.addres_add, name="addres_add"),
    url(r'^addres/list/$', views.addres_list, name="addres_list"),
    url(r'^addres/edit/$', views.addres_edit, name="addres_edit"),
    url(r'^myorder/list/$', views.myorder_list, name="myorder_list"),
    url(r'^myorder/desc/$', views.myorder_desc, name="myorder_desc"),

    # click record
    url(r'^good/click/$', views.good_click, name="good_click"),
    url(r'^good/rec/$', views.good_rec, name="good_rec"),
    url(r'^search/$', views.search, name="search")


]
