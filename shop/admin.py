from django.contrib import admin
from .models import Goods
from .models import User
from .models import GoodsType
from .models import UserAction


# 用户管理
admin.site.register(User)
# 管理商类型
admin.site.register(GoodsType)
# 商品类型
admin.site.register(Goods)
# 用户行为
admin.site.register(UserAction)