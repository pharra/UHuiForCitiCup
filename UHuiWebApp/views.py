from django.shortcuts import render
from UHuiWebApp import models
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import hashlib
import json


def index(request):
    return render(request, 'index.html')


def login(request):
    u_name = request.POST.get('username')
    if models.user.objects.filter(username=u_name).count()==0:
        return
    psw = encode(request.POST.get('password'))
    pswObj = models.user.objects.get(username=u_name)
    password = pswObj.password.encode('UTF-8')
    if psw == password:
        return
    else:
        return


def signUp(request):
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


def encode(md5):
    key = 'UHuiForCiti'
    m = hashlib.md5()
    m.update(md5.join(key))
    return m.hexdigest()
