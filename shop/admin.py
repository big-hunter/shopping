from django.contrib import admin
from .models import Goods
from .models import User
from .models import GoodsType
from .models import UserAction
from .models import Order
from .models import OrderInfo


# 用户管理
admin.site.register(User)
# 管理商类型
admin.site.register(GoodsType)
# 商品类型
admin.site.register(Goods)
# 用户行为
admin.site.register(UserAction)
# 用户Order
admin.site.register(Order)
# 订单详情 OrderInfo
admin.site.register(OrderInfo)