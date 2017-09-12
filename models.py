# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    areaid = models.CharField(db_column='areaID', primary_key=True, max_length=128)  # Field name made lowercase.
    x = models.CharField(db_column='X', max_length=45, blank=True, null=True)  # Field name made lowercase.
    y = models.CharField(db_column='Y', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brand(models.Model):
    brandid = models.AutoField(db_column='brandID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=16)
    areaid = models.ForeignKey(Area, models.DO_NOTHING, db_column='areaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand'


class Category(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'category'


class Companycoupon(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=4)  # Field name made lowercase.
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='brandID')  # Field name made lowercase.
    catid = models.ForeignKey(Category, models.DO_NOTHING, db_column='catID')  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.CharField(max_length=16)
    discount = models.CharField(max_length=16)
    pic = models.CharField(max_length=128)
    expiredtime = models.DateField(db_column='expiredTime')  # Field name made lowercase.
    remain = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'companycoupon'


class Coupon(models.Model):
    couponid = models.CharField(db_column='couponID', primary_key=True, max_length=16)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='brandID')  # Field name made lowercase.
    catid = models.ForeignKey(Category, models.DO_NOTHING, db_column='catID')  # Field name made lowercase.
    listprice = models.DecimalField(db_column='listPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    value = models.ForeignKey('Valueset', models.DO_NOTHING, db_column='value')
    product = models.CharField(max_length=16, blank=True, null=True)
    discount = models.CharField(max_length=16)
    pic = models.CharField(max_length=128, blank=True, null=True)
    expiredtime = models.DateField(db_column='expiredTime')  # Field name made lowercase.
    onsale = models.IntegerField(db_column='onSale', blank=True, null=True)  # Field name made lowercase.
    expired = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    bought = models.DateField(blank=True, null=True)
    sold = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'
        unique_together = (('couponid', 'userid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Like(models.Model):
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', primary_key=True)
    cid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='cid')

    class Meta:
        managed = False
        db_table = 'like'
        unique_together = (('uid', 'cid'),)


class Limit(models.Model):
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'limit'
        unique_together = (('couponid', 'content'),)


class Message(models.Model):
    messageid = models.CharField(db_column='messageID', primary_key=True, max_length=16)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=128, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    messagecat = models.CharField(db_column='messageCat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hasread = models.IntegerField(db_column='hasRead')  # Field name made lowercase.
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID')  # Field name made lowercase.
    hassend = models.IntegerField(db_column='hasSend')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'message'


class User(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=16)  # Field name made lowercase.
    nickname = models.CharField(unique=True, max_length=32)
    phonenum = models.CharField(db_column='phoneNum', unique=True, max_length=11, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=1)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=32)
    email = models.CharField(unique=True, max_length=32, blank=True, null=True)
    ucoin = models.DecimalField(db_column='UCoin', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hasconfirm = models.IntegerField(db_column='hasConfirm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Valuecalculate(models.Model):
    vid = models.ForeignKey('Valueset', models.DO_NOTHING, db_column='vid', primary_key=True)
    listprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valuecalculate'


class Valueset(models.Model):
    vid = models.IntegerField(db_column='VID', primary_key=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valueset'
