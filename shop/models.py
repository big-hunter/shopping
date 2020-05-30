from django.db import models

'''
用户 tag: 用于 标记用户 购买的一些倾向
    tag：1，3，4 都是商品的具体类型
'''


# 用户表
class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    pic = models.CharField(max_length=100, default='/static/shop/images/header/default.jpg')
    add_time = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)


# 用户行为
class UserAction(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50)
    browsed_good = models.CharField(max_length=300)  # 最近浏览过的商品
    last_time_buy = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    login_out = models.DateTimeField(auto_now_add=True)  # login login_out 时间
    buy_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)


'''

1级 ： 男装 女装 儿童服饰 男包|女包  打牌先看  今日折扣 今日最新
2级 ： 个性潮男 商务绅士 等

'''


# 商品分类模板
class GoodsType(models.Model):
    paren_id = models.IntegerField()  # 上一级分类id
    typename = models.CharField(max_length=20)  # 男装 or 女装
    type_level = models.IntegerField()  # 分类等级
    popular = models.IntegerField()    # 流行程度
    path = models.CharField(max_length=20)
    addtime = models.DateTimeField(auto_now_add=True, null=True)
    nowtime = models.DateTimeField(auto_now=True, null=True)


'''
   
    商品属性tag  用“,” 分割  过滤出  可以用于商品的协同过滤
    tag = "男装,短袖,潮牌"

'''


class Goods(models.Model):
    good_type = models.CharField(max_length=255)
    gname = models.CharField(max_length=255)
    descr = models.TextField()  # 商品的一些描述 或者 设计灵感
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic_path = models.CharField(max_length=100, default='/static/pdf/contract.pdf')  # 商品图片地址
    brand = models.CharField(max_length=60)  # 商品品牌
    state = models.CharField(max_length=60)  # 商品状态
    discount = models.FloatField(default=1)  # 打折 1  0.8 0.7 or 0.6
    color = models.CharField(max_length=30)  # 颜色
    tag = models.TextField(max_length=2000)  # 风格  风格可以有很多
    popular = models.IntegerField(default=0)  # 0 - 100 的流行程度
    store = models.IntegerField()  # 库存数量
    num = models.IntegerField(default=0)  # 购买次数
    addtime = models.DateTimeField(auto_now_add=True)


# 接货地址
class address(models.Model):
    uid = models.ForeignKey(to="User", to_field="user_id", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)
    status = models.IntegerField(default=0)
    addres = models.CharField(max_length=255)
    addtime = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    uid = models.ForeignKey('User', to_field="user_id", on_delete=models.CASCADE)
    aid = models.ForeignKey('address', to_field='id', on_delete=models.CASCADE)
    totalprice = models.FloatField()
    totalnum = models.IntegerField()
    # 1 未付款 2已付款,待发货,3已发货,待收货,4已完成,5已取消
    status = models.IntegerField()
    addtime = models.DateTimeField(auto_now_add=True)


# 订单详情
class OrderInfo(models.Model):
    orderid = models.ForeignKey('Order', to_field="id", on_delete=models.CASCADE)
    gid = models.ForeignKey('goods', to_field="id", on_delete=models.CASCADE)
    num = models.IntegerField()
    price = models.FloatField()
