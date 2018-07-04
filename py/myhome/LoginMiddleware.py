from django.shortcuts import render
from django.http import HttpResponse
import re

class LoginMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self,request):

        url = request.path
        # 后台中间键验证
        if re.match('/myadmin/',url) and url not in ['/myadmin/user/login/']:
            # 判断是否登录
            if not request.session.get('AdminUser',None):
                # 如果没有登录,则跳转到登录页面
                return HttpResponse('<script>alert("请先登录");location.href="/myadmin/user/login/?next='+url+'"</script>')
            

        # 前台中间键验证
        urllist = ['/ordercheck/','/addressedit/','/addressadd/','/ordercreate/','/buy/','/mycenter/','/myorders/','/fukuan/']
        # 验证路径
        if url in urllist:
            # 验证是否登录
            if not request.session.get("VipUser",None):
                return HttpResponse("<script>alert('请先登录！');location.href='/login/?next="+url+"'</script>")

        response = self.get_response(request)
        return response
