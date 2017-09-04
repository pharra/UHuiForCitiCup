from rest_framework import serializers
from UHuiWebApp.models import *
'''class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('ID','username','nickname','password','phoneNum','gender','avatar','email')

class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('brandID','name','address')

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('catID','name')

class couponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields =('couponID','brandID','catID','listPrice','value','product','stat')

# class couponListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Couponlist
#         fields = ('listID','stat','userID')

class limitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = ('couponID','content')

# class listItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Listitem
#         fields =('listID','couponID')

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('messageID','useID','content','time','messageCat')'''
