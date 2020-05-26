from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import json

class UserLoginMiddleware(MiddlewareMixin):
    # 若请求的是登陆和注册页面 则往下执行
    def process_request(self, request):
        hlist = ['/myorder/', '/order/', '/myorder/list/', '/myorder/desc/', '/addres/list/','/addres/add/']
        if request.path in hlist:
            if request.session.get('shoppingUser') is None:
                return HttpResponse('<script>alert("请先登录");location.href="/login/"</script>')
        elif request.path == '/cart/add/':
            if request.session.get('shoppingUser') is None:
                response = {"rsp": 3}
                return HttpResponse(json.dumps(response))