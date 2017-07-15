from django.shortcuts import render
from UHuiWebApp import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib
import time
import random
import json


# Create your views here.


# 普通函数
def encryption(md5):
    key = 'UHuiForCiti'
    m = hashlib.md5()
    m.update(md5.join(key).encode("UTF-8"))
    return m.hexdigest()


def randomID():
    signUpTime = int(time.time())
    for i in range(0, 4):
        append = append + random.random('abcdefghijklmopqrstuvwxyz')
    ID = "%d%s" % (signUpTime, append)
    if models.User.objects.filter(ID=ID).count() != 0:
        return randomID()
    return ID




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
    # 通过@判断用户名为email/手机号
    if "@" in u_name:
        # 查询用户是否存在
        user = models.User.objects.filter(email=u_name)
        if user is None:
            return HttpResponse(u"用户不存在", content_type="text/plain")
        pswObj = models.User.objects.get(email=u_name)
    else:
        user = models.User.objects.filter(phonenum=u_name)
        if user is None:
            return HttpResponse(u"用户不存在", content_type="text/plain")
        pswObj = models.User.objects.get(phonenum=u_name)

    psw = encryption(request.POST.get('password'))
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    if psw == password:
        # 返回cookie，在浏览器关闭前维持登录状态
        response = HttpResponseRedirect("/")
        value = u_name + "_" + encryption(u_name + psw)
        response.set_cookie(key="uhui", value=value, httponly=True)
        return response
    else:
        return HttpResponse(u"密码错误", content_type="text/plain")


def post_signUp(request):
    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    password = encryption(request.POST.get('password'))
    gender = request.POST.get('gender')


    # 查询数据库中昵称是否存在
    if models.User.objects.filter(nickname=nickname):
        return HttpResponse(u"昵称已存在", content_type="text/plain")
    if '@' in username:
        if models.User.objects.filter(email=username).count() != 0:
            return HttpResponse(u"邮箱已被注册", content_type="text/plain")

        # 邮箱验证
        # 将邮箱作为用户名存入数据库中
        models.User.objects.create(ID=randomID(), nickname=nickname, password=password, gender=gender, email=username)
        return HttpResponse(u"请检查验证邮件", content_type="text/plain")
    else:
        if models.User.objects.filter(phonenum=username).count() != 0:
            return HttpResponse(u"手机号已被注册", content_type="text/plain")
        # 短信验证码验证
        pass
        # 将手机号作为用户名存入数据库中
        models.User.objects.create(ID=randomID(), nickname=nickname, password=password, gender=gender,
                                   phoneNum=username)
        return HttpResponse(u"注册成功", content_type="text/plain")
