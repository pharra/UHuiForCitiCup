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

def signUpForAndroid(request):
    pass

def loginForAndroid(request):
    pass

#搜索
def searchForAndroid(request):
    searchKeyWord = request.POST.get('keyWord',0)
    try:
        result = coupon.objects.filter(product__contains=searchKeyWord)
    except coupon.DoesNotExist:
        return HttpResponse(status = 404)

    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)

#点击种类进行查询
def selectCategoryForAndroid(request):
    selectCategory = request.POST.get('categoryID',0)
    try:
        result = coupon.objects.filter(catID=selectCategory)
    except coupon.DoesNotExist:
        return HttpResponse(status=404)

    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)

#查询优惠券详细信息
def couponDetailForAndroid(request):
    cpID = request.POST.get('couponID',0)
    try:
        result = coupon.objects.filter(couponID=cpID)
    except coupon.DoesNotExist:
        return HttpResponse(status=404)

    couponSeria = couponSerializer(result)
    return JSONResponse(couponSeria.data)
