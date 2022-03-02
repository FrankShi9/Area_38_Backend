from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import LoginSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


''' Backup code 
class LoginList(LoginRequiredMixin, APIView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def LoginList(self, request, format=None):
        loginKits = User.objects.all()[0:5]  # change table name
        serializer = LoginSerializer(loginKits, many=True)
        return Response(serializer.data)
'''


def login(request):
    if request.method == "GET":
        return render(request, "login.vue")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    if not user_obj:
        return redirect("/login/")  # Url redirect to login again
    else:
        rep = redirect("/index/")  # Url redirect to index after success login
        rep.set_cookie("is_login", True)  # Update cookie
        return rep


def index(request):
    print(request.COOKIES.get('is_login'))
    # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "index.js")


def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep  # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面

def register(request):
    if request.method == "GET":
        return render(request, "register.vue")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    rep = redirect("/index/")  # Url redirect to index after success login
    rep.set_cookie("is_login", True)  # Update cookie
    return rep

# def order(request):
#     print(request.COOKIES.get('is_login'))
#     status = request.COOKIES.get('is_login')
#     if not status:
#         return redirect('/login/')
#     return render(request, "order.html")
