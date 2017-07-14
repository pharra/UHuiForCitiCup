from django.shortcuts import render
from UHuiWebApp.models import  user
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def signUp(request):
    emailAddress = request.GET['email',0]
    phoneNumber = request.GET['phoneNum',0]
    password = request.GET['password']
    if(emailAddress != 0):
        # 将邮箱作为用户名存入数据库中
        newUser = user()
    elif(phoneNumber!=0):
        # 将手机号作为用户名存入数据库中

