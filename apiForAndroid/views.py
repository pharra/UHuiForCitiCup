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
    else:
        user = models.User.objects.filter(phonenum=u_name).count()
        if user == 0:
            return JsonResponse({'error': '用户不存在'})
        pswObj = models.User.objects.get(phonenum=u_name)

    psw = encryption(request.POST.get('password'))
    password = bytes.decode(pswObj.password.encode("UTF-8"))
    if psw == password:
        response = JSONResponse({'result': 'success'})
        return response
    else:
        return JsonResponse({'error': '密码错误'})
#搜索
def searchForAndroid(request):
    searchKeyWord = request.POST.get('keyWord',0)
    try:
        result = Coupon.objects.filter(product__contains=searchKeyWord)
    except Coupon.DoesNotExist:
        return JSONResponse({'error':'内容不存在'})
    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)

#点击种类进行查询
def selectCategoryForAndroid(request):
    selectCategory = request.POST.get('categoryID',0)
    try:
        result = Coupon.objects.filter(catID=selectCategory)
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

