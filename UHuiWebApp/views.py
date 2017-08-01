import json

from django.http import HttpResponseRedirect

from UHuiProject.settings import DEBUG
from django.core.exceptions import ObjectDoesNotExist
from UHuiWebApp import models
from .shortcut import JsonResponse, render

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import hashlib
import time
import random
import datetime

DEFAULT_PIC = 'images/avatar/default.jpg'


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


def emailVerifyCode():
    code = ''
    for i in range(0, 4):
        code = code + random.choice('abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return code


def mobileVerifyCode():
    code = ''
    for i in range(0, 4):
        code = code + random.choice('1234567890')
    return code


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendMail(to_addr, msg):
    # address 为登录判断的一条request
    from_addr = 'No-Reply@uhuiforciti.cn'
    password = 'pj4lkqMF4b'
    smtp_server = 'smtp.ym.163.com'

    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    try:
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        return True
    except smtplib.SMTPException as smtpe:
        print(str(smtpe))
        return False
    finally:
        server.quit()


def sendConfirmMail(to_addr, nickname, uid):
    address = generateAddress(nickname, uid)
    msg = MIMEText('请点击下方链接确认注册\n http://www.uhuiforciti.cn/emailVerification/%s' % address, 'plain', 'utf-8')
    msg['From'] = _format_addr('No-Reply <No-Reply@uhuiforciti.cn>')
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('U惠网注册确认 ', 'utf-8').encode()
    sendMail(to_addr, msg)


def generateAddress(nickname, uid):
    md5 = encryption(nickname)
    extra = '9s0d'
    key = uid + extra
    address = ''
    for (i, k) in zip(md5, key):
        address = address + i + k

    return address


def emailVerification(request):
    path = request.path
    code = path.split('/')[2]
    uid = ''
    for i in range(1, 28, 2):
        uid = uid + code[i]
    try:
        user = models.User.objects.get(id=uid)
    except ObjectDoesNotExist:
        pass
    user.hasconfirm = True
    user.save()
    value = uid + "_" + encryption(uid + user.password)
    response = HttpResponseRedirect('/')
    response.set_cookie(key="uhui", value=value, httponly=True)
    return response


# 定时任务
def timer():
    coupons = models.Coupon.objects.all()
    currentDate = datetime.date.today()
    for coupon in coupons:
        expiredTime = coupon.expiredtime
        lists = models.Listitem.objects.filter(couponid=coupon.couponid)
        listID = lists[0].listid.listid
        userID = models.Couponlist.objects.get(listid=listID).userid.id
        if currentDate >= expiredTime:
            if coupon.stat == 'onSale':
                createMessage('上架的优惠券已过期', coupon.couponid)
            changeCouponStat(coupon.couponid, userID, 'expired')
            createMessage('我的优惠券已过期', coupon.couponid)
        elif (currentDate + datetime.timedelta(days=1)) == expiredTime:
            if coupon.stat == 'onSale':
                createMessage('上架的优惠券即将过期', coupon.couponid)
                createMessage('关注的优惠券即将过期', coupon.couponid)
            changeCouponStat(coupon.couponid, userID, 'expired')
            createMessage('我的优惠券即将过期', coupon.couponid)


# 修改用户信息
def post_modifyUserInfo(request):
    uid = request.uid
    oldPsw = request.POST.get('oldPassword', False)
    newNickName = request.POST.get('nickname', False)
    newPhoneNum = request.POST.get('phoneNum', False)
    newGender = request.POST.get('gender', False)
    newPsw = request.POST.get('password', False)
    newEmail = request.POST.get('email', False)
    user = models.User.objects.get(id=uid)
    response = JsonResponse({})
    if newPsw and oldPsw:
        if encryption(oldPsw) == bytes.decode(user.password.encode("UTF-8")):
            user.password = encryption(newPsw)
        else:
            response.content = json.dumps({'errno': '1', 'message': '旧密码不正确'})

            return response
    elif newPsw and not oldPsw:
        response.content = json.dumps({'errno': '1', 'message': '请输入旧密码'})
        return response

    if newNickName:
        if models.User.objects.filter(nickname=newNickName).exists():
            response.content = json.dumps({'errno': '1', 'message': '昵称已存在'})
            return response
        user.nickname = newNickName

    if newPhoneNum:
        # 需要短信验证码
        if encryption(request.POST['newphone_verification_code']) == request.COOKIES.get('VCm', -1):
            user.phonenum = newPhoneNum
        else:
            response.content = json.dumps({'errno': '1', 'message': '手机验证码不正确'})
            response.delete_cookie('VCm')
            return response

    if newEmail:
        # 向邮箱发送验证码

        if encryption(request.POST['email_verification_code']) == request.COOKIES.get('VCe', -1):
            user.email = newEmail
        else:
            response.content = json.dumps({'errno': '1', 'message': '邮箱验证码不正确'})
            response.delete_cookie('VCe')
            return response

    if newGender:
        user.gender = newGender

    user.save()
    response.content = json.dumps({'errno': '0', 'message': '修改成功'})
    return response


def post_changeAvatar(request):
    uid = request.uid
    user = models.User.objects.get(id=uid)
    list = request.FILES.getlist('file')
    user.avatar = list[0]
    user.save()
    return JsonResponse({'errno': '0', 'message': '成功'})


def changeCouponStat(couponID, sellerID, stat):
    # 只用于上架下架与过期
    try:
        coupon = models.Coupon.objects.get(couponid=couponID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '优惠券不存在'})

    if stat == 'onSale' and coupon.stat != 'store':
        return JsonResponse({'errno': 1, 'message': '上架失败'})
    elif stat == 'store' and coupon.stat != 'onSale':
        return JsonResponse({'errno': 1, 'message': '下架失败'})

    coupon.stat = stat
    coupon.save()
    onSaleList = models.Couponlist.objects.get(stat='onSale', userid=sellerID)
    if stat == 'store' or stat == 'expired':
        if models.Listitem.objects.filter(listid=onSaleList, couponid=coupon).exists():
            models.Listitem.objects.filter(listid=onSaleList, couponid=coupon).delete()
    elif stat == 'onSale':
        models.Listitem.objects.create(listid=onSaleList, couponid=coupon)
        createMessage('关注的优惠券已下架', couponID)
    return JsonResponse({'errno': '0', 'message': '成功'})


# 获取数据
def getListItem(listid):
    lists = models.Couponlist.objects.get(listid=listid)
    listItems = models.Listitem.objects.filter(listid=listid)
    coupon = []
    for item in listItems:
        coupon.append(item.couponid.couponid)
    listInfo = {'listID': listid, 'stat': lists.stat, 'coupons': coupon}
    return listInfo


def post_sendMobileVerifyCode(request):
    verifyCode = mobileVerifyCode()
    print(verifyCode)
    # 调用短信接口

    response = JsonResponse({'send': 'success'})
    response.set_cookie('VCm', encryption(verifyCode))
    return response


def post_sendEmailVerifyCode(request):
    to_addr = request.POST.get('email')
    code = emailVerifyCode()
    msg = MIMEText('您的验证码是：\n %s' % code)
    msg['From'] = _format_addr('No-Reply <No-Reply@uhuiforciti.cn>')
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('U惠网验证码', 'utf-8').encode()
    sendMail(to_addr, msg)
    response = JsonResponse({'send': 'success'})
    response.set_cookie('VCe', encryption(code))
    return response


def post_presearch(request):
    keyword = request.POST.get('keyWord', '不存在的')
    if keyword == '':
        return JsonResponse({'result': []})
    # if not keyword:
    #    return JsonResponse({'error':'keyword not exist'})
    productResult = models.Coupon.objects.filter(product__istartswith=keyword, stat='onSale')
    brandResult = models.Brand.objects.filter(name__istartswith=keyword)
    result = []
    for coupon in productResult:
        if coupon.product not in result:
            result.append(coupon.product)
    result.reverse()
    result = result[0: min(5, len(result))]
    for brand in brandResult.reverse():
        if brand.name not in result:
            result.append(brand.name)
    result = result[0:min(10, len(result))]
            
    return JsonResponse({'result': result})


def post_search(request):
    key = request.POST.get('keyWord', False)

    orderBy = request.POST.get('order', None)
    page = int(request.POST.get('page', 1)) - 1
    if not key:
        return render(request, 'search.html', {'keyWord': key})
    if not orderBy:
        orderBy = 'expiredtime'
    else:
        pass
    result = []
    productResult = models.Coupon.objects.filter(product__icontains=key, stat='onSale').order_by(orderBy)
    brandIDResult = models.Brand.objects.filter(name__icontains=key)
    for i in range(0, 16):
        if (16 * page + i) == productResult.count():
            break
        result.append(couponInfo(productResult[16 * page + i].couponid))
    # 数量不够时的结果仍需补全
    for brand in brandIDResult:
        pc = int(16 / brandIDResult.count())
        brandItem = models.Coupon.objects.filter(brandid=brand.brandid, stat='onSale')
        for i in range(0, pc):
            if (pc * page + i) == brandItem.count():
                break
            result.append(couponInfo(brandItem[pc * page + i].couponid))

    # if not productResult.exists() and not brandIDResult.exists():
    #     return render(request, 'search.html')
    return render(request, 'search.html', {'coupons': result, 'keyWord': key})


def post_getUserCoupon(request):
    count = request.POST.get('couponsNumbers', '10')
    if count != 'all':
        count = int(count)
    if not request.uid:
        return {'couponsOwn': '', 'couponsLike': ''}
    try:
        ownList = models.Couponlist.objects.get(userid=request.uid, stat='own')
        likeList = models.Couponlist.objects.get(userid=request.uid, stat='like')
        onSaleList = models.Couponlist.objects.get(userid=request.uid, stat='onSale')
    except ObjectDoesNotExist:
        print('DoesNotExist')
        return {'couponsOwn': '', 'couponsLike': ''}
    ownCoupons = models.Listitem.objects.filter(listid=ownList.listid)
    likeCoupons = models.Listitem.objects.filter(listid=likeList.listid)
    onSaleCoupons = models.Listitem.objects.filter(listid=onSaleList.listid)
    messages = post_getMessage(request)
    own = []
    like = []
    onSale = []
    if ownCoupons.exists():
        if (count != 'all' and ownCoupons.count() <= count) or count == 'all':
            for coupon in ownCoupons:
                own.append(couponInfo(coupon.couponid.couponid))
        else:
            for i in range(0, count):
                own.append(couponInfo(ownCoupons[i].couponid.couponid))

    if likeCoupons.exists():
        if (count != 'all' and likeCoupons.count() <= count) or count == 'all':
            for coupon in likeCoupons:
                like.append(couponInfo(coupon.couponid.couponid))
        else:
            for i in range(0, count):
                onSale.append(couponInfo(likeCoupons[i].couponid.couponid))

    if onSaleCoupons.exists():
        if (count != 'all' and onSaleCoupons.count() <= count) or count == 'all':
            for coupon in onSaleCoupons:
                onSale.append(couponInfo(coupon.couponid.couponid))
        else:
            for i in range(0, count):
                onSale.append(couponInfo(onSaleCoupons[i].couponid.couponid))

    own.reverse()
    like.reverse()
    onSale.reverse()

    couponDict = {'couponsOwn': own, 'couponsLike': like, 'couponsOnSale': onSale,
                  'couponMessages': messages['couponMessages'], 'systemMessages': messages['systemMessages']}

    return couponDict


def post_getMobileUserCoupon(request):
    uid = request.uid
    ownList = models.Couponlist.objects.get(userid=uid, stat='own')
    objects = models.Listitem.objects.filter(listid=ownList.listid)
    objects.reverse()
    couponsStore = []
    couponsOnSale = []
    couponsExpired = []
    for id in objects:
        info = couponInfo(id.couponid.couponid)
        if info['stat'] == 'store':
            couponsStore.append(info)
        elif info['stat'] == 'onSale':
            couponsOnSale.append(info)
        elif info['stat'] == 'expired':
            info['expiredReason'] = '于' + info['expiredTime'] + '过期'
            couponsExpired.append(info)
        elif info['stat'] == 'used':
            info['expiredReason'] = '已使用'
            couponsExpired.append(info)

    return {'couponsStore': couponsStore, 'couponsOnSale': couponsOnSale,
            'couponsExpired': couponsExpired}


def post_getBoughtCouponsMobile(request):
    uid = request.uid
    listID = models.Couponlist.objects.get(stat='bought', userid=uid)
    couponIDs = models.Listitem.objects.filter(listid=listID.listid)
    used = []
    own = []
    for couponid in couponIDs:
        if couponid.couponid.stat == 'used':
            used.append(couponInfo(couponid.couponid.couponid))
        elif couponid.couponid.stat == 'store':
            own.append(couponInfo(couponid.couponid.couponid))
    return {'own': own, 'used': used}


def post_getCouponByCat(request):
    catName = request.POST['catName']
    page = int(request.POST['page']) - 1
    try:
        catid = models.Category.objects.get(name=catName)
    except ObjectDoesNotExist:
        return JsonResponse({'error': '类别不存在'})
    coupons = models.Coupon.objects.filter(catid=catid, stat='onSale')

    result = []
    for i in range(32 * page, min(32 * (page + 1), coupons.count())):
        result.append(couponInfo(coupons[i].couponid))
    response = JsonResponse({'coupons': result})
    return response


def post_getCouponByCatIndex(request):
    category = models.Category.objects.all()
    couponByCat = {}
    for cat in category:
        coupons = models.Coupon.objects.filter(catid=cat.catid, stat='onSale')
        coupons.reverse()
        couponByCat[cat.name] = []
        for i in range(0, min(8, coupons.count())):
            couponByCat[cat.name].append(couponInfo(coupons[i].couponid))
    # values = coupons.values()
    # values.reverse()
    # couponByCat[cat.name] = values[0:8]
    result = {'coupons': couponByCat}
    return result


def post_getCouponForMobileIndex(request):
    index = int(request.COOKIES.get('indexM', '0'))
    couponsAll = models.Coupon.objects.filter(stat='onSale')
    couponsAll.reverse()
    resultSet = []
    for i in range(index, min(couponsAll.count(), index + 10)):
        resultSet.append(couponInfo(couponsAll[i].couponid))

    result = {'coupons': resultSet}
    # result = json.dumps(result)
    response = JsonResponse(result)
    response.set_cookie('indexM', index + 10)
    return response


def post_couponDetail(request):
    uid = request.uid
    couponID = request.GET.get('couponID')
    if uid is None:
        like = False
    else:
        likeList = models.Couponlist.objects.get(userid=uid, stat='like')
        like = models.Listitem.objects.filter(listid=likeList.listid, couponid=couponID).exists()

    if like:
        like = '1'
    else:
        like = '0'
    info = couponInfo(couponID)
    sellerInfo = info['sellerInfo']
    if sellerInfo['userid'] == uid:
        isOwner = '1'
    else:
        isOwner = '0'
    return {'info': info, 'like': like, 'isOwner': isOwner}


def couponInfo(couponID):
    try:
        coupon = models.Coupon.objects.get(couponid=couponID)
    except ObjectDoesNotExist:
        return {'error': '找不到此优惠券信息'}
    limits = models.Limit.objects.filter(couponid=couponID)
    lists = models.Listitem.objects.filter(couponid=couponID)
    sellerInfo = {}
    for listItem in lists:
        listID = listItem.listid.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            sellerInfo = post_userInfo(listStat.userid.id)
    couponInfo = {}
    couponInfo['couponID'] = coupon.couponid
    couponInfo['brand'] = coupon.brandid.name
    couponInfo['cat'] = coupon.catid.name
    couponInfo['listPrice'] = str(coupon.listprice)
    couponInfo['value'] = str(coupon.value)
    couponInfo['product'] = coupon.product
    couponInfo['discount'] = coupon.discount
    couponInfo['stat'] = coupon.stat
    couponInfo['pic'] = '/static/' + str(coupon.pic)
    couponInfo['expiredTime'] = coupon.expiredtime.strftime("%Y-%m-%d")
    limitList = []
    if limits.exists():
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
    avatar = '/static/' + str(user.avatar)
    phoneNum = user.phonenum
    if phoneNum is None:
        phoneNum = '未绑定手机号'
    else:
        phoneNum = phoneNum[0:3] + '****' + phoneNum[7:]
    email = user.email
    if email is None:
        email = '未绑定邮箱'

    # {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList}
    content = {'userid': u_id, 'nickname': nickname, 'gender': gender, 'lists': couponList, 'UCoin': UCoin,
               'avatar': avatar, 'phoneNum': phoneNum, 'email': email}
    return content


def getCatName(cid):
    try:
        cat = models.Category.objects.get(catid=cid)
    except ObjectDoesNotExist:
        return 'category does not exist'
    return cat.name


def getBrandInfo(bid):
    try:
        brand = models.Brand.objects.get(brandid=bid)
    except ObjectDoesNotExist:
        return {'brand': 'no brand info'}
    info = {'name': brand.name, 'address': brand.address}
    return info


def post_getMessage(request):
    uid = request.uid
    messages = models.Message.objects.filter(userid=uid).order_by('time')
    info = post_userInfo(uid)
    content = []
    systemMsg = []
    for item in messages:
        message = {'messageID': item.messageid, 'time': item.time, 'messageCat': item.messagecat,
                   'hasRead': item.hasread, 'content': item.content}
        if item.messagecat == '系统通知':
            systemMsg.append(message)
        else:
            content.append(message)
    content.reverse()
    systemMsg.reverse()
    info['couponMessages'] = content
    info['systemMessages'] = systemMsg
    return info


def readMessage(request):
    uid = request.uid
    messageID = request.POST['messageID']
    try:
        message = models.Message.objects.get(messageid=messageID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '消息不存在'})

    message.hasread = True
    message.save()
    return JsonResponse({'errno': '0', 'message': '成功'})


# 存储数据
def post_storeCoupon(request):
    # 缺了limits
    uid = request.uid
    brand = request.POST['brand']
    cat = request.POST['category']
    expiredTime = datetime.datetime.strptime(request.POST['expired time'], '%Y-%m-%d')
    listPrice = request.POST['listPrice']
    value = calculateValue()
    product = request.POST['product']
    discount = request.POST['discount']
    stat = request.POST.get('stat', 'store')
    pic = request.FILES.get('pic')

    # 判断brand是否存在
    if not models.Brand.objects.filter(name=brand).exists():
        brandID = models.Brand(brandid=None, name=brand)
    else:
        brandID = models.Brand.objects.get(name=brand)

    # 获取catID
    if not models.Category.objects.filter(name=cat).exists():
        return JsonResponse({'errno': 1, 'message': 'category not found'})
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
    return JsonResponse({'errno': 0, 'message': 'store success'})


def post_buy(request):
    couponID = request.POST['couponID']
    sellerID = request.POST['sellerID']
    buyerID = request.uid
    # 检查优惠券是否存在
    try:
        coupon = models.Coupon.objects.get(couponid=couponID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '优惠券不存在'})
    if coupon.stat != 'onSale':
        return JsonResponse({'errno': '1', 'message': '优惠券已下架'})
    # 检查卖家UCoin是否足够
    buyer = models.User.objects.get(id=buyerID)
    if buyer.ucoin < coupon.listprice:
        return JsonResponse({'errno': '1', 'message': 'UCoin不足以支付'})
    buyer.ucoin = buyer.ucoin - coupon.listprice
    # 优惠券状态由onSale修改为store
    createMessage('上架的优惠券被购买', couponID)
    coupon.stat = 'store'
    buyer.save()
    coupon.save()
    # 优惠券由卖家的own列表移除
    sellerOwnList = models.Couponlist.objects.get(stat='own', userid=sellerID)
    models.Listitem.objects.get(listid=sellerOwnList.listid, couponid=couponID).delete()
    # # 优惠券由卖家的onSale列表移除
    # onSaleList = models.Couponlist.objects.get(stat='onSale', userid=sellerID)
    # models.Listitem.objects.get(listid=onSaleList.listid, couponid=couponID).delete()
    # 优惠券存入卖家的sold列表
    soldList = models.Couponlist.objects.get(stat='sold', userid=sellerID)
    models.Listitem.objects.create(listid=soldList, couponid=coupon)
    # 优惠券存入买家的bought列表
    boughtList = models.Couponlist.objects.get(stat='bought', userid=buyerID)
    models.Listitem.objects.create(listid=boughtList, couponid=coupon)
    # 优惠券存入买家的own列表
    ownList = models.Couponlist.objects.get(stat='own', userid=buyerID)
    models.Listitem.objects.create(listid=ownList, couponid=coupon)
    # 去掉所有like
    createMessage('关注的优惠券已被购买', couponID)
    likeList = models.Listitem.objects.filter(couponid=couponID)
    for lists in likeList:
        temp = models.Couponlist.objects.get(listid=lists.listid.listid)
        if temp.stat == 'like':
            lists.delete()
    return JsonResponse({'errno': '0', 'message': '购买成功'})


def post_putOnSale(request):
    couponID = request.POST['couponID']
    sellerID = request.uid
    return changeCouponStat(couponID, sellerID, 'onSale')


def post_putOffSale(request):
    couponID = request.POST['couponID']
    sellerID = request.uid
    return changeCouponStat(couponID, sellerID, 'own')


def post_like(request):
    # 优惠券加入like列表
    couponID = request.POST['couponID']
    sellerID = request.uid
    try:
        coupon = models.Coupon.objects.get(couponid=couponID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '优惠券不存在', 'like': '0'})
    likeList = models.Couponlist.objects.get(stat='like', userid=sellerID)
    if models.Listitem.objects.filter(listid=likeList.listid, couponid=couponID).exists():
        return JsonResponse({'errno': '1', 'message': '该优惠券已被关注', 'like': '1'})
    models.Listitem.objects.create(listid=likeList, couponid=coupon)
    return JsonResponse({'errno': '0', 'message': '关注成功', 'like': '1'})


def post_dislike(request):
    # 优惠券加入like列表
    couponID = request.POST['couponID']
    sellerID = request.uid
    likeList = models.Couponlist.objects.get(stat='like', userid=sellerID)
    if models.Listitem.objects.filter(listid=likeList.listid, couponid=couponID).exists():
        models.Listitem.objects.get(listid=likeList.listid, couponid=couponID).delete()
        return JsonResponse({'errno': '0', 'message': '取消关注成功', 'like': '0'})
    else:
        return JsonResponse({'errno': '1', 'message': '此优惠券不在关注列表中', 'like': '0'})


def post_buyCredit(request):
    uid = request.uid
    amount = request.POST['amount']
    if request.POST['pay'] == 'failed':
        return JsonResponse({'errno': 1, 'message': '支付失败'})
    user = models.User.objects.get(id=uid)
    user.ucoin = user.ucoin + amount
    user.save()
    return JsonResponse({'errno': 0, 'message': '充值成功'})


# 添加商家。后台接口，前端不连接
def post_storeBrand(request):
    pass


# 添加商家。后台接口，前端不连接
def post_storeCat(request):
    pass


# 创建message
def createMessage(messageType, couponID, content=None):
    messageID = randomID()
    # 为该优惠券所有符合messageType的用户添加messageType的消息
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
    if not userlist:
        return {'errno': 0, 'message': '目标用户不存在'}
    for user in userlist:
        models.Message.objects.create(messageID=randomID(), userid=user, content=content,
                                      time=time.strftime("%Y-%m-%d", time.localtime()), messageCat=messageType,
                                      couponid=couponID, hasread=False, hassend=False)
    return {'errno': '0', 'message': '成功'}


# 为用户添加各种表
def createLists(user):
    # models.User.objects.create
    stat = ['own', 'sold', 'bought', 'onSale', 'like']
    for content in stat:
        models.Couponlist.objects.create(userid=user, stat=content, listid=None)


# get方法函数
def index(request):
    return render(request, 'index.html', post_getCouponByCatIndex(request))


def login(request):
    return render(request, 'login.html')


def userPage(request):
    return render(request, 'user.html', post_getUserCoupon(request))


def myCouponsPage(request):
    return render(request, 'mobile_mycoupons.html', post_getMobileUserCoupon(request))


def search(request):
    return render(request, 'search.html')


def commodity(request):
    detail = post_couponDetail(request)
    if detail['isOwner'] == '1':
        return render(request, 'mycoupons_for_sell.html', detail)
    return render(request, 'commodity.html', detail)


def mobile_appraisement(request):
    return render(request, 'mobile_appraisement.html')


def mobile_user_setting(request):
    return render(request, 'mobile_user_setting.html')


def mobile_user_wallet(request):
    return render(request, 'mobile_user_wallet.html')


def mobile_couponsmessage(request):
    return render(request, 'mobile_couponsmessage.html')


def mobile_user_focus(request):
    return render(request, 'mobile_user_focus.html')


def mobile_sell_final(request):
    return render(request, 'mobile_sell_final.html', post_couponDetail(request))


def mobile_couponsmessage(request):
    return render(request, 'mobile_couponsmessage.html')


def mobile_myboughtcoupons(request):
    return render(request, 'mobile_myboughtcoupons.html', post_getBoughtCouponsMobile(request))


# post方法加上前缀post_
def post_login(request):
    # cookie_content = request.COOKIES.get('uhui')
    # if cookie_content:
    #     u_name = cookie_content.split("_")[0]
    # uid = request.uid
    u_name = request.POST.get('username')
    # 通过@判断用户名为email/手机号
    if "@" in u_name:
        # 查询用户是否存在
        user = models.User.objects.filter(email=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(email=u_name)
        if pswObj.hasconfirm is False:
            return JsonResponse({'error': '请到邮箱验证您的账号'})
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
        # 将邮箱作为用户名存入数据库中
        uid = randomID()
        # 邮箱验证
        sendConfirmMail(username, nickname, uid)

        user = models.User(id=uid, nickname=nickname, password=password, gender=gender, email=username, ucoin=0,
                           hasconfirm=False, avatar=DEFAULT_PIC)

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
                           phonenum=username, ucoin=0, hasconfirm=True, avatar=DEFAULT_PIC)
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
        return False
