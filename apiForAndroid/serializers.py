from rest_framework import serializers
from UHuiWebApp.models import *
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('ID','username','nickname','password','phoneNum','gender','avatar','email')

class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = ('brandID','name','address')

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('catID','name')

class couponSerializer(serializers.ModelSerializer):
    class Meta:
        model = coupon
        fields =('couponID','brandID','catID','listPrice','value','product','stat')

class couponListSerializer(serializers.ModelSerializer):
    class Meta:
        model = couponList
        fields = ('listID','stat','userID')

class limitSerializer(serializers.ModelSerializer):
    class Meta:
        model = limit
        fields = ('couponID','content')

class listItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = listItem
        fields =('listID','couponID')

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ('messageID','useID','content','time','messageCat')
