from django.db import models


# Create your models here.
class user(models.Model):
    ID = models.CharField(max_length=16, primary_key=True, unique=True)
    username = models.CharField(max_length=16, unique=True)
    nickname = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    phoneNum = models.CharField(max_length=16, unique=True)
    gender_choice = (
        ('1', '男'),
        ('2', '女')
    )
    gender = models.CharField(max_length=2, choices=gender_choice)
    avatar = models.CharField(max_length=128, null=True)


class brand(models.Model):
    brandID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)
    address = models.CharField(max_length=128, default="地址未录入", null=True)


class category(models.Model):
    catID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)


class coupon(models.Model):
    couponID = models.CharField(max_length=16, primary_key=True)
    brandID = models.ForeignKey(brand)
    catID = models.ForeignKey(category)
    listPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    product = models.CharField(max_length=16, null=True)
    choice_stat = (
        ('1', 'onSale'),
        ('2', 'expired'),
        ('3', 'used'),
        ('4', 'store')
    )
    stat = models.CharField(max_length=16, choices=choice_stat, default='store')


class couponList(models.Model):
    listID = models.AutoField(primary_key=True)
    choice_stat = (
        ('1', 'own'),
        ('2', 'sold'),
        ('3', 'brought'),
        ('4', 'onSell'),
        ('5', 'like')
    )
    stat = models.CharField(max_length=8, choices=choice_stat, null=True)
    userID = models.ForeignKey(user)


class limit(models.Model):
    couponID = models.ForeignKey(coupon)
    content = models.CharField(max_length=128)


class listItem(models.Model):
    listID = models.ForeignKey(couponList, primary_key=True)
    couponID = models.ForeignKey(coupon, primary_key=True)


class massage(models.Model):
    messageID = models.CharField(max_length=16, primary_key=True)
    userID = models.CharField(max_length=16, null=True)
    content = models.CharField(max_length=128, null=True)
    time = models.TimeField(null=True)
    messageCat_choice = (
        ('1', '上架的优惠券被购买'),
        ('2', '上架的优惠券即将过期'),
        ('3', '上架的优惠券已过期'),
        ('4', '关注的优惠券即将过期'),
        ('5', '关注的优惠券已被购买'),
        ('6', '我的优惠券即将过期'),
        ('7', '我的优惠券已过期'),
        ('8', '系统通知')
    )
    messageCat = models.CharField(max_length=32, choices=messageCat_choice, null=True)


