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
    searchKeyWord = request.POST.get('keyWord',0)
    result = Coupon.objects.filter(product__contains=searchKeyWord).filter(stat='onSale')
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata, content_type="application/json")
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
    result = Coupon.objects.filter(pk=cpID)
    resultdata = serializers.serialize('json',result)
    return HttpResponse(resultdata, content_type="application/json")
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
    userLikeList = Couponlist.objects.get(userid=u_ID,stat='like').listid
    Listitem.objects.create(couponID = cpID,listID = userLikeList)
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
#修改密码
