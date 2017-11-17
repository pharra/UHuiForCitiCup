

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django import forms
from rest_framework.parsers import JSONParser
from UHuiWebApp.models import *
from apiForAndroid.serializers import *
from UHuiWebApp.views import *
from django.core import serializers
#返回json数据

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
# Create your views here.
class userForm(forms.Form):
    userID = forms.CharField()
    avatar = forms.FileField()

#注册
def signUpForAndroid(request):
    return post_signUp(request)


#登录
def loginForAndroid(request):
    u_name = request.POST.get('username')
    # 通过@判断用户名为email/手机号
    if "@" in u_name:
        # 查询用户是否存在
        user = models.User.objects.filter(email=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(email=u_name)
        uid = User.objects.get(email = u_name).id
        name = User.objects.get(email=u_name).nickname
        ava = str(User.objects.get(email=u_name).avatar)
        coin = User.objects.get(email=u_name).ucoin
        gen = User.objects.get(email=u_name).gender
    else:
        user = models.User.objects.filter(phonenum=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(phonenum=u_name)
        uid = User.objects.get(phonenum=u_name).id
        name = User.objects.get(phonenum=u_name).nickname
        ava = str(User.objects.get(phonenum=u_name).avatar)
        coin = User.objects.get(phonenum=u_name).ucoin
        gen = User.objects.get(phonenum = u_name).gender

    psw = encryption(request.POST.get('password'))
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    if psw == password:
        response = JsonResponse({'result': 'success','userid':uid,'nickname':name,'avatar':ava,'Ucoin':coin,'gender':gen})
        return response
    else:
        return JsonResponse({'error': '密码错误'})


#预搜索
def preSearch(request):
    keyword = request.POST.get('keyword')
    #if not keyword:
    #    return JsonResponse({'error':'keyword not exist'})
    productResult = Coupon.objects.filter(product__istartswith=keyword,onsale = 1).values('product').distinct()
    result = []
    for coupon in productResult:
        result.append(coupon)
    return JsonResponse({'result':result})


#分类下预搜索
def preSearchInCategory(request):
    keyword = request.POST.get('keyword')
    cat = request.POST.get('category')
    #if not keyword:
    #    return JsonResponse({'error':'keyword not exist'})
    productResult = Coupon.objects.filter(product__istartswith=keyword,onsale=1,catid=cat).values('product').distinct()
    result = []
    for coupon in productResult:
        result.append(coupon)
    return JsonResponse({'result':result})


#搜索
def searchForAndroid(request):
    key = request.POST.get('keyWord',0)
    orderBy = request.POST.get('order', None)
    if key == 0:
        return {'error': '101'}
    if orderBy == '':
        orderBy = 'expiredtime'
    else:
        pass
    productResult = models.Coupon.objects.filter(product__icontains=key, onsale=1).order_by(orderBy)
    result = []
    for each in productResult:
        dic = {
            'couponid': each.couponid,
            'listprice': each.listprice,
            'value': Valueset.objects.get(vid=each.value.vid).value,
            'product': each.product,
            'discount': each.discount,
            'pic':str(each.pic),
            'expiredtime': each.expiredtime,
            'category': Category.objects.get(catid=each.catid.catid).name,
            'brand': Brand.objects.get(brandid=each.brandid.brandid).name,
                   }
        result.append(dic)
    brandIDResult = models.Brand.objects.filter(name__icontains=key)
    for brand in brandIDResult:
        temp = models.Coupon.objects.filter(brandid=brand.brandid,onsale = 1)
        if temp.exists():
            for each in temp:
                dic = {
                    'couponid': each.couponid,
                    'listprice': each.listprice,
                    'value': Valueset.objects.get(vid=each.value.vid).value,
                    'product': each.product,
                    'discount': each.discount,
                    'pic': str(each.pic),
                    'expiredtime': each.expiredtime,
                    'category': Category.objects.get(catid=each.catid.catid).name,
                }
                result.append(dic)
        return JsonResponse({'result': result})
    if result == None:
        return JsonResponse({'error':'102'})
    return JsonResponse({'result':result})


#在分类下搜索
def searchInCategory(request):
    key = request.POST.get('keyWord', 0)
    cat = request.POST.get('catId',0)
    orderBy = request.POST.get('order',None)
    if cat == 0:
        return JsonResponse({'error': '103'})
    if key == 0:
        return JsonResponse({'error': '101'})
    if orderBy == '':
        orderBy = 'expiredtime'
    else:
        pass
    productResult = models.Coupon.objects.filter(product__contains=key, onsale=1,catid=cat).order_by(orderBy)
    result = []
    for each in productResult:
        dic = {
            'couponid': each.couponid,
            'listprice': each.listprice,
            'value': Valueset.objects.get(vid=each.value.vid).value,
            'product': each.product,
            'discount': each.discount,
            'pic':str(each.pic),
            'expiredtime': each.expiredtime,
            'category': Category.objects.get(catid=each.catid.catid).name,
                   }
        result.append(dic)
    brandIDResult = models.Brand.objects.filter(name__contains=key)
    for brand in brandIDResult:
        temp = models.Coupon.objects.filter(brandid=brand.brandid, onsale=1,catid=cat)
        if temp.exists():
            for each in temp:
                dic = {
                    'couponid': each.couponid,
                    'listprice': each.listprice,
                    'value': Valueset.objects.get(vid=each.value.vid).value,
                    'product': each.product,
                    'discount': each.discount,
                    'pic': str(each.pic),
                    'expiredtime': each.expiredtime,
                    'category': Category.objects.get(catid=each.catid.catid).name,
                }
                result.append(dic)
        return JsonResponse({'result': result})
    if result == None:
        return JsonResponse({'error': '102'})
    return JsonResponse({'result': result})


#点击种类进行查询
def searchByCategory(request):
    catID = request.POST.get('categoryID',0)
    orderBy = request.POST.get('order', 'expiredtime')
    if Category.objects.filter(catid=catID).exists():
        result = []
        couponList = Coupon.objects.filter(catid=catID, onsale=1).order_by(orderBy)
        for each in couponList:
            dic = {
                'couponid': each.couponid,
                'listprice': each.listprice,
                'value': Valueset.objects.get(vid=each.value.vid).value,
                'product': each.product,
                'discount': each.discount,
                'pic': str(each.pic),
                'expiredtime': each.expiredtime,
            }
            result.append(dic)
        return JsonResponse({'result': result})
    return JsonResponse({'error':'103'})


#查询优惠券详细信息
def couponDetail(request):
    cpID = request.POST.get('couponID',0)
    if cpID == 0 :
        return JsonResponse({'error':'104'})
    CouponResult = Coupon.objects.filter(pk=cpID).values()
    CResult= []
    for coupon in CouponResult:
        CResult.append(coupon)
    LimitResult = Limit.objects.filter(couponid = cpID).values('content')
    LResult = []
    for limit in LimitResult:
        LResult.append(limit)
    #查询所有者ID
    userid = Coupon.objects.get(couponid=cpID).userid.id
    Seller = User.objects.filter(pk = userid).values('id','nickname','gender','avatar')
    SResult = []
    for seller in Seller:
        SResult.append(seller)
    brandID = Coupon.objects.get(couponid=cpID).brandid.brandid
    brandResult = Brand.objects.filter(brandid=brandID).values('name')
    BResult = []
    for i in brandResult:
        BResult.append(i)
    return JsonResponse({'coupon':CResult,'limit':LResult,'seller':SResult,'brand':BResult})


#返回使用限制、商家名以及出售者信息
def returnInformation(request):
    cpID = request.POST.get('couponID',0)
    u_id = request.POST.get('userID')
    stat= request.POST.get('stat',1)#01
    if u_id=='':
        return JsonResponse({'error':'105'})
    if cpID == 0 :
        return JsonResponse({'error':'104'})
    isLike = 0
    #查看该优惠券是否已被关注
    if Like.objects.filter(cid=cpID,uid=u_id).exists():
        isLike = 1
    limitResult = Limit.objects.filter(couponid = cpID).values('content')
    LResult = []
    for limit in limitResult:
        LResult.append(limit)
    sellerID = None
    if stat == 1:
        if Coupon.objects.filter(couponid=cpID,sold__isnull=True).exists():
            sellerID = Coupon.objects.filter(couponid=cpID,sold__isnull=True)[0].userid.id
    elif stat == 0:
        if Coupon.objects.filter(couponid=cpID,expired=0,used=0,onsale=0,store=0).exists():
            sellerID = Coupon.objects.filter(couponid=cpID,expired=0,used=0,onsale=0,store=0)[0].userid.id
    Seller = User.objects.filter(pk=sellerID).values('id','nickname','gender','avatar')
    SResult = []
    for seller in Seller:
        SResult.append(seller)
    brandID = Coupon.objects.get(couponid=cpID, sold__isnull=True).brandid.brandid
    brandResult = Brand.objects.filter(brandid=brandID).values('name')
    #brand = Brand.objects.get(brandid = brandID)
    BResult = []
    #AResult = []
    for b in brandResult:
        BResult.append(b)
    #AreaResult = Area.objects.filter(areaid=brand.areaid.areaid).values('areaid','x','y')
    #for each in AreaResult:
    #    AResult.append(each)
    return JsonResponse({'brand': BResult, 'limit': LResult, 'seller': SResult,'isLike':isLike})


#返回出售者正在卖的优惠券
def sellerOnSaleList(request):
    sellerID = request.POST.get('sellerID',0)
    if sellerID ==0:
        return JsonResponse({'error':'105'})
    sellerOnSaleList = Coupon.objects.filter(userid=sellerID,onsale=1)
    #sellerSoldList = Coupon.objects.filter(userid=sellerID,sold__isnull=False)
    onSaleList =[]
    #soldList = []
    for each in sellerOnSaleList:
        dic = {
            'couponid': each.couponid,
            'listprice': each.listprice,
            'value': Valueset.objects.get(vid=each.value.vid).value,
            'product': each.product,
            'discount': each.discount,
            'pic': str(each.pic),
            'expiredtime': each.expiredtime,
        }
        onSaleList.append(dic)
    #for each in sellerSoldList:
    #    soldList.append(each)
    return JsonResponse({'result':onSaleList})


#返回出售者正在卖的优惠券
def sellerSoldList(request):
    sellerID = request.POST.get('sellerID',0)
    if sellerID ==0:
        return JsonResponse({'error':'105'})
    #sellerOnSaleList = Coupon.objects.filter(userid=sellerID,onsale=1)
    sellerSoldList = Coupon.objects.filter(userid=sellerID,sold__isnull=False)
    #onSaleList =[]
    soldList = []
    if sellerSoldList != None:
        for each in sellerSoldList:
            dic = {
                'couponid': each.couponid,
                'listprice': each.listprice,
                'value': Valueset.objects.get(vid=each.value.vid).value,
                'product': each.product,
                'discount': each.discount,
                'pic': str(each.pic),
                'expiredtime': each.expiredtime,
            }
            soldList.append(dic)
    #for each in sellerSoldList:
    #    soldList.append(each)
    return JsonResponse({'result':soldList})


#通过优惠券ID查询所有
'''
def ownerDetail(request):
    cpID = request.POST.get('couponID',0)
    checklistitem = Listitem.objects.filter(couponid=cpID)
    checklistID = checklistitem.values('listid')
    checkCouponlist = Couponlist.objects.filter(listid=checklistID).filter(stat='onSale')
    checkUserid =  checkCouponlist.values('userid')
    try:
        result = User.objects.filter(id=checkUserid)
    except User.DoesNotExist:
        return JsonResponse({'error':'105'})
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata,content_type='application/json')'''


#购买
def buyCoupon(request):
    cpID = request.POST.get('couponID',0)
    u_id = request.POST.get('userID',0)
    #检查优惠券是否存在
    coupon = models.Coupon.objects.get(couponid=cpID)
    if coupon.onsale != 1:
        return JsonResponse({'error': '106'})
    #检查用户UCoin
    buyerUCoin = models.User.objects.get(id=u_id).ucoin
    if buyerUCoin < coupon.listprice:
        return JsonResponse({'error': '107'})
    #修改当前优惠券状态
    coupon.onsale = 0
    coupon.store = 0
    coupon.expired = 0
    coupon.used = 0
    coupon.sold = time.strftime("%Y-%m-%d", time.localtime())
    coupon.save()
    #创建新的coupon行
    user = User.objects.get(id=u_id)
    Coupon.objects.create(couponid = coupon.couponid,userid = user,brandid = coupon.brandid,catid = coupon.catid,listprice = coupon.listprice,discount = coupon.discount,value = coupon.value,product = coupon.product,pic = coupon.pic,expiredtime = coupon.expiredtime,onsale = 0,expired = 0,used = 0,store = 1,bought = time.strftime("%Y-%m-%d", time.localtime()))
    #修改用户UCoin
    seller = coupon.userid
    userUcoin = buyerUCoin-coupon.listprice
    User.objects.filter(id=u_id).update(ucoin = userUcoin)
    sellerUcoin = seller.ucoin + coupon.listprice
    User.objects.filter(id = seller.id).update(ucoin = sellerUcoin)
    #生成通知拥有者的message
    createMessage('上架的优惠券被购买', cpID)
    #生成通知关注者的message
    createMessage('关注的优惠券已被购买', cpID)

    tmp = Like.objects.filter(cid=cpID)
    for each in tmp:
        each.delete()

    return JsonResponse({'result':'200'})


#关注优惠券接口
def likeCoupon(request):
    cpID = request.POST.get('couponID',0)
    u_ID = request.POST.get('userID',0)
    if Like.objects.filter(cid=cpID,uid=u_ID).exists():
        return JsonResponse({'error':'115'})
    cp = Coupon.objects.get(couponid=cpID)
    user = User.objects.get(id=u_ID)
    Like.objects.create(cid=cp,uid=user)
    return JsonResponse({'result':'200'})


#取消关注
def dislikeCoupon(request):
    cpID = request.POST.get('couponID', 0)
    u_ID = request.POST.get('userID', 0)
    if Like.objects.filter(cid=cpID, uid=u_ID).exists():
        Like.objects.get(cid=cpID,uid=u_ID).delete()
        return JsonResponse({'result': '200'})
    return JsonResponse({'error': '116'})


#消息发送接口
def sendMessage(request):
    userID = request.POST.get('userID',0)
    tmp = Message.objects.filter(userid=userID)
    msg = Message.objects.filter(userid=userID).values('messageid','content','time','messagecat','hasread','couponid')
    messageResult = []
    couponResult = []
    for each in msg:
        messageResult.append(each)
    for i in tmp:
        cp = Coupon.objects.filter(couponid=i.couponid)
        dic = {
                'couponid': cp[0].couponid,
                'listprice': cp[0].listprice,
                'value': Valueset.objects.get(vid=cp[0].value.vid).value,
                'product': cp[0].product,
                'discount': cp[0].discount,
                'pic': str(cp[0].pic),
                'expiredtime': cp[0].expiredtime,
            }
        couponResult.append(dic)
    return JsonResponse({'messageResult':messageResult,'couponResult':couponResult})


#修改密码接口
def updatePassword(request):
    newPassword = request.POST.get('password',0)
    phone = request.POST.get('phoneNum',0)
    newPassword = encryption(newPassword)
    if newPassword == User.objects.get(phonenum = phone).password:
        return JsonResponse({'error':'108'})
    User.objects.filter(phonenum=phone).update(password = newPassword)
    return JsonResponse({'result':'200'})


#判断手机/邮箱是否存在
def checkUsername(request):
    username = request.POST.get('username')
    if '@' in username:
        if User.objects.filter(email=username).exists():
            return JsonResponse({'error':'109'})
        return JsonResponse({'result':'200'})
    else:
        if User.objects.filter(phonenum=username).exists():
            return JsonResponse({'error': '109'})
        return JsonResponse({'result': '200'})


#获取个人信息
def getUserInformation(request):
    u_id = request.POST.get('userID')
    result = User.objects.filter(pk = u_id)
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata,content_type='application/json')


#修改个人信息
def updateUserInformation(request):
    u_id = request.POST.get('userID')
    user = User.objects.get(id=u_id)
    newNickname = request.POST.get('nickname')
    newGender = request.POST.get('gender',user.gender)
    if User.objects.filter(nickname=newNickname).exists():
        return JsonResponse({'error':'110'})
    if newNickname!=None:
        user.nickname = newNickname
        user.save()
    if newGender!=None:
        user.gender = newGender
        user.save()
    return JsonResponse({'result':'200'})


#修改头像
def updateAvatar(request):
    #uf = userForm(request.POST,request.FILES)
    #u_id = uf.cleaned_data['userID']
    #headImg = uf.cleaned_data['avatar']
    u_id = request.POST.get('userID',0)
    if u_id == 0:
        return JsonResponse({'error':'105'})
    headImg = request.FILES.get('imgFile',None)
    user = User.objects.get(id = u_id)
    if User.objects.filter(id = u_id).exists():
        user.avatar = headImg
        user.save()
    return JsonResponse({'result': '200'})


#修改手机/邮箱
def updatePhoneOrEmail(request):
    u_id = request.POST.get('userID')
    NewPhoneOrEmail = request.POST.get('username')
    userObj = User.objects.get(pk = u_id)
    if  '@'in NewPhoneOrEmail:
        if userObj.phonenum == None:
            userObj.email = NewPhoneOrEmail
            userObj.save()
            return JsonResponse({'result':'200'})
        else:
            return JsonResponse({'error':'111'})
    else:
        if userObj.email == None:
            userObj.phonenum = NewPhoneOrEmail
            userObj.save()
            return JsonResponse({'result':'200'})
        else:
            return JsonResponse({'error':'112'})


#估值
def getValue(request):
    #couponID = request.POST.get('couponID')
    #coupon = Coupon.objects.get(couponid=couponID)
    discount = request.POST.get('discount')
    result = []
    if Valueset.objects.filter(description=discount).exists():
        temp = Valueset.objects.filter(description=discount)[0]
        result.append({'vid':temp.vid, 'value': float(str(temp.value))})
        return JsonResponse({'result': result})
    else:
        Valueset.objects.create(value = 0.0, description = discount)
        temp = Valueset.objects.filter(description=discount)[0]
        result.append({'vid': temp.vid, 'value': float(str(temp.value))})
        return JsonResponse({'result': result})




#添加优惠券
def addCoupon(request):
    u_id = request.POST.get('userID')
    brandName = request.POST.get('brand')
    cat = request.POST.get('category')
    expiredTime = datetime.datetime.strptime(request.POST.get('expiredTime'), '%Y-%m-%d')
    listPrice = float(request.POST.get('listPrice'))
    product = request.POST.get('product')
    discount = request.POST.get('discount')
    stat = request.POST.get('stat', 'store')
    pic = request.FILES.get('pic', DEFAULT_PIC)
    limit = request.POST.getlist('limit[]')

    if Valueset.objects.filter(description=discount).exists():
        temp_v = Valueset.objects.filter(description=discount)[0]
    else:
        Valueset.objects.create(value = 0.0, description = discount)
        temp_v = Valueset.objects.filter(description=discount)[0]

    #估值
    # 判断brand是否存在
    if not models.Brand.objects.filter(name=brandName).exists():
        brandID = models.Brand(brandid=None, name=brandName)
        brandID.save()
    else:
        brandID = models.Brand.objects.get(name=brandName)
    # 获取catID
    #if not models.Category.objects.filter(name=cat).exists():
    #    return JsonResponse({'errno': 1, 'message': 'category not found'})
    #else:
    catID = models.Category.objects.get(catid=cat)
    user = models.User.objects.get(id=u_id)
    #temp_v = Valueset.objects.get(vid=value)
    couponID = randomID()

    if stat == 'store':
        coupon = models.Coupon(couponid=couponID, userid=user, brandid=brandID, catid=catID, listprice=listPrice,
                               value=temp_v, product=product, discount=discount, onsale=0, store=1, expired=0, used=0,
                               pic=pic,
                               expiredtime=expiredTime)
        coupon.save()
    elif stat == 'onsale':
        coupon = models.Coupon(couponid=couponID, userid=user, brandid=brandID, catid=catID, listprice=listPrice,
                               value=temp_v, product=product, discount=discount, onsale=0, store=1, expired=0, used=0,
                               pic=pic,
                               expiredtime=expiredTime)
        coupon.save()
        changeCouponStat(couponID, 'onSale', listPrice)
    else:
        return JsonResponse({'error':'113'})

    for each in limit:
        Limit.objects.create(couponid=coupon,content=each)
    return JsonResponse({'result': '200'})


#获取"我买过的"优惠券
def getBoughtList(request):
    u_id = request.POST.get('userID')
    boughtList = []
    if User.objects.filter(id=u_id).exists():
        tmp = Coupon.objects.filter(userid=u_id,bought__isnull=False)
        for each in tmp:
            tempDic = {'couponid': each.couponid,
                       'product': each.product,
                       'listprice': each.listprice,
                       'value': Valueset.objects.get(vid=each.value.vid).value,
                       'expiredtime': each.expiredtime,
                       'discount': each.discount,
                       'pic': str(each.pic),
                       }
            boughtList.append(tempDic)
        return JsonResponse({'result':boughtList})
    else:
        return JsonResponse({'error':'105'})


#获取我拥有的优惠券
'''def getOwnList(request):
    u_id = request.POST.get('userID')
    onSaleList =[]
    storeList = []
    usedList = []
    if User.objects.filter(id=u_id).exists():
        ownListID = Couponlist.objects.get(userid=u_id,stat='own').listid
        ownListitem = Listitem.objects.filter(listid=ownListID)
        for each in ownListitem:
            tmpOnSalelist = Coupon.objects.filter(couponid=each.couponid.couponid,stat='onSale').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount','pic')
            for i in tmpOnSalelist:
                onSaleList.append(i)
            tmpStoreList = Coupon.objects.filter(couponid=each.couponid.couponid,stat = 'store').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount','pic')
            for i in tmpStoreList:
                storeList.append(i)
            tmpUsedList = Coupon.objects.filter(couponid=each.couponid.couponid,stat='used').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount','pic')
            for i in tmpUsedList:
                usedList.append(i)
        return JsonResponse({'onSaleList':onSaleList,'storeList':storeList,'usedList':usedList})
    else:
        return JsonResponse({'result':'user not exist'})'''


#获取我正在出售的优惠券
def getOnSaleList(request):
    u_id = request.POST.get('userID')
    onSaleList =[]
    if User.objects.filter(id=u_id).exists():
        tmp = Coupon.objects.filter(userid=u_id,onsale=1)
        for each in tmp:
            tempDic = {'couponid': each.couponid,
                       'product': each.product,
                       'listprice': each.listprice,
                       'value': Valueset.objects.get(vid=each.value.vid).value,
                       'expiredtime': each.expiredtime,
                       'discount': each.discount,
                       'pic': str(each.pic),
                       }
            onSaleList.append(tempDic)
        return JsonResponse({'result':onSaleList})
    else:
        return JsonResponse({'error':'105'})


#获取我存储的优惠券
def getStoreList(request):
    u_id = request.POST.get('userID')
    storeList = []
    if User.objects.filter(id= u_id).exists():
        tmp = Coupon.objects.filter(userid=u_id,store=1)
        for each in tmp:
            tempDic = {'couponid':each.couponid,
                       'product':each.product,
                       'listprice': each.listprice,
                       'value': Valueset.objects.get(vid=each.value.vid).value,
                       'expiredtime': each.expiredtime,
                       'discount': each.discount,
                       'pic': str(each.pic),
                       }
            storeList.append(tempDic)
        return JsonResponse({'result':storeList})
    else:
        return JsonResponse({'error':'105'})


#获取我用过的优惠券
def getUsedList(request):
    u_id = request.POST.get('userID')
    usedList = []
    if User.objects.filter(id = u_id).exists():
        tmp = Coupon.objects.filter(userid=u_id,used=1)
        for each in tmp:
            tempDic = {'couponid': each.couponid,
                       'product': each.product,
                       'listprice': each.listprice,
                       'value': Valueset.objects.get(vid=each.value.vid).value,
                       'expiredtime': each.expiredtime,
                       'discount': each.discount,
                       }
            usedList.append(tempDic)
        return JsonResponse({'result':usedList})
    else:
        return JsonResponse({'error':'105'})


#获取我卖出的优惠券
def getSoldList(request):
    u_id = request.POST.get('userID')
    soldList = []
    if User.objects.filter(id = u_id).exists():
        tmp = Coupon.objects.filter(userid=u_id,sold__isnull=False)
        for each in tmp:
            tempDic = {'couponid': each.couponid,
                       'product': each.product,
                       'listprice': each.listprice,
                       'value': Valueset.objects.get(vid=each.value.vid).value,
                       'expiredtime': each.expiredtime,
                       'discount': each.discount,
                       'pic': str(each.pic),
                       }
            soldList.append(tempDic)
        return JsonResponse({'result':soldList})
    else:
        return JsonResponse({'error':'105'})


#获取我用过的优惠券
'''def post_getUsedCoupon(request):
    u_id = request.POST.get('userID')
    usedList =[]
    if User.objects.filter(id = u_id).exists():
        ownListID = Couponlist.objects.get(userid=u_id,stat='own').listid
        ownListitem = Listitem.objects.filter(listid=ownListID)
        for each in ownListitem:
            couponList = Coupon.objects.filter(couponid=each.couponid.couponid,stat='used').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in couponList:
                usedList.append(i)
        return JsonResponse({'usedList':usedList})
    else:
        return JsonResponse({'result':'user not exist'})'''


#充值
def buyUcoin(request):
    pass


#獲取關注列表
def getLikeList(request):
    u_id = request.POST.get('userID')
    likeList = []
    if User.objects.filter(id = u_id).exists():
        tmp = Like.objects.filter(uid=u_id)
        for each in tmp:
            cp = Coupon.objects.get(couponid=each.cid.couponid)
            tempDic = {'couponid': cp.couponid,
                       'product': cp.product,
                       'listprice': cp.listprice,
                       'value': Valueset.objects.get(vid=cp.value.vid).value,
                       'expiredtime': cp.expiredtime,
                       'discount': cp.discount,
                       'pic': str(each.pic),
                       }
            likeList.append(tempDic)
        return JsonResponse({'result':likeList})
    else:
        return JsonResponse({'error':'105'})


#上架下架已拥有的优惠券  还需要创建message
def changeCouponState(request):
    cpID = request.POST.get('couponID')
    newStat = request.POST.get('state')
    cp = Coupon.objects.filter(couponid=cpID,sold__isnull=True)
    if newStat=='onSale':
        for each in cp:
            if each.store == 1:
                cp.update(store = 0,onsale = 1)
                Valuecalculate.objects.create(vid=each.value,listprice=each.listprice)
                calculateValue(each.couponid)
                return JsonResponse({'result': '200'})
            else:
                return JsonResponse({'error': '113'})
    elif newStat == 'store':
        for each in cp:
            if each.onsale == 1:
                cp.update(store =1,onsale = 0)
                Valuecalculate.objects.filter(listprice=each.listprice)[0].delete()
                calculateValue(each.couponid)
                return JsonResponse({'result': '200'})
            else:
                return JsonResponse({'error': '113'})
    else:
        return JsonResponse({'error':'114'})


#主页的推荐
def homepageCoupon(request):
    couponCat_1 = Coupon.objects.filter(catid = 1,onsale = 1)
    tmp1 = couponCat_1.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_1.count(),5)].reverse()#生活百货
    couponCat_2 = Coupon.objects.filter(catid = 2,onsale = 1)
    tmp2 = couponCat_2.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_2.count(),5)].reverse()#美妆装饰
    couponCat_3 = Coupon.objects.filter(catid = 3,onsale = 1)
    tmp3 = couponCat_3.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_3.count(),5)].reverse()#文娱体育
    couponCat_4 = Coupon.objects.filter(catid = 4,onsale = 1)
    tmp4 = couponCat_4.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_4.count(),5)].reverse()#家具家居
    couponCat_5 = Coupon.objects.filter(catid = 5,onsale = 1)
    tmp5 = couponCat_5.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_5.count(),5)].reverse()#电子产品
    couponCat_6 = Coupon.objects.filter(catid = 6,onsale = 1)
    tmp6 = couponCat_6.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_6.count(),5)].reverse()#服装服饰
    couponCat_7 = Coupon.objects.filter(catid = 7,onsale = 1)
    tmp7 = couponCat_7.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_7.count(),5)].reverse()#旅行住宿
    couponCat_8 = Coupon.objects.filter(catid = 8,onsale = 1)
    tmp8 = couponCat_8.values('couponid','listprice','value','product','discount','pic','expiredtime')[0:min(couponCat_8.count(),5)].reverse()#饮食保健
    result=[]
    for each in tmp1:
        each['category'] = Category.objects.get(catid=1).name
        result.append(each)
    for each in tmp2:
        each['category'] = Category.objects.get(catid=2).name
        result.append(each)
    for each in tmp3:
        each['category'] = Category.objects.get(catid=3).name
        result.append(each)
    for each in tmp4:
        each['category'] = Category.objects.get(catid=4).name
        result.append(each)
    for each in tmp5:
        each['category'] = Category.objects.get(catid=5).name
        result.append(each)
    for each in tmp6:
        each['category'] = Category.objects.get(catid=6).name
        result.append(each)
    for each in tmp7:
        each['category'] = Category.objects.get(catid=7).name
        result.append(each)
    for each in tmp8:
        each['category'] = Category.objects.get(catid=8).name
        result.append(each)
    return JsonResponse({'result':result})


#搜索栏的推荐 未完成
def searchCoupon(request):
    pass


#主页轮播图
def getBanner(request):
    url1 = 'images/banner/banner_1.jpg'
    url2 = 'images/banner/banner_2.jpg'
    url3 = 'images/banner/banner_3.jpg'
    url4 = 'images/banner/banner_4.jpg'
    url5 = 'images/banner/banner_5.jpg'
    result = []
    result.append(url1)
    result.append(url2)
    result.append(url3)
    result.append(url4)
    result.append(url5)
    return JsonResponse({'result':result})



