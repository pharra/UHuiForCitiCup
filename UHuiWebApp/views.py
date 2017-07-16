
from UHuiWebApp import models
from .shortcut import JsonResponse, render
import hashlib
import time
import random
import json

# 初始化render
# render = render()

# Create your views here.


# 普通函数
def encryption(md5):
    key = 'UHuiForCiti'
    m = hashlib.md5()
    m.update(md5.join(key).encode("UTF-8"))
    return m.hexdigest()


# 获取随机ID
def randomID():
    signUpTime = int(time.time())
    append = ''
    for i in range(0, 4):
        append = append + random.choice('abcdefghijklmopqrstuvwxyz')
    ID = "%d%s" % (signUpTime, append)
    if models.User.objects.filter(id=ID).count() != 0:
        return randomID()
    return ID


# 根据request的COOKIES判断登录uid
def get_uid(request):
    cookie_content = request.COOKIES.get('uhui', False)
    print(type(cookie_content))
    if cookie_content:
        content = cookie_content.split('_')
    else:
        return None
    uid = content[0]
    psw = content[1]
    pswObj = models.User.objects.get(id=uid)
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    encrypPsw = encryption(uid + password)
    if psw == encrypPsw:
        return uid
    else:
        return None


# 为用户添加各种表
def createLists(uid):
    pass


# get方法函数
def index(request):

    return render(request, 'index.html', {"a": "a"})


def login(request):
    return render(request, 'login.html')


# post方法加上前缀post_
def post_login(request):
    # cookie_content = request.COOKIES.get('uhui')
    # if cookie_content:
    #     u_name = cookie_content.split("_")[0]
    # uid = get_uid(request)
    u_name = request.POST.get('username')
    # 通过@判断用户名为email/手机号
    if "@" in u_name:
        # 查询用户是否存在
        user = models.User.objects.filter(email=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(email=u_name)
    else:
        user = models.User.objects.filter(phonenum=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(phonenum=u_name)

    psw = encryption(request.POST.get('password'))
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    if psw == password:
        # 返回cookie，在浏览器关闭前维持登录状态
        response = JsonResponse({'error': ''})

        u_id = bytes.decode(pswObj.id.encode("UTF-8"))
        value = u_id + "_" + encryption(u_id + psw)
        response.set_cookie(key="uhui", value=value, httponly=True)
        return response
    else:
        return JsonResponse({'error': '密码错误'})


def post_signUp(request):
    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    password = encryption(request.POST.get('password'))
    gender = request.POST.get('gender')

    if '@' in username:
        if models.User.objects.filter(email=username).count() != 0:
            return JsonResponse({'errno': '1', 'message': '邮箱已被注册'})
        # 查询数据库中昵称是否存在
        if models.User.objects.filter(nickname=nickname):
            return JsonResponse({'errno': '1', 'message': '昵称已存在'})
        # 邮箱验证
        # 将邮箱作为用户名存入数据库中
        uid = randomID()
        models.User.objects.create(id=uid, nickname=nickname, password=password, gender=gender, email=username)
        # 创建列表
        createLists(uid)
        return JsonResponse({'errno': '0', 'message': '请检查验证邮件'})
    else:
        if models.User.objects.filter(phonenum=username).count() != 0:
            return JsonResponse({'errno': '1', 'message': '手机号已被注册'})
        # 查询数据库中昵称是否存在
        if models.User.objects.filter(nickname=nickname):
            return JsonResponse({'errno': '1', 'message': '昵称已存在'})
        # 短信验证码验证
        pass
        # 将手机号作为用户名存入数据库中
        uid = randomID()
        models.User.objects.create(id=uid, nickname=nickname, password=password, gender=gender,
                                   phonenum=username)
        # 创建列表
        createLists(uid)
        return JsonResponse({'errno': '0', 'message': '注册成功'})


def post_userInfo(u_id):
    # 判断是否存在cookie及cookie中信息是否正确
    user = models.User.objects.get(id=u_id)
    lists = models.Couponlist.objects.filter(userid=u_id)
    couponList = []
    for item in lists:
        couponList.append({'type': item.stat, 'listid': item.listid})
    nickname = user.nickname
    gender = user.gender
    # {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList}
    content = [{'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList}]
    content = content[0]
    return content


def post_couponInfo(request):
    pass


