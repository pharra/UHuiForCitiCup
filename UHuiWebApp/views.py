from UHuiProject.settings import DEBUG
from django.core.exceptions import ObjectDoesNotExist
from UHuiWebApp import models
from .shortcut import JsonResponse, render
import hashlib
import time
import random
import datetime

DEFAULT_PIC = '/pic/pic1.jpg'


# 初始化render
# render = render()

# Create your views here.
# 估值算法
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
    if models.User.objects.filter(id=ID).exists():
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
def post_getCouponByCat(request):
    catid = request.POST['catID']
    cookie_content = request.COOKIES.get('page', False)
    coupons = models.Coupon.objects.filter(catid=catid, stat='onSale')
    if not cookie_content:
        page = 0
    else:
        page = cookie_content
    result = []
    for i in range(0,9):
        result.append(coupons[9*page+i])
    resultSet = {}
    for coupon in result:
        resultSet[coupon.couponid] = post_couponInfo(coupon.couponid)
    response = JsonResponse(resultSet)
    response.set_cookie('page', page+1)
    return response
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
    couponInfo['brand'] = getBrandInfo(coupon.brandid)
    couponInfo['cat'] = getCatName(coupon.catid)
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
    UCoin = user.ucoin
    avatar = user.avatar
    # {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList}
    content = {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList, 'UCoin': UCoin, 'avatar': avatar}
    return content
def getCatName(cid):
    try:
        cat = models.Category.objects.get(catid=cid)
    except ObjectDoesNotExist:
        return 'cat does not exist'
    return cat.name
def getBrandInfo(bid):
    try:
        brand = models.Brand.objects.get(brandid=bid)
    except ObjectDoesNotExist:
        return {'brand': 'no brand info'}
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
    expiredTime = datetime.datetime.strptime(request.POST['expired time'], '%Y-%m-%d')
    listPrice = request.POST['listPrice']
    value = calculateValue()
    product = request.POST['product']
    discount = request.POST['discount']
    stat = request.POST.get('stat', 'store')
    pic = request.POST.get('pic', DEFAULT_PIC)

    # 判断brand是否存在
    if not models.Brand.objects.filter(name=brand).exists():
        brandID = models.Brand(brandid=None, name=brand)
    else:
        brandID = models.Brand.objects.get(name=brand)

    # 获取catID
    if not models.Category.objects.filter(name=cat).exists():
        return {'errno': 1, 'message': 'category not found'}
    else:
        catID = models.Category.objects.get(name=cat)

    user = models.User.objects.get(id=uid)
    couponID = randomID()
    coupon = models.Coupon(couponid=couponID, brandid=brandID, catid=catID, listPrice=listPrice,
                           value=value, product=product, discount=discount, stat=stat, pic=pic,
                           expiredTime=expiredTime)
    coupon.save()
    if stat == 'onSale':
        list = models.Couponlist.objects.get(stat='onSale', userid=user.id)
    else:
        list = models.Couponlist.objects.get(stat='own', userid=user.id)

    models.Listitem.objects.create(listid=list, couponid=coupon)
    return {'errno': 0, 'message': 'store success'}
def post_buy(request):
    couponID = request.POST['couponID']
    sellerID = request.POST['sellerID']
    buyerID = get_uid(request)
    # 检查优惠券是否存在
    coupon = models.Coupon.objects.get(couponid=couponID)
    if coupon.stat != 'onSale':
        return {'errno': 1, 'message': '优惠券已下架'}
    # 检查卖家UCoin是否足够
    buyerUCoin = models.User.objects.get(id=buyerID).ucoin
    if buyerUCoin < coupon.listprice:
        return {'errno': 1, 'message': 'UCoin不足以支付'}
    # 优惠券状态由onSale修改为store
    coupon.stat = 'store'
    coupon.save()
    # 优惠券由卖家的own列表移除
    sellerOwnList = models.Couponlist.objects.get(stat='own', userid=sellerID)
    models.Listitem.objects.get(listid=sellerOwnList.listid, couponid=couponID).delete()
    # 优惠券由卖家的onSale列表移除
    onSaleList = models.Couponlist.objects.get(stat='onSale', userid=sellerID)
    models.Listitem.objects.get(listid=onSaleList.listid, couponid=couponID).delete()
    # 优惠券存入卖家的sold列表
    soldList = models.Couponlist.objects.get(stat='sold', userid=sellerID)
    models.Listitem.objects.create(listid=soldList, couponid=coupon)
    # 优惠券存入买家的brought列表
    broughtList = models.Couponlist.objects.get(stat='brought', userid=buyerID)
    models.Listitem.objects.create(listid=broughtList, couponID=coupon)
    # 优惠券存入买家的own列表
    ownList = models.Couponlist.objects.get(stat='own', userid=buyerID)
    models.Listitem.objects.create(listid=ownList, couponID=coupon)
    return {'errno': 0, 'message': 'successfully brought'}
def post_putOnSale(request):
    # 优惠券加入卖家的onSale列表
    couponID = request.POST['couponID']
    sellerID = get_uid(request)
    coupon = models.Coupon.objects.get(couponid=couponID)
    if coupon.stat != 'store':
        return {'errno': 1, 'message': '上架失败'}
    onSaleList = models.Couponlist.objects.get(stat='onSale', userid=sellerID)
    models.Listitem.objects.create(listid=onSaleList, couponid=coupon)
    return {'errno': '0', 'message': '上架成功'}
def post_like(request):
    # 优惠券加入like列表
    couponID = request.POST['couponID']
    sellerID = get_uid(request)
    coupon = models.Coupon.objects.get(couponid=couponID)
    likeList = models.Couponlist.objects.get(stat='like', userid=sellerID)
    if models.Listitem.objects.filter(listid=likeList.listid, couponid=couponID).exists():
        return {'errno': 1, 'message': '该优惠券已被关注'}
    models.Listitem.objects.create(listid=likeList, couponid=coupon)
    return {'errno': '0', 'message': '关注成功'}
def post_buyCredit(request):
    uid = get_uid(request)
    amount = request.POST['amount']
    if request.POST['pay'] == 'failed':
        return {'errno': 1, 'message': '支付失败'}
    user = models.User.objects.get(id=uid)
    user.ucoin = user.ucoin + amount
    user.save()
    return {'errno': 0, 'message': '充值成功'}
# 添加商家。后台接口，前端不连接
def post_storeBrand(request):
    pass
# 添加商家。后台接口，前端不连接
def post_storeCat(request):
    pass
# 创建message
def post_createMessage(messageType, couponID, content=None):

    messageID = randomID()

    # 找owner
    lists = models.Listitem.objects.filter(couponid=couponID)
    # 根据messageType的不同寻找不同的接收USER，并填入相应的content
    #               0                    1                   2                3                 4
    types = ['上架的优惠券被购买', '上架的优惠券即将过期', '上架的优惠券已过期', '关注的优惠券即将过期', '关注的优惠券已被购买',
             '我的优惠券即将过期', '我的优惠券已过期', '系统通知']
    #               5                   6           7
    if messageType not in lists:
        return {'errno': '1', 'message': '消息类型不存在'}
    userlist = []
    if messageType == types[3] or messageType == types[4]:
        # like列表

        for listItem in lists:
            if models.Couponlist.objects.filter(stat='like', listid=listItem.listid).exists():
                userlist.append(models.Couponlist.objects.get(stat='like', listid=listItem.listid))

        pass
    else:
        # own列表
        for listItem in lists:
            if models.Couponlist.objects.filter(stat='own', listid=listItem.listid).exists():
                userlist.append(models.Couponlist.objects.get(stat='own', listid=listItem.listid))
    if content is None:
        content = messageType
    for user in userlist:
        models.Message.objects.create(messageID=randomID(), userid=user, content=content,
                                      time=time.strftime("%Y-%m-%d", time.localtime()), messageCat=messageType,
                                      couponid=couponID, hasread=False, hassend=False)
    return {'errno': '0', 'message': '成功'}
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
def userPage(request):
    return render(request, 'user.html')
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
    if username == '':
        return JsonResponse({'errno': '1', 'message': '手机号或邮箱不能为空'})
    nickname = request.POST.get('nickname')
    password = encryption(request.POST.get('password'))
    gender = request.POST.get('gender')

    if DEBUG is True:
        print(username + nickname + gender)

    if '@' in username:
        if models.User.objects.filter(email=username).exists():
            return JsonResponse({'errno': '1', 'message': '邮箱已被注册'})
        # 查询数据库中昵称是否存在
        if models.User.objects.filter(nickname=nickname):
            return JsonResponse({'errno': '1', 'message': '昵称已存在'})
        # 邮箱验证
        # 将邮箱作为用户名存入数据库中
        uid = randomID()

        user = models.User(id=uid, nickname=nickname, password=password, gender=gender, email=username, ucoin=0)

        # 创建列表
        user.save()
        createLists(user)

        return JsonResponse({'errno': '2', 'message': '请检查验证邮件'})

    else:
        if models.User.objects.filter(phonenum=username).exists():
            return JsonResponse({'errno': '1', 'message': '手机号已被注册'})
        # 查询数据库中昵称是否存在
        if models.User.objects.filter(nickname=nickname):
            return JsonResponse({'errno': '1', 'message': '昵称已存在'})
        # 短信验证码验证
        pass
        # 将手机号作为用户名存入数据库中
        uid = randomID()
        user = models.User(id=uid, nickname=nickname, password=password, gender=gender,

                           phonenum=username, ucoin=0)
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
    if not models.User.objects.filter(id=uid).exists():
        return None
    pswObj = models.User.objects.get(id=uid)
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    encrypPsw = encryption(uid + password)
    if psw == encrypPsw:
        return uid
    else:
        return None
