from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from UHuiWebApp.models import *
from apiForAndroid.serializers import *
from UHuiWebApp.views import *
#返回json数据
class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
# Create your views here.

def post_signUpForAndroid(request):
    return post_signUp(request)


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
        response = JSONResponse({'result': 'success','userid':uid})
        return response
    else:
        return JsonResponse({'error': '密码错误'})
#搜索
def searchForAndroid(request):
    searchKeyWord = request.POST.get('keyWord',0)
    try:
        result = Coupon.objects.filter(product__contains=searchKeyWord).filter(stat='onSale')
    except Coupon.DoesNotExist:
        return JSONResponse({'error':'内容不存在'})
    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)

#点击种类进行查询
def selectCategoryForAndroid(request):
    selectCategory = request.POST.get('categoryID',0)
    try:
        result = Coupon.objects.filter(catID=selectCategory).filter(stat='onSale')
    except Coupon.DoesNotExist:
        return JSONResponse({'error': '内容不存在'})
    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)

#查询优惠券详细信息
def couponDetailForAndroid(request):
    cpID = request.POST.get('couponID',0)
    try:
        result = Coupon.objects.filter(couponID=cpID)
    except Coupon.DoesNotExist:
        return JSONResponse({'error': '内容不存在'})
    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)

#通过优惠券ID查询所有者
def ownerDetailForAndroid(request):
    cpID = request.POST.get('couponID',0)
    checklistitem = Listitem.objects.filter(couponid=cpID)
    checklistID = checklistitem.values('listid')
    checkCouponlist = Couponlist.objects.filter(listid=checklistID).filter(stat='OnSale')
    checkUserid =  checkCouponlist.values('userid')
    try:
        result = User.objects.filter(id=checkUserid)
    except User.DoesNotExist:
        return JsonResponse({'error':'用户不存在'})
    UserSeria = userSerializer(result)
    return JSONResponse(UserSeria.data)

#购买后修改优惠券信息
def buyCoupon(request):
    cpID = request.POST.get('couponID',0)
    userID = request.POST.get('userID',0)
    cp = Coupon.objects.get(couponid=cpID)
    #修改优惠券stat信息
    Coupon.objects.filter(couponid=cpID).update(stat = 'store')
    #将优惠券从拥有者的OnSale list、own list中删除并加入sold list中
    #找到拥有者各个list对应的listID
    checklistitem = Listitem.objects.filter(couponid=cpID)
    checklistID = checklistitem.values('listid')
    checkCouponlist = Couponlist.objects.filter(listid=checklistID).filter(stat='OnSale')
    ownID = checkCouponlist.values('userid')
    #将优惠券加入购买者的brought list和own list中
    pass

#消息发送接口
def sendMessage(request):
    userID = request.POST.get('userID',0)
    msg = Message.objects.filter(userid=userID)
    msgSeria = messageSerializer(msg)
    return JSONResponse(msgSeria.data)

#消息生成接口
def createMessage():
    pass
