from django.shortcuts import render
from .models import Goods, User, GoodsType, address, OrderInfo, Order
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import json
import datetime


# Create your views here.
def index(request):
    if request.session.get('shoppingUser') is None:
        # 最为流行的商品 轮播图的商品
        popular_goods = Goods.objects.filter(popular=100)
        # 页面第二列放一些 打折中商品
        discount_goods = Goods.objects.filter(discount=0.8)
        sub_type = []
        good_types_one = GoodsType.objects.filter(type_level=1)
        for type in good_types_one:
            sub_type.append(GoodsType.objects.filter(paren_id=type.id))
        return render(request, 'shop/index.html',
                      {'goods': popular_goods, 'discount': discount_goods})
    else:
        user = request.session.get('shoppingUser')
        # 最为流行的商品 轮播图的商品
        popular_goods = Goods.objects.filter(popular=100)
        # 页面第二列放一些 打折中商品
        discount_goods = Goods.objects.filter(discount=0.8)
        sub_type = []
        good_types_one = GoodsType.objects.filter(type_level=1)
        for type in good_types_one:
            sub_type.append(GoodsType.objects.filter(paren_id=type.id))
        return render(request, 'shop/index.html', {'user': user, 'goods': popular_goods, 'discount': discount_goods})


def login(request):
    if request.method == "POST":
        user_info = json.loads(request.body)
        user = User.objects.filter(username=user_info.get("username"))
        if check_password(user_info.get('password'), user[0].password):
            response = {"responseCode": 200, 'username': user[0].username}
            request.session['shoppingUser'] = {"username": user[0].username,
                                       "userid": user[0].user_id,
                                       "status": user[0].status}
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            response = {"responseCode": 400, "error": "密码错误"}
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

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(good_detail, 10)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            good_detail = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            good_detail = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            good_detail = paginator.page(paginator.num_pages)

    return render(request, 'shop/goodslist.html', {'details': good_detail})


def details(request):
    rid = request.GET.get('id')
    good_detail = Goods.objects.filter(id=int(rid))
    tags = good_detail[0].tag
    return render(request, 'shop/details.html', {"detail": good_detail[0]})


def cart(request):
    if request.session.get('shoppingUser', None):
        print("hello")
    else:
        uid = request.session["shoppingUser"]["user_id"]
        status = request.GET.get("status", "0")
        if status == "0":
            date = Order.objects.filter(uid=uid)
        else:
            date = Order.objects.filter(uid=uid, status=status)
        print(date)
        return render(request, 'shop/cart.html', {"date": date})
    return render(request, 'shop/cart.html')



def cart_add(request):
    rid = request.GET['id']
    num = request.GET['num']
    res = Goods.objects.get(id=rid)
    cart = request.session.get('cart', {})
    key = cart.keys()
    if rid in key:
        num = int(request.session['cart'][rid]["num"]) + int(num)
        date = {rid: {"gname": res.gname, "price": int(res.price), "num": num}}
        request.session['cart'] = date
    else:
        date = cart
        date[str(rid)] = {"gname": res.gname, "price": int(res.price), "num": num}
        request.session['cart'] = date
    print(request.session['cart'])
    response = {"rsp": 1}
    return HttpResponse(json.dumps(response))


def cart_del(request):
    uid = request.GET['id']
    res = request.session.get('cart', None)
    try:
        del request.session['cart'][uid]
        date = request.session['cart']
        request.session['cart'] = date
        res = 0
    except:
        res = 1
    return HttpResponse(res)


def cart_delall(request):
    try:
       # id = request.GET['id']
       # date = request.session['cart']
        return render(request, 'shop/myorder.html')
    except:
        return HttpResponse('<script>alert("清空购物车成功！");location.href="/cart/"</script>')


def cart_editnum(request):
    # 进行商品数量的修改，目的是为了防止用户刷新后数量的还原
    datecart = request.session['cart']
    gid = request.GET['gid']
    num = request.GET['num']
    datecart[gid]['num'] = num
    request.session["cart"] = datecart
    print(datecart)
    return HttpResponse("1")


# 确认订单，需要的参数有，商品id列表，发送的参数有，用户地址和订单商品列表
def myorder(request):
    if request.method == "GET":
        ids = request.GET.get("id", None)
        if ids:
            try:
                k = ids.split(",")
                order = {}
                date = []
                for x in k:
                    order[x] = request.session['cart'][x]
                    good = Goods.objects.get(id=x)
                    good.num = order[x]["num"]
                    del request.session['cart'][x]
                    date.append(good)
                request.session["order"] = order
                print(request.session["order"])
                obj = address.objects.filter(uid=request.session["shoppingUser"]["userid"])
                if len(obj) == 0:
                    response = {"rsp": 2}
                else:
                   # add_info = {"address": obj[0].addres, "name":obj[0].name, "phone": obj[0].phone, "status": obj[0].status}
                   # request.session["shoppingUser"]["add_info"] = add_info
                   # request.session["shoppingUser"].update({"goods": date})
                   response = {"rsp": 1}
                return HttpResponse(json.dumps(response))
            except Exception as e:
                response = {"rsp": 3}
                return HttpResponse(json.dumps(response))
        else:
            o = request.session.get("order", None)
            if o:
                date = request.session.get("order", None)
                obj = address.objects.filter(uid=request.session["shoppingUser"]["id"])
                return render(request, 'shop/myorder.html', {"date": obj, "res": date})
            else:
                return HttpResponse('<script>alert("商品获取失败！");location.href="/cart/"</script>')
    elif request.method == "POST":
        aid = request.POST.get("aid", None)
        if aid:
            uid = request.session["shoppingUser"]["userid"]
            good = request.session["order"]
            sun = 0
            num = 0
            for x in good:
                n = good[x]["num"]
                price = good[x]["price"]
                s = int(n) * int(price)
                sun += s
                num += int(n)
            obj = Order()
            obj.uid = User.objects.get(id=uid)
            obj.aid = address.objects.get(id=aid)
            obj.totalprice = sun
            obj.totalnum = num
            obj.status = 1  # 未付款
            obj.save()
            ob = OrderInfo()
            for x in good:
                ob.orderid = obj
                ob.gid = Goods.objects.get(id=x)
                ob.num = good[x]["num"]
                ob.price = good[x]["price"]
                ob.save()
                o = Goods.objects.get(id=x)
                o.store -= int(good[x]["num"])
                o.num += int(good[x]["num"])
                o.save()
            good = []
            request.session["order"] = good
            return render(request, "shop/buy.html", {"date": obj})
        else:
            return HttpResponse('<script>alert("发生了一个意外！"),location.href=""</script>')


def addres_add(request):
    res = request.GET
    obj = address()
    obj.uid = User.objects.get(user_id=request.session['shoppingUser']['userid'])
    obj.name = res.get("name")
    obj.phone = res.get("phone")
    obj.addres = res.get("addres")
    s = int(res.get("status", 0))
    if s == 1:
        addset = address.objects.filter(status=1)
        for x in addset:
            x.status = 0
            x.save()
        obj.status = 1
    else:
        obj.status = 0
    obj.save()
    return HttpResponse('<script>alert("地址添加成功！");location.href="/myorder/"</script>')


def addres_edit(request):
    if request.method == "GET":
        aid = request.GET["id"]
        date = address.objects.get(id=aid)
        return render(request, "home/addres_edit.html", {"res": date})
    elif request.method == "POST":
        res = request.POST
        obj = address.objects.get(id=res["id"])
        obj.name = res["name"]
        obj.phone = res["phone"]
        obj.addres = res["addres"]
        obj.save()
        return HttpResponse('<script>alert("地址修改成功！");location.href="/addres/list/"</script>')


def myorder_list(request):
    uid = request.session["s"]["id"]
    status = request.GET.get("status", "0")
    if status == "0":
        date = Order.objects.filter(uid=uid)
    else:
        date = Order.objects.filter(uid=uid, status=status)
    print(date)

    return render(request, "home/myorder_list.html", {"date": date})


def myorder_desc(request):
    oid = request.GET.get("oid", None)
    print(oid)
    if oid:
        date = Order.objects.get(id=oid)
        return render(request, "home/myorder_desc.html", {"date": date})
    else:
        return HttpResponse('<script>alert("sorry!您查询的订单不存在！")</script>')


def addres_list(request):
    if request.method == "GET":
        uid = request.session["shoppingUser"]["userid"]
        date = address.objects.filter(uid=uid)
        print(date, "----")
        return render(request, 'shop/addres_list.html', {"date": date})
    elif request.method == "POST":
        aid = request.POST["id"]
        print(aid)
        obj = address.objects.get(id=aid)
        del obj
        print(obj)
        return HttpResponse(1)
