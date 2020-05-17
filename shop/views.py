from django.shortcuts import render
from .models import Goods, User,GoodsType
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.hashers import make_password, check_password
import json
import datetime
# Create your views here.


def index(request):
    if not request.session.get('user', None):
        # 最为流行的商品 轮播图的商品
        popular_goods = Goods.objects.filter(popular=100)
        # 页面第二列放一些 打折中商品
        discount_goods = Goods.objects.filter(discount=0.8)
        sub_type = []
        good_types_one = GoodsType.objects.filter(type_level=1)
        for type in good_types_one:
            sub_type.append(GoodsType.objects.filter(paren_id=type.id))
    else:
        print("user")  # 根据用户信息过滤 出一些商品
    return render(request, 'shop/index.html', {'goods': popular_goods, 'discount': discount_goods})


def login(request):

    if request.method == "POST":
        user_info = json.loads(request.body)
        user = User.objects.filter(username=user_info.get("username"))
        if check_password(user_info.get('password'), user[0].password):
            response = {"responseCode": 200}
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            response = {"responseCode": 400, "error":  "密码错误"}
            return HttpResponseBadRequest(json.dumps(response), content_type="application/json")
    return render(request, 'shop/login_user.html')


def register(request):
    if request.method == "POST":
        user_info = json.loads(request.body)
        user = User()
        user.username = user_info.get("username")
        user.password = make_password(user_info.get("password"), None, "pbkdf2_sha256")
        user.add_time = datetime.date.today()
        user.save()
        response = {"resposeCode": 200}
        return HttpResponse(json.dumps(response), content_type="application/json")
    return render(request, 'shop/register.html')


def goods_list(request):

    type = request.GET.get('type')
    good_detail = Goods.objects.filter(good_type=type)

    return render(request, 'shop/goodslist.html', {'details': good_detail})


def details(request):
    rid = request.GET.get('id')
    good_detail = Goods.objects.filter(id=int(rid))
    tags = good_detail[0].tag
    return render(request, 'shop/details.html', {"detail": good_detail[0]})


def cart(request):
    print("details")
    return render(request, 'shop/cart.html')