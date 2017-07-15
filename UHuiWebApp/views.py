from django.shortcuts import render
from UHuiWebApp import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json


# Create your views here.


# 普通函数
def encode(md5):
    key = 'UHuiForCiti'
    m = hashlib.md5()
    m.update(md5.join(key).encode("UTF-8"))
    return m.hexdigest()


# get方法函数
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


# post方法加上前缀post_
def post_login(request):
    # cookie_content = request.COOKIES.get('uhui')
    # if cookie_content:
    #     u_name = cookie_content.split("_")[0]

    u_name = request.POST.get('username')
    if "@" in u_name:
        user = models.User.objects.filter(email=u_name)
        if user is None:
            return None
        pswObj = models.User.objects.get(email=u_name)

    else:
        user = models.User.objects.filter(phonenum=u_name)
        if user is None:
            return None
        pswObj = models.User.objects.get(phonenum=u_name)

    psw = encode(request.POST.get('password'))
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    if psw == password:
        response = HttpResponseRedirect("/")
        value = u_name + "_" + encode(u_name + psw)
        response.set_cookie(key="uhui", value=value, httponly=True)
        return response
    else:
        return None


def post_signUp(request):
    emailAddress = request.POST.get('email', 0)
    _nickname = request.POST.get('nickname', 0)
    phoneNumber = request.POST.get('phoneNum', 0)
    password = request.POST.get('password')

    # 查询数据库中昵称是否存在
    if models.user.objects.filter(nickname=_nickname):
        return
    if emailAddress != 0:
        # 将邮箱作为用户名存入数据库中
        newUser = models.user(email=emailAddress)
    elif phoneNumber != 0:
        # 将手机号作为用户名存入数据库中
        pass
