from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
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
    else:
        user = models.User.objects.filter(phonenum=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(phonenum=u_name)
        uid = User.objects.get(phonenum=u_name).id

    psw = encryption(request.POST.get('password'))
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    if psw == password:
        response = JsonResponse({'result': 'success','userid':uid})
        return response
    else:
        return JsonResponse({'error': '密码错误'})
#搜索
def post_searchForAndroid(request):
    key = request.POST.get('keyWord',0)
    if not key:
        return {'result': "请输入关键词"}
    productResult = models.Coupon.objects.filter(product__contains=key, stat='onSale').values()
    result = []
    for coupon in productResult:
        result.append(coupon)
    brandIDResult = models.Brand.objects.filter(name__contains=key)
    for brand in brandIDResult:
        temp = models.Coupon.objects.filter(brandid=brand.brandid)
        if temp.exists():
            for info in temp.values():
                result.append(info)
        return JsonResponse({'coupons': result})
#点击种类进行查询
def post_selectCategoryForAndroid(request):
    selectCategory = request.POST.get('categoryID',0)
    result = Coupon.objects.filter(catID=selectCategory).filter(stat='onSale')
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata,content_type="application/json")
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
    for each in checklist:
        listID = each.listid.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            checkUserid = listStat.userid.id
    Seller = User.objects.filter(pk = checkUserid).values('nickname','avatar')
    SResult = []
    for seller in Seller:
        SResult.append(seller)
    brandID = Coupon.objects.get(couponid=cpID).brandid
    brandResult = Brand.objects.filter(brandid=brandID)
    BResult = []
    for b in brandResult:
        BResult.append(b)
    return JsonResponse({'coupon':CResult,'limit':LResult,'seller':SResult,'brand':BResult})
#返回使用限制、商家名以及出售者信息
def post_returnInformation(request):
    cpID = request.POST.get('couponID')
    if cpID == 0 :
        return JsonResponse({'error':'优惠券不存在'})
    limitResult = Limit.objects.filter(couponid = cpID).values('content')
    LResult = []
    for limit in limitResult:
        LResult.append(limit)
    checklist = Listitem.objects.filter(couponid=cpID)
    for each in checklist:
        listID = each.listid.listid
        listStat = models.Couponlist.objects.get(listid=listID)
        if listStat.stat == 'onSale':
            checkUserid = listStat.userid.id
    Seller = User.objects.filter(pk=checkUserid).values('nickname', 'avatar')
    SResult = []
    for seller in Seller:
        SResult.append(seller)
    brandID = Coupon.objects.get(couponid=cpID).brandid
    brandResult = Brand.objects.filter(brandid=brandID)
    BResult = []
    for b in brandResult:
        BResult.append(b)
    return JsonResponse({'brand': BResult, 'limit': LResult, 'seller': SResult})
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
#购买后修改优惠券信息
def post_buyCoupon(request):
    cpID = request.POST.get('couponID',0)
    u_id = request.POST.get('userID',0)
    cp = Coupon.objects.get(couponid=cpID)
    #检查优惠券是否存在
    coupon = models.Coupon.objects.get(couponid=cpID)
    if coupon.stat != 'onSale':
        return JsonResponse({'errno': 1, 'message': '优惠券已下架'})
    #检查用户UCoin
    buyerUCoin = models.User.objects.get(id=u_id).ucoin
    if buyerUCoin < coupon.listprice:
        return {'errno': 1, 'message': 'UCoin不足以支付'}
    #修改优惠券stat信息
    Coupon.objects.filter(couponid=cpID).update(stat = 'store')
    #将优惠券从拥有者的OnSale list、own list中删除并加入sold list中
    checklistID = Listitem.objects.get(couponid=cpID).listid
    ownerID = Couponlist.objects.get(listid=checklistID,stat = 'onSale').userid
    ownerOnsaleList = Couponlist.objects.get(userid=ownerID,stat='onSale').listid
    ownerOwnList = Couponlist.objects.get(userid = ownerID,stat = 'own').listid
    ownerSoldList = Couponlist.objects.get(userid=ownerID,stat='sold').listid
    Listitem.objects.filter(couponid=cpID).filter(listid=ownerOnsaleList).delete()
    Listitem.objects.filter(couponid=cpID).filter(listid=ownerOwnList).delete()
    Listitem.objects.create(couponID = cpID,listID=ownerSoldList)
    #将优惠券加入购买者的brought list和own list中
    buyerBroughtList = Couponlist.objects.get(userid=u_id,stat = 'brought').listid
    buyerOwnList = Couponlist.objects.get(userid=u_id,stat='own').listid
    Listitem.objects.create(couponID = cpID,listID = buyerBroughtList)
    Listitem.objects.create(couponID = cpID,listID = buyerOwnList)
    #生成通知拥有者的message
    pass
    #生成通知关注者的message
    pass
    return JsonResponse({'result':'success'})
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
    userID = request.POST.get('userID',0)
    newPassword = encryption(newPassword)
    if newPassword == User.objects.get(pk = userID).password:
        return JsonResponse({'result':'New Password is the same as old'})
    User.objects.filter(pk=userID).update(password = newPassword)
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
    pass
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



