from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class UserLoginMiddleware(MiddlewareMixin):
    # 若请求的是登陆和注册页面 则往下执行
    def process_request(self, request):
        print("middle")
        hlist = ['/myorder/', '/order/', "/personal/", "/myorder/list", "/myorder/desc/",
                 "/addres/list/", "/addres/add/"]
        if request.path in hlist:
            if request.session.get('user', None):
                return HttpResponse('<script>alert("请先登录");location.href="/login/"</script>')
        response = self.res(request)
        return response