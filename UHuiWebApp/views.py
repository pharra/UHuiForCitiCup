from UHuiProject.settings import DEBUG
from UHuiWebApp import models
from .shortcut import JsonResponse, render
import hashlib
import time
import random
import json


DEFAULT_PIC = '/'

# 初始化render
# render = render()

# Create your views here.
def calculateValue():
    pass


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


# 获取数据
def getListItem(listid):
    lists = models.Couponlist.objects.get(listid=listid)
    listItems = models.Listitem.objects.filter(listid=listid)
    coupon = []
    for item in listItems:
        coupon.append(item.couponid)
    listInfo = {'listID': listid, 'stat': lists.stat, 'coupons': coupon}
    return listInfo


def post_couponInfo(couponID):
    coupon = models.Coupon.objects.get(couponid=couponID)
    limits = models.Limit.objects.filter(couponID=couponID)
    lists = models.Listitem.objects.filter(couponid=couponID)
    sellerInfo = {}
    for listItem in lists:
        listID = listItem.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            sellerInfo = post_userInfo(listStat.userid)
    couponInfo = {}
    couponInfo['couponID'] = coupon.couponid
    couponInfo['brand'] = getBrand(coupon.brandid)
    couponInfo['cat'] = getCat(coupon.catid)
    couponInfo['listPrice'] = coupon.listprice
    couponInfo['value'] = coupon.value
    couponInfo['product'] = coupon.product
    couponInfo['discount'] = coupon.discount
    couponInfo['stat'] = coupon.stat
    couponInfo['pic'] = coupon.pic
    limitList = []
    for content in limits:
        limitList.append(content.content)
    couponInfo['limits'] = limitList
    couponInfo['sellerInfo'] = sellerInfo
    return couponInfo


def post_userInfo(u_id):
    user = models.User.objects.get(id=u_id)
    lists = models.Couponlist.objects.filter(userid=u_id)
    couponList = []
    for item in lists:
        couponList.append({'type': item.stat, 'listid': item.listid})
    nickname = user.nickname
    gender = user.gender
    # {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList}
    content = {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList}
    return content


def getCat(cid):
    cat = models.Category.objects.get(catid=cid)
    return cat.name


def getBrand(bid):
    brand = models.Brand.objects.get(brandid=bid)
    info = {}
    info['name'] = brand.name
    info['address'] = brand.address
    return info


def getMessage(uid):
    messages = models.Message.objects.filter(userid=uid).order_by('time')
    info = post_userInfo(uid)
    content = []
    for item in messages:
        message = {'messageID': item.messageid, 'time': item.time, 'messageCat': item.messagecat,
                   'hasRead': item.hasread, 'content': item.content}
        content.append(message)
    info['messages'] = content
    return info


# 存储数据
def post_storeCoupon(request):
    uid = request.POST['userID']
    brand = request.POST['brand']
    cat = request.POST['category']
    listPrice = request.POST['listPrice']
    value = calculateValue()
    product = request.POST['product']
    discount = request.POST['discount']
    stat =  request.POST['stat']
    pic = request.POST.get('pic', DEFAULT_PIC)
    # 判断brand是否存在

    if models.Brand.objects.filter(name=brand).count() == 0:
        brandID = models.Brand(brandid=None, name=brand)
    else:
        brandID = models.Brand.objects.get(name=brand).brandid

    # 获取catID
    # if models.Category.objects.filter()


    pass


def post_storeBrand(request):
    pass


def post_storeCat(request):
    pass


def post_storeMessage():
    pass


# 为用户添加各种表
def createLists(user):
    # models.User.objects.create

    stat = ['own', 'sold', 'brought', 'onSale', 'like']

    for content in stat:
        models.Couponlist.objects.create(userid=user, stat=content, listid=None)


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

    if DEBUG is True:
        print(username + nickname + gender)


    if '@' in username:
        if models.User.objects.filter(email=username).count() != 0:
            return JsonResponse({'errno': '1', 'message': '邮箱已被注册'})
        # 查询数据库中昵称是否存在
        if models.User.objects.filter(nickname=nickname):
            return JsonResponse({'errno': '1', 'message': '昵称已存在'})
        # 邮箱验证
        # 将邮箱作为用户名存入数据库中
        uid = randomID()
        user = models.User(id=uid, nickname=nickname, password=password, gender=gender, email=username)
        # 创建列表
        user.save()
        createLists(user)

        return JsonResponse({'errno': '2', 'message': '请检查验证邮件'})

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
        user = models.User(id=uid, nickname=nickname, password=password, gender=gender,

                           phonenum=username)
        user.save()
        # 创建列表

        createLists(user)
        return JsonResponse({'errno': '0', 'message': '注册成功'})


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
