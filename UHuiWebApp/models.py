# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
