import json
from decimal import Decimal

from django.db.models import Q
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


# 去除尾数
def removeTailZero(listprice):
    if '.' not in listprice:
        return listprice
    return listprice.rstrip('0').rstrip('.')


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
        if coupon.used is True or (coupon.store is False and coupon.onsale is False) or coupon.expired is True:
            continue
        expiredTime = coupon.expiredtime
        userID = coupon.userid.id
        if currentDate >= expiredTime:
            if coupon.onsale is True:
                createMessage('上架的优惠券已过期', coupon.couponid)
            changeCouponStat(coupon.couponid, userID, 'expired')
            createMessage('我的优惠券已过期', coupon.couponid)
        elif (currentDate + datetime.timedelta(days=1)) == expiredTime:
            if coupon.onsale is True:
                createMessage('上架的优惠券即将过期', coupon.couponid)
                createMessage('关注的优惠券即将过期', coupon.couponid)
            changeCouponStat(coupon.couponid, userID, 'expired')
            createMessage('我的优惠券即将过期', coupon.couponid)


def addSearchHistory(key, history):
    historyList = history.split('__')
    if len(historyList) == 10:
        historyList.pop()
    newHistory = key
    for value in historyList:
        newHistory = '%s__%s' % (newHistory, value)

    return newHistory


# 修改用户信息
def post_modifyUserInfo(request):
    uid = request.uid
    hasChange = False
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
            hasChange = True
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
        hasChange = True

    if newPhoneNum:
        # 需要短信验证码
        if encryption(request.POST['newphone_verification_code']) == request.COOKIES.get('VCm', -1):
            user.phonenum = newPhoneNum
            hasChange = True
        else:
            response.content = json.dumps({'errno': '1', 'message': '手机验证码不正确'})
            response.delete_cookie('VCm')
            return response

    if newEmail:
        # 向邮箱发送验证码

        if encryption(request.POST['email_verification_code']) == request.COOKIES.get('VCe', -1):
            user.email = newEmail
            hasChange = True
        else:
            response.content = json.dumps({'errno': '1', 'message': '邮箱验证码不正确'})
            response.delete_cookie('VCe')
            return response

    if newGender:
        user.gender = newGender
        hasChange = True

    user.save()
    if not hasChange:
        response.content = json.dumps({'errno': '1', 'message': '请输入新数据'})
    else:
        response.content = json.dumps({'errno': '0', 'message': '修改成功'})
    return response


def post_changeAvatar(request):
    uid = request.uid
    user = models.User.objects.get(id=uid)
    list = request.FILES.getlist('file')
    user.avatar = list[0]
    user.save()
    return JsonResponse({'errno': '0', 'message': '成功'})


def changeCouponStat(couponID, stat, listPrice='-1'):
    # 只用于上架下架与过期
    try:
        coupon = models.Coupon.objects.get(couponid=couponID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '优惠券不存在', 'stat': '', 'listPrice': ''})

    if stat == 'onSale':
        if coupon.store is False:
            return JsonResponse({'errno': '1', 'message': '上架失败', 'stat': '',
                                 'listPrice': removeTailZero(str(coupon.listprice))})
        coupon.onsale = True
        coupon.store = False
        if listPrice != '-1':
            coupon.listprice = Decimal(listPrice)
        coupon.save()
        return JsonResponse({'errno': '0', 'message': '操作成功', 'stat': stat,
                             'listPrice': removeTailZero(str(coupon.listprice))})

    elif stat == 'store':
        if coupon.onsale is False:
            return JsonResponse({'errno': '1', 'message': '下架失败', 'stat': stat,
                                'listPrice': removeTailZero(str(coupon.listprice))})
        coupon.onsale = False
        coupon.store = True
        coupon.save()
        if models.Like.objects.filter(cid=couponID).exists():
            createMessage('关注的优惠券已下架', couponID)
            models.Like.objects.filter(cid=couponID).delete()
        return JsonResponse({'errno': '0', 'message': '操作成功', 'stat': stat,
                             'listPrice': removeTailZero(str(coupon.listprice))})

    elif stat == 'expired':
        coupon.onsale = False
        coupon.store = False
        coupon.expired = True
        coupon.save()
        if models.Like.objects.filter(cid=couponID).exists():
            createMessage('关注的优惠券已下架', couponID)
            models.Like.objects.filter(cid=couponID).delete()
        return JsonResponse({'errno': '0', 'message': '操作成功', 'stat': stat,
                             'listPrice': removeTailZero(str(coupon.listprice))})


# 获取数据
# def getListItem(listid):
#     lists = models.Couponlist.objects.get(listid=listid)
#     listItems = models.Listitem.objects.filter(listid=listid)
#     coupon = []
#     for item in listItems:
#         coupon.append(item.couponid.couponid)
#     listInfo = {'listID': listid, 'stat': lists.stat, 'coupons': coupon}
#     return listInfo


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
    productResult = models.Coupon.objects.filter(product__istartswith=keyword, onsale=True)
    brandResult = models.Brand.objects.filter(name__istartswith=keyword)
    result = []
    for coupon in productResult:
        if coupon.product not in result:
            result.append(coupon.product)
    result.reverse()
    result = result[0: min(6, len(result))]
    for brand in brandResult.reverse():
        if brand.name not in result:
            result.append(brand.name)
    result = result[0:min(9, len(result))]

    return JsonResponse({'result': result})


def searchResult(request):
    # history = request.COOKIES.get('history', '')
    key = request.GET.get('keyWord', False)
    orderBy = request.POST.get('order', None)
    page = int(request.GET.get('page', 1)) - 1
    if not key:
        return {'keyWord': key, 'maxPage': 0, 'currentPage': 0}
    if not orderBy:
        orderBy = 'expiredtime'
    else:
        pass
    result = []
    productResult = models.Coupon.objects.filter(product__icontains=key, onsale=True).order_by(orderBy)
    brandIDResult = models.Brand.objects.filter(name__icontains=key)
    productCount = productResult.count()
    brandCount = 0
    for i in range(0, 9):
        if (8 * page + i) >= productResult.count():
            break
        result.append(couponInfo(productResult[8 * page + i].couponid, request))
    # 数量不够时的结果仍需补全
    for brand in brandIDResult:
        pc = int(6 / brandIDResult.count())
        if pc == 0:
            pc = 1
        brandItem = models.Coupon.objects.filter(brandid=brand.brandid, onsale=True)
        brandCount = brandCount + brandItem.count()
        for i in range(0, pc):
            if (pc * page + i) >= brandItem.count():
                break
            result.append(couponInfo(brandItem[pc * page + i].couponid, request))
    maxPage = max(productCount / 9, brandCount / 6)
    if maxPage > int(maxPage):
        maxPage = int(maxPage) + 1
    # if not productResult.exists() and not brandIDResult.exists():
    #     return render(request, 'search.html')
    response = render(request, 'search.html', )
    # response.set_cookie('history', addSearchHistory(key, history))
    return {'coupons': result, 'keyWord': key, 'maxPage': maxPage, 'currentPage': page + 1}


def post_search(request):
    return render(request, 'search.html', searchResult(request))


def mobile_search(request):
    return render(request, 'mobile_search.html', searchResult(request))


def post_getUserCoupon(request):
    count = request.POST.get('couponsNumbers', '10')
    if count != 'all':
        count = int(count)
    if not request.uid:
        return {'couponsOwn': '', 'couponsLike': ''}

    ownCoupons = models.Coupon.objects.filter(userid=request.uid, store=True)
    onSaleCoupons = models.Coupon.objects.filter(userid=request.uid, onsale=True)
    likeCoupons = models.Like.objects.filter(userid=request.uid)

    messages = post_getMessage(request)
    own = []
    like = []
    onSale = []
    if ownCoupons.exists():
        if (count != 'all' and ownCoupons.count() <= count) or count == 'all':
            for coupon in ownCoupons:
                own.append(couponInfo(coupon.couponid, request))
        else:
            for i in range(0, count):
                own.append(couponInfo(ownCoupons[i].couponid, request))

    if likeCoupons.exists():
        if (count != 'all' and likeCoupons.count() <= count) or count == 'all':
            for coupon in likeCoupons:
                like.append(couponInfo(coupon.cid.couponid, request))
        else:
            for i in range(0, count):
                onSale.append(couponInfo(likeCoupons[i].cid.couponid, request))

    if onSaleCoupons.exists():
        if (count != 'all' and onSaleCoupons.count() <= count) or count == 'all':
            for coupon in onSaleCoupons:
                onSale.append(couponInfo(coupon.couponid, request))
        else:
            for i in range(0, count):
                onSale.append(couponInfo(onSaleCoupons[i].couponid, request))

    own.reverse()
    like.reverse()
    onSale.reverse()

    couponDict = {'couponsOwn': own, 'couponsLike': like, 'couponsOnSale': onSale,
                  'couponMessages': messages['couponMessages'], 'systemMessages': messages['systemMessages']}

    return couponDict


def post_getMobileUserCoupon(request):
    uid = request.uid
    own = models.Coupon.objects.filter(userid=uid, store=True)
    own.reverse()
    couponsStore = []
    couponsOnSale = []
    couponsExpired = []
    for coupon in own:
        info = couponInfo(coupon.couponid, request)
        if coupon.onsale is False:
            couponsStore.append(info)
        elif coupon.onsale is True:
            couponsOnSale.append(info)
        elif coupon.expired is True:
            info['expiredReason'] = '于' + info['expiredTime'] + '过期'
            couponsExpired.append(info)
        elif coupon.used is True:
            info['expiredReason'] = '已使用'
            couponsExpired.append(info)

    return {'couponsStore': couponsStore, 'couponsOnSale': couponsOnSale,
            'couponsExpired': couponsExpired}


def post_getBoughtCouponsMobile(request):
    uid = request.uid
    coupons = models.Coupon.objects.filter(bought__isnull=False, userid=uid)
    coupons.reverse()
    used = []
    own = []
    for couponid in coupons:
        if couponid.used is True:
            used.append(couponInfo(couponid.couponid, request))
        elif couponid.store is True:
            own.append(couponInfo(couponid.couponid, request))
    return {'own': own, 'used': used}


def post_getSoldOrLikeCouponsMobile(request, stat):
    uid = request.uid
    if stat == 'like':
        couponIDs = models.Like.objects.filter(uid=uid)
        couponIDs.reverse()
        result = []
        for couponid in couponIDs:
            result.append(couponInfo(couponid.couponid.couponid, request))

        return {'coupons' + stat: result}
    elif stat == 'sold':
        coupons = models.Coupon.objects.filter(sold__isnull=False, userid=uid)
        coupons.reverse()
        result = []
        for couponid in coupons:
            result.append(couponInfo(couponid.couponid, request))
        return {'coupons' + stat: result}


def post_getCouponByCat(request):
    catName = request.GET['catName']
    page = int(request.GET['page']) - 1
    try:
        catid = models.Category.objects.get(name=catName)
    except ObjectDoesNotExist:
        return JsonResponse({'error': '类别不存在'})
    coupons = models.Coupon.objects.filter(catid=catid, onsale=True)
    maxPage = coupons.count() / 16
    if maxPage > int(maxPage):
        maxPage = int(maxPage) + 1
    result = []
    for i in range(16 * page, min(16 * (page + 1), coupons.count())):
        result.append(couponInfo(coupons[i].couponid, request))

    return render(request, 'mobile_search.html',
                  {'coupons': result, 'keyWord': catName, 'maxPage': maxPage, 'currentPage': page + 1})


def post_getCouponByCatIndex(request):
    category = models.Category.objects.all().order_by('catid')
    couponByCat = {}
    for cat in category:
        coupons = models.Coupon.objects.filter(catid=cat.catid, onsale=True)
        coupons.reverse()
        couponByCat[cat.name] = []
        for i in range(0, min(9, coupons.count())):
            couponByCat[cat.name].append(couponInfo(coupons[i].couponid, request))
    # values = coupons.values()
    # values.reverse()
    # couponByCat[cat.name] = values[0:8]
    emptyCat = []
    for key in couponByCat:
        if not couponByCat[key]:
            emptyCat.append(key)
    for i in emptyCat:
        couponByCat.pop(i)
    result = {'coupons': couponByCat}
    return result


def post_getCouponForMobileIndex(request):
    index = int(request.COOKIES.get('indexM', '0'))
    couponsAll = models.Coupon.objects.filter(onsale=True)
    couponsAll.reverse()
    resultSet = []
    for i in range(index, min(couponsAll.count(), index + 10)):
        resultSet.append(couponInfo(couponsAll[i].couponid, request))
    if len(resultSet) == 0:
        resultSet = 'null'
    result = {'coupons': resultSet}
    # result = json.dumps(result)
    response = JsonResponse(result)
    response.set_cookie('indexM', index + 10)
    return response


def post_couponDetailMobile(request):
    uid = request.uid
    couponID = request.GET.get('couponID')
    if uid is None:
        like = False
    else:
        like = models.Like.objects.filter(uid=uid, cid=couponID).exists()

    if like:
        like = '1'
    else:
        like = '0'
    info = couponInfo(couponID, request)
    if info.get('error', False) is not False:
        return {'info': info, 'like': like, 'isOwner': '0'}
    sellerInfo = info['sellerInfo']
    if not sellerInfo or sellerInfo['userid'] == uid:
        isOwner = '1'
    else:
        isOwner = '0'
    return {'info': info, 'like': like, 'isOwner': isOwner}


def post_couponDetail(request):
    couponID = request.POST.get('couponID')
    info = couponInfo(couponID, request)
    # stat: 0 未关注 1 已关注 2 已上架 3 未上架
    return JsonResponse({'info': info, 'stat': info['stat']})



# def modifyStat(request, info, couponID):
#     # stat: 0 未关注 1 已关注 2 已上架 3 未上架
#     if request.uid is None:
#         info['stat'] = '0'
#         return info
#     sellerInfo = info['sellerInfo']
#     if not sellerInfo or sellerInfo['userid'] == request.uid:
#         if info['stat'] == 'onSale':
#             info['stat'] = '2'
#             return info
#         elif info['stat'] == 'store':
#             info['stat'] = '3'
#             return info
#     else:
#         likeList = models.Couponlist.objects.get(userid=request.uid, stat='like')
#         like = models.Listitem.objects.filter(listid=likeList.listid, couponid=couponID).exists()
#         if like:
#             info['stat'] = '1'
#             return info
#         else:
#             info['stat'] = '0'
#             return info


def couponInfo(couponID, request):
    try:
        coupon = models.Coupon.objects.get(couponid=couponID, sold__isnull=True)
    except ObjectDoesNotExist:
        return {'error': '找不到此优惠券信息'}
    limits = models.Limit.objects.filter(couponid=couponID)
    couponInfo = {}
    couponInfo['couponID'] = coupon.couponid
    couponInfo['brand'] = coupon.brandid.name
    couponInfo['cat'] = coupon.catid.name
    couponInfo['catID'] = coupon.catid.catid
    couponInfo['listPrice'] = removeTailZero(str(coupon.listprice))
    couponInfo['value'] = removeTailZero(str(coupon.value))
    couponInfo['product'] = coupon.product
    couponInfo['discount'] = coupon.discount
    couponInfo['stat'] = None
    couponInfo['pic'] = '/static/' + str(coupon.pic)
    couponInfo['expiredTime'] = coupon.expiredtime.strftime("%Y-%m-%d")
    couponInfo['bought'] = coupon.bought
    couponInfo['sold'] = coupon.sold
    limitList = []
    if limits.exists():
        for content in limits:
            limitList.append(content.content)
    couponInfo['limits'] = limitList
    couponInfo['sellerInfo'] = post_userInfo(coupon.userid.id)
    
    if request.uid is None:
        couponInfo['stat'] = '0'
        return couponInfo
    sellerInfo = couponInfo['sellerInfo']
    if not sellerInfo or sellerInfo['userid'] == request.uid:
        if coupon.onsale is True:
            couponInfo['stat'] = '2'
            return couponInfo
        elif coupon.store is True:
            couponInfo['stat'] = '3'
            return couponInfo
    else:
        like = models.Like.objects.filter(uid=request.uid, cid=couponID).exists()
        if like:
            couponInfo['stat'] = '1'
            return couponInfo
        else:
            couponInfo['stat'] = '0'
    return couponInfo


def post_userInfo(u_id):
    user = models.User.objects.get(id=u_id)

    nickname = user.nickname
    gender = user.gender
    UCoin = removeTailZero(str(user.ucoin))
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
    content = {'userid': u_id, 'nickname': nickname, 'gender': gender, 'UCoin': UCoin,
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
        message = {'messageID': item.messageid, 'time': item.time.strftime("%Y-%m-%d"), 'messageCat': item.messagecat,
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
    if stat == 'onSale':
        coupon = models.Coupon(couponid=couponID, userid=user, brandid=brandID, catid=catID, listPrice=listPrice,
                            value=value, product=product, discount=discount, onsale=True, pic=pic,
                            expiredTime=expiredTime)
        coupon.save()
    elif stat == 'store':
        coupon = models.Coupon(couponid=couponID, userid=user, brandid=brandID, catid=catID, listPrice=listPrice,
                               value=value, product=product, discount=discount, store=True, pic=pic,
                               expiredTime=expiredTime)
        coupon.save()


    return JsonResponse({'errno': 0, 'message': 'store success'})


def post_buy(request):
    couponID = request.POST['couponID']
    sellerID = request.POST['sellerID']
    buyerID = request.uid
    # 检查优惠券是否存在
    try:
        coupon = models.Coupon.objects.get(couponid=couponID, onsale=True)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '优惠券不存在'})
    # 检查卖家UCoin是否足够
    buyer = models.User.objects.get(id=buyerID)
    if buyer.ucoin < coupon.listprice:
        return JsonResponse({'errno': '1', 'message': 'UCoin不足以支付'})
    buyer.ucoin = buyer.ucoin - coupon.listprice
    # 优惠券状态由onSale修改为store
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    coupon.onsale = False
    coupon.store = False
    coupon.used = False
    coupon.expired = False
    coupon.sold = date
    newCoupon = models.Coupon(couponid=coupon, userid=buyer, brandid=coupon.brandid, catid=coupon.catid, listPrice=coupon.listPrice,
                               value=coupon.value, product=coupon.product, discount=coupon.discount, store=True, bought=date, pic=coupon.pic,
                               expiredTime=coupon.expiredTime)
    buyer.save()
    coupon.save()
    newCoupon.save()
    createMessage('上架的优惠券被购买', couponID)
    # 去掉所有like
    createMessage('关注的优惠券已被购买', couponID)
    like = models.Like.objects.filter(cid=couponID)
    for item in like:
        item.delete()
    return JsonResponse({'errno': '0', 'message': '购买成功'})


def post_putOnSale(request):
    couponID = request.POST['couponID']
    sellerID = request.uid
    listPrice = request.POST.get('listPrice', '-1')
    return changeCouponStat(couponID, 'onSale', listPrice)


def post_putOffSale(request):
    couponID = request.POST['couponID']
    sellerID = request.uid
    return changeCouponStat(couponID, sellerID, 'store')


def post_like(request):
    # 优惠券加入like列表
    couponID = request.POST['couponID']
    sellerID = request.uid
    try:
        coupon = models.Coupon.objects.get(couponid=couponID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '优惠券不存在', 'like': '0'})

    try:
        user = models.User.objects.get(id=sellerID)
    except ObjectDoesNotExist:
        return JsonResponse({'errno': '1', 'message': '用户不存在', 'like': '0'})
    if models.Like.objects.filter(uid=sellerID, cid=couponID).exists():
        return JsonResponse({'errno': '1', 'message': '该优惠券已被关注', 'like': '1'})

    models.Like.objects.create(uid=user, couponid=coupon)
    return JsonResponse({'errno': '0', 'message': '关注成功', 'like': '1'})


def post_dislike(request):
    # 优惠券加入like列表
    couponID = request.POST['couponID']
    sellerID = request.uid

    if models.Like.objects.filter(uid=sellerID, cid=couponID).exists():
        coupon = models.Like.objects.filter(uid=sellerID, cid=couponID)
        coupon.delete()
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
    coupon = models.Coupon.objects.get(couponid=couponID)
    # 根据messageType的不同寻找不同的接收USER，并填入相应的content
    #               0                    1                   2                3                 4
    types = ['上架的优惠券被购买', '上架的优惠券即将过期', '上架的优惠券已过期', '关注的优惠券即将过期', '关注的优惠券已被购买',
             '我的优惠券即将过期', '我的优惠券已过期', '关注的优惠券已下架', '系统通知']
    #               5                   6           7                8
    if messageType not in types:
        return {'errno': '1', 'message': '消息类型不存在'}

    userlist = []
    if messageType == types[3] or messageType == types[4] or messageType == types[7]:
        # like列表
        if models.Like.objects.filter(cid=couponID).exists():
            users = models.Like.objects.filter(cid=couponID)
            for user in users:
                userlist.append(user.uid)
        pass
    else:
        # own列表
        if models.Coupon.objects.filter(Q(store=True) | Q(store=True), couponid=couponID).exists():
            users = models.Coupon.objects.filter(Q(store=True) | Q(store=True), couponid=couponID)
            for user in users:
                userlist.append(user.userid)

    if content is None:
        content = messageType
    if not userlist:
        return {'errno': 0, 'message': '目标用户不存在'}
    for user in userlist:
        models.Message.objects.create(messageid=randomID(), userid=user, content=content,
                                      time=time.strftime("%Y-%m-%d", time.localtime()), messagecat=messageType,
                                      couponid=coupon, hasread=False, hassend=False)
    return {'errno': '0', 'message': '成功'}


# 为用户添加各种表
# def createLists(user):
#     # models.User.objects.create
#     stat = ['own', 'sold', 'bought', 'onSale', 'like']
#     for content in stat:
#         models.Couponlist.objects.create(userid=user, stat=content, listid=None)


# get方法函数
def index(request):
    return render(request, 'index.html', post_getCouponByCatIndex(request))


def login(request):
    return render(request, 'login.html')


def mobile_login(request):
    return render(request, 'mobile_login.html')


def mobile_index(request):
    return render(request, 'mobile_index.html')


def userPage(request):
    return render(request, 'user.html', post_getUserCoupon(request))


def myCouponsPage(request):
    return render(request, 'mobile_mycoupons.html', post_getMobileUserCoupon(request))


def search(request):
    return render(request, 'search.html')


def commodity(request):
    detail = post_couponDetailMobile(request)
    if detail['isOwner'] == '1':
        return render(request, 'mobile_mycoupons_for_sell.html', detail)
    return render(request, 'commodity.html', detail)


def mobile_appraisement(request):
    return render(request, 'mobile_appraisement.html')


def mobile_user_setting(request):
    return render(request, 'mobile_user_setting.html')


def mobile_user_wallet(request):
    return render(request, 'mobile_user_wallet.html')


def mobile_user(request):
    return render(request, 'mobile_user.html', post_getUserCoupon(request))


def mobile_couponsmessage(request):
    return render(request, 'mobile_couponsmessage.html')


def mobile_sell_final(request):
    return render(request, 'mobile_sell_final.html', post_couponDetailMobile(request))


def mobile_couponsmessage(request):
    return render(request, 'mobile_couponsmessage.html')


def mobile_myboughtcoupons(request):
    return render(request, 'mobile_myboughtcoupons.html', post_getBoughtCouponsMobile(request))


def mobile_mysoldcoupons(request):
    return render(request, 'mobile_mysoldcoupons.html', post_getSoldOrLikeCouponsMobile(request, 'Sold'))


def mobile_mylikecoupons(request):
    return render(request, 'mobile_mylikecoupons.html', post_getSoldOrLikeCouponsMobile(request, 'Like'))


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


def post_logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('uhui')
    return response


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
        # createLists(user)

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

        # createLists(user)
        return JsonResponse({'errno': '0', 'message': '注册成功'})


# 根据request的COOKIES判断登录uid
def get_uid(request):
    cookie_content = request.COOKIES.get('uhui', False)
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
