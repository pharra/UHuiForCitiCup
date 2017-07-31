from django.shortcuts import render

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
def post_signUpForAndroid(request):
    return post_signUp(request)


#登录
def post_loginForAndroid(request):
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
def post_preSearch(request):
    keyword = request.POST.get('keyword')
    #if not keyword:
    #    return JsonResponse({'error':'keyword not exist'})
    productResult = Coupon.objects.filter(product__startswith=keyword,stat='onSale').values('product')
    result = []
    for coupon in productResult:
        result.append(coupon)
    return JsonResponse({'result':result})


#搜索
def post_searchForAndroid(request):
    key = request.POST.get('keyWord',0)
    orderBy = request.POST.get('order', None)
    if not key:
        return {'result': "请输入关键词"}
    if not orderBy:
        orderBy = 'expiredtime'
    else:
        pass
    productResult = models.Coupon.objects.filter(product__contains=key, stat='onSale').values('couponid','listprice','value','product','discount','pic','expiredtime').order_by(orderBy)
    result = []
    for coupon in productResult:
        result.append(coupon)
    brandIDResult = models.Brand.objects.filter(name__contains=key)
    for brand in brandIDResult:
        temp = models.Coupon.objects.filter(brandid=brand.brandid,stat = 'onSale').values('couponid','listprice','value','product','discount','pic','expiredtime')
        if temp.exists():
            for info in temp:
                result.append(info)
        return JsonResponse({'coupons': result})
    if result == None:
        return JsonResponse({'result':'result no exist'})
    return JsonResponse({'coupon':result})


#点击种类进行查询
def post_searchByCategory(request):
    catID = request.POST.get('categoryID',0)
    if Category.objects.filter(catid=catID).exists():
        return JsonResponse({'error':'不存在该种类'})
    result = []
    couponList = Coupon.objects.filter(catid=catID,stat='onSale').values('couponid','listprice','value','product','discount','pic','expiredtime')
    for each in couponList:
        result.append(each)
    return JsonResponse({'result':result})


#查询优惠券详细信息
def post_couponDetailForAndroid(request):
    cpID = request.POST.get('couponID',0)
    if cpID == 0 :
        return JsonResponse({'error':'优惠券不存在'})
    CouponResult = Coupon.objects.filter(pk=cpID).values()
    CResult= []
    for coupon in CouponResult:
        CResult.append(coupon)
    LimitResult = Limit.objects.filter(couponid = cpID).values('content')
    LResult = []
    for limit in LimitResult:
        LResult.append(limit)
    #查询所有者ID
    checklist = Listitem.objects.filter(couponid=cpID)
    checkUserid = 0
    for each in checklist:
        listID = each.listid.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            checkUserid = listStat.userid.id
    Seller = User.objects.filter(pk = checkUserid).values('id','nickname','gender','avatar')
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
def post_returnInformation(request):
    cpID = request.POST.get('couponID',0)
    u_id = request.POST.get('userID')
    if u_id=='':
        return JsonResponse({'errno':'user no exist'})
    isLike = 0
    #查看该优惠券是否已被关注
    likeList = Couponlist.objects.get(userid=u_id,stat='like')
    if Listitem.objects.filter(listid=likeList.listid,couponid=cpID).exists():
        isLike = 1
    if cpID == 0 :
        return JsonResponse({'error':'优惠券不存在'})
    limitResult = Limit.objects.filter(couponid = cpID).values('content')
    LResult = []
    for limit in limitResult:
        LResult.append(limit)
    checklist = Listitem.objects.filter(couponid=cpID)
    checkUserid = 0
    for each in checklist:
        listID = each.listid.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            checkUserid = listStat.userid.id
    Seller = User.objects.filter(pk=checkUserid).values('id','nickname','gender','avatar')
    SResult = []
    for seller in Seller:
        SResult.append(seller)
    brandID = Coupon.objects.get(couponid=cpID).brandid.brandid
    brandResult = Brand.objects.filter(brandid=brandID).values('name','address')
    BResult = []
    for b in brandResult:
        BResult.append(b)
    return JsonResponse({'brand': BResult, 'limit': LResult, 'seller': SResult,'isLike':isLike})


#返回出售者卖过的、正在卖的优惠券
def post_sellerInformation(request):
    sellerID = request.POST.get('sellerID')
    sellerOnSaleList = Couponlist.objects.get(userid=sellerID,stat = 'onSale').listid
    sellerSoldList = Couponlist.objects.get(userid=sellerID,stat='Sold').listid
    onSaleList =[]
    soldList = []
    sellerOnSaleListitem = Listitem.objects.filter(listid=sellerOnSaleList)
    if sellerOnSaleListitem.exists():
        for each in sellerOnSaleListitem:
            onSaleCoupon = Coupon.objects.filter(couponid=each.couponid.couponid).values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in onSaleCoupon:
                onSaleList.append(i)
    sellerSoldListitem = Listitem.objects.filter(listid = sellerSoldList)
    if sellerSoldListitem.exists():
        for each in sellerSoldListitem:
            soldCoupon = Coupon.objects.filter(couponid=each.couponid.couponid).values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in soldCoupon:
                soldList.append(i)
    return JsonResponse({'onSale':onSaleList,'sold':soldList})


#通过优惠券ID查询所有者
def post_ownerDetailForAndroid(request):
    cpID = request.POST.get('couponID',0)
    checklistitem = Listitem.objects.filter(couponid=cpID)
    checklistID = checklistitem.values('listid')
    checkCouponlist = Couponlist.objects.filter(listid=checklistID).filter(stat='onSale')
    checkUserid =  checkCouponlist.values('userid')
    try:
        result = User.objects.filter(id=checkUserid)
    except User.DoesNotExist:
        return JsonResponse({'error':'用户不存在'})
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata,content_type='application/json')


#购买
def post_buyCoupon(request):
    cpID = request.POST.get('couponID',0)
    u_id = request.POST.get('userID',0)
    #检查优惠券是否存在
    coupon = models.Coupon.objects.get(couponid=cpID)
    if coupon.stat != 'onSale':
        return JsonResponse({'errno': 1, 'message': '优惠券已下架'})
    #检查用户UCoin
    buyerUCoin = models.User.objects.get(id=u_id).ucoin
    if buyerUCoin < coupon.listprice:
        return JsonResponse({'errno': 1, 'message': 'UCoin不足以支付'})
    #修改优惠券stat信息
    Coupon.objects.filter(couponid=cpID).update(stat = 'store')
    #将优惠券从拥有者的OnSale list、own list中删除并加入sold list中
    checklist = Listitem.objects.filter(couponid=cpID)
    sellerID = 0
    for each in checklist:
        listID = each.listid.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            sellerID = listStat.userid.id
    ownerOnsaleList = Couponlist.objects.get(userid=sellerID,stat='onSale').listid
    ownerOwnList = Couponlist.objects.get(userid = sellerID,stat = 'own').listid
    ownerSoldList = Couponlist.objects.get(userid=sellerID,stat='sold')
    Listitem.objects.filter(couponid=cpID).filter(listid=ownerOnsaleList).delete()
    Listitem.objects.filter(couponid=cpID).filter(listid=ownerOwnList).delete()
    Listitem.objects.create(couponid = coupon,listid=ownerSoldList)
    #将优惠券加入购买者的brought list和own list中
    buyerBroughtList = Couponlist.objects.get(userid=u_id,stat = 'brought')
    buyerOwnList = Couponlist.objects.get(userid=u_id,stat='own')
    Listitem.objects.create(couponid= coupon,listid = buyerBroughtList)
    Listitem.objects.create(couponid = coupon,listid = buyerOwnList)
    #修改用户UCoin
    seller = User.objects.get(id=sellerID)
    userUcoin = buyerUCoin-coupon.listprice
    User.objects.filter(id=u_id).update(ucoin = userUcoin)
    sellerUcoin = seller.ucoin + coupon.listprice
    User.objects.filter(id = seller.id).update(ucoin = sellerUcoin)
    #生成通知拥有者的message
    createMessage('上架的优惠券被购买', cpID)
    #生成通知关注者的message
    createMessage('关注的优惠券已被购买', cpID)
    likeList = models.Listitem.objects.filter(couponid=cpID)
    for lists in likeList:
        temp = models.Couponlist.objects.get(listid=lists.listid.listid)
        if temp.stat == 'like':
            lists.delete()
    return JsonResponse({'errno': 0, 'message': '购买成功'})


#关注优惠券接口
def post_likeCoupon(request):
    cpID = request.POST.get('couponID',0)
    u_ID = request.POST.get('userID',0)
    CouponObj = Coupon.objects.get(pk = cpID)
    userLikeList = Couponlist.objects.get(userid=u_ID,stat='like')
    if Listitem.objects.filter(couponid = cpID,listid = userLikeList).exists():
        return JsonResponse({'result':'already like'})
    Listitem.objects.create(couponid = CouponObj,listid = userLikeList)
    return JsonResponse({'result':'success'})


#消息发送接口
def post_sendMessage(request):
    userID = request.POST.get('userID',0)
    msg = Message.objects.filter(userid=userID)
    msgdata = serializers.serialize("json",msg,fields = ('messageid','content','time','messagecat','couponid'))
    return HttpResponse(msgdata,content_type="application/json")


#修改密码接口
def post_updatePassword(request):
    newPassword = request.POST.get('password',0)
    phone = request.POST.get('phoneNum',0)
    newPassword = encryption(newPassword)
    if newPassword == User.objects.get(phonenum = phone).password:
        return JsonResponse({'result':'New Password is the same as old'})
    User.objects.filter(phonenum=phone).update(password = newPassword)
    return JsonResponse({'result':'success'})


#判断手机/邮箱是否存在
def post_checkUsername(request):
    username = request.POST.get('username')
    if '@' in username:
        if User.objects.filter(email=username).exists():
            return JsonResponse({'result':'0'})
        return JsonResponse({'result':'1'})
    else:
        if User.objects.filter(phonenum=username).exists():
            return JsonResponse({'result': '0'})
        return JsonResponse({'result': '1'})


#获取个人信息
def post_getUserInformation(request):
    u_id = request.POST.get('userID')
    result = User.objects.filter(pk = u_id)
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata,content_type='application/json')


#修改个人信息
def post_updateUserInformation(request):
    u_id = request.POST.get('userID')
    newNickname = request.POST.get('nickname')
    newGender = request.POST.get('gender')
    User.objects.filter(pk = u_id).update(nickname = newNickname)
    User.objects.filter(pk = u_id).update(gender = newGender)
    return JsonResponse({'result':'success'})
    pass


#修改头像
def post_updateAvatar(request):
    #uf = userForm(request.POST,request.FILES)
    #u_id = uf.cleaned_data['userID']
    #headImg = uf.cleaned_data['avatar']
    u_id = request.POST.get('userID',0)
    headImg = request.FILES.get('imgFile',None)
    user = User.objects.get(id = u_id)
    if User.objects.filter(id = u_id).exists():
        user.avatar = headImg
        user.save()
    return JsonResponse({'errno': '0', 'message': '成功'})


#修改手机/邮箱
def post_updatePhonenumOrEmail(request):
    u_id = request.POST.get('userID')
    NewPhonenumOrEmail = request.POST.get('username')
    userObj = User.objects.get(pk = u_id)
    if  '@'in NewPhonenumOrEmail:
        if userObj.phonenum == None:
            userObj.email = NewPhonenumOrEmail
            userObj.save()
            return JsonResponse({'result':'success'})
        else:
            return JsonResponse({'result':'该账户使用手机注册'})
    else:
        if userObj.email == None:
            userObj.phonenum = NewPhonenumOrEmail
            userObj.save()
            return JsonResponse({'result':'success'})
        else:
            return JsonResponse({'result':'该账户使用邮箱注册'})


#添加优惠券
def post_addCoupon(request):
    u_id = request.POST.get('userID')
    brandName = request.POST.get('brand')
    cat = request.POST.get('category')
    expiredTime = datetime.datetime.strptime(request.POST.get('expiredTime'), '%Y-%m-%d')
    listPrice = request.POST.get('listPrice')
    product = request.POST.get('product')
    discount = request.POST.get('discount')
    stat = request.POST.get('stat', 'store')
    pic = request.POST.get('pic', DEFAULT_PIC)

    #估值
    value = 0
    # 判断brand是否存在
    if not models.Brand.objects.filter(name=brandName).exists():
        brandID = models.Brand(brandid=None, name=brandName)
    else:
        brandID = models.Brand.objects.get(name=brandName)

    # 获取catID
    if not models.Category.objects.filter(name=cat).exists():
        return JsonResponse({'errno': 1, 'message': 'category not found'})
    else:
        catID = models.Category.objects.get(name=cat)

    user = models.User.objects.get(id=u_id)
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


#获取"我买过的"优惠券
def post_getBoughtList(request):
    u_id = request.POST.get('userID')
    boughtList = []
    if User.objects.filter(id=u_id).exists():
        broughtListID = Couponlist.objects.get(userid=u_id, stat='brought').listid
        broughtListitem = Listitem.objects.filter(listid=broughtListID)
        for each in broughtListitem:
            couponList = Coupon.objects.filter(couponid=each.couponid.couponid).values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in couponList:
                boughtList.append(i)
        return JsonResponse({'boughtList':boughtList})
    else:
        return JsonResponse({'result':'user not exist'})


#获取我拥有的优惠券
def post_getOwnList(request):
    u_id = request.POST.get('userID')
    onSaleList = []
    storeList = []
    usedList = []
    if User.objects.filter(id=u_id).exists():
        ownListID = Couponlist.objects.get(userid=u_id,stat='own').listid
        ownListitem = Listitem.objects.filter(listid=ownListID)
        for each in ownListitem:
            tmpOnSalelist = Coupon.objects.filter(couponid=each.couponid.couponid,stat='onSale').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in tmpOnSalelist:
                onSaleList.append(i)
            tmpStoreList = Coupon.objects.filter(couponid=each.couponid.couponid,stat = 'store').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in tmpStoreList:
                storeList.append(i)
            tmpUsedList = Coupon.objects.filter(couponid=each.couponid.couponid,stat='used').values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in tmpUsedList:
                usedList.append(i)
        return JsonResponse({'onSaleList':onSaleList,'storeList':storeList,'usedList':usedList})
    else:
        return JsonResponse({'result':'user not exist'})


#获取我卖出的优惠券
def post_getSoldList(request):
    u_id = request.POST.get('userID')
    soldList = []
    if User.objects.filter(id = u_id).exists():
        soldListID = Couponlist.objects.get(userid=u_id,stat='sold').listid
        soldListitem = Listitem.objects.filter(listid = soldListID)
        for each in soldListitem:
            couponList = Coupon.objects.filter(couponid=each.couponid.couponid).values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in couponList:
                soldList.append(i)
        return JsonResponse({'soldList':soldList})
    else:
        return JsonResponse({'result':'user not exist'})


#获取我用过的优惠券
def post_getUsedCoupon(request):
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
        return JsonResponse({'result':'user not exist'})


#充值
def post_buyUcoin(request):
    pass


#獲取關注列表
def post_getLikeList(request):
    u_id = request.POST.get('userID')
    likeList = []
    if User.objects.filter(id = u_id).exists():
        likeListID = Couponlist.objects.get(userid=u_id,stat='like').listid
        likeListitem = Listitem.objects.filter(listid = likeListID)
        for each in likeListitem:
            couponList = Coupon.objects.filter(couponid=each.couponid.couponid).values('couponid', 'product', 'listprice', 'value', 'expiredtime','discount')
            for i in couponList:
                likeList.append(i)
        return JsonResponse({'likeList':likeList})
    else:
        return JsonResponse({'result':'user not exist'})


#上架下架已拥有的优惠券  还需要创建message
def post_changeCouponStat(request):
    cpID = request.POST.get('couponID')
    newStat = request.POST.get('stat')
    cp = Coupon.objects.get(couponid=cpID)
    if newStat=='onSale':
        if cp.stat == 'onSale':
            return JsonResponse({'errno':'1','message':'优惠券已上架'})
        elif cp.stat == 'store':
            cp.stat = 'onSale'
            cp.save()
            return JsonResponse({'errno':'0','message':'优惠券上架成功'})
        else:
            return JsonResponse({'errno':'2','message':'优惠券状态错误'})
    elif newStat == 'store':
        if cp.stat == 'store':
            return JsonResponse({'errno':'1','message':'优惠券已下架'})
        elif cp.stat == 'onSale':
            cp.stat = 'store'
            cp.save()
            return JsonResponse({'errno':'0','message':'优惠券下架成功'})
        else:
            return JsonResponse({'errno':'2','message':'优惠券状态错误'})
    else:
        return JsonResponse({'errno':'3','message':'提交的状态错误'})


#主页的推荐 未完成
def post_homepageCoupon(request):
    u_id = request.POST.get('userID')
    #根据用户最近购买的优惠券种类中关注度最高的进行推荐
    couponCat_1 = Coupon.objects.filter(catid=1).order_by()[0:5]#生活百货




#搜索栏的推荐 未完成
def post_searchCoupon(request):
    pass




