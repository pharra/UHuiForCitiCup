from django.shortcuts import render
from UHuiWebApp.models import  user
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    print(request.GET.get('method'))
    return render(request, 'login.html')

def signUp(request):
    emailAddress = request.GET['email',0]
    _nickname = request.GET['nickname',0]
    phoneNumber = request.GET['phoneNum',0]
    password = request.GET['password']

    #查询数据库中昵称是否存在
    if(user.objects.filter(nickname= _nickname)):
        pass
    if(emailAddress != 0):
        # 将邮箱作为用户名存入数据库中
        newUser = user(email=emailAddress)
    elif(phoneNumber!=0):
        # 将手机号作为用户名存入数据库中

