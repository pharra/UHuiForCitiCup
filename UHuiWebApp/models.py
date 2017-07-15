# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


<<<<<<< HEAD
# Create your models here.
class user(models.Model):
    ID = models.CharField(max_length=16, primary_key=True, unique=True)
    username = models.CharField(max_length=16, unique=True)
    nickname = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    phoneNum = models.CharField(max_length=16, unique=True, null=True)
    gender_choice = (
        ('1', '男'),
        ('2', '女')
    )
    gender = models.CharField(max_length=2, choices=gender_choice)
    avatar = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=32, unique=True, null=True)


class brand(models.Model):
    brandID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)
    address = models.CharField(max_length=128, default="地址未录入", null=True)


class category(models.Model):
    catID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True)


class coupon(models.Model):
    couponID = models.CharField(max_length=16, primary_key=True)
    brandID = models.ForeignKey(brand, related_name="bID")
    catID = models.ForeignKey(category, related_name="cID")
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


class message(models.Model):
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
=======
class Brand(models.Model):
    brandid = models.AutoField(db_column='brandID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=16)
    address = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brand'


class Category(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=16)

    class Meta:
        managed = True
        db_table = 'category'


class Coupon(models.Model):
    couponid = models.CharField(db_column='couponID', primary_key=True, max_length=16)  # Field name made lowercase.
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='brandID', blank=True, null=True)  # Field name made lowercase.
    catid = models.ForeignKey(Category, models.DO_NOTHING, db_column='catID', blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='listPrice', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    product = models.CharField(max_length=16, blank=True, null=True)
    discount = models.CharField(max_length=16, blank=True, null=True)
    stat = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'coupon'


class Couponlist(models.Model):
    listid = models.AutoField(db_column='listID', primary_key=True)  # Field name made lowercase.
    stat = models.CharField(max_length=7)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'couponlist'
>>>>>>> origin/zww


class Limit(models.Model):
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'limit'


class Listitem(models.Model):
    listid = models.ForeignKey(Couponlist, models.DO_NOTHING, db_column='listID')  # Field name made lowercase.
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'listitem'
        unique_together = (('couponid', 'listid'),)


class Messege(models.Model):
    messegeid = models.CharField(db_column='messegeID', primary_key=True, max_length=16)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=128, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    messagecat = models.CharField(db_column='messageCat', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'messege'


class User(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=16)  # Field name made lowercase.
    # username = models.CharField(unique=True, max_length=16)
    nickname = models.CharField(unique=True, max_length=32, blank=True, null=True)
    phonenum = models.CharField(db_column='phoneNum', unique=True, max_length=11, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=1)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
