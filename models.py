
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
    address = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Category(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=16)

    class Meta:
        managed = False
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
    pic = models.CharField(max_length=128, blank=True, null=True)
    expiredtime = models.DateField(db_column='expiredTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coupon'


class Couponlist(models.Model):
    listid = models.AutoField(db_column='listID', primary_key=True)  # Field name made lowercase.
    stat = models.CharField(max_length=7)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'couponlist'


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


class Limit(models.Model):
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit'


class Listitem(models.Model):
    listid = models.ForeignKey(Couponlist, models.DO_NOTHING, db_column='listID')  # Field name made lowercase.
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listitem'
        unique_together = (('couponid', 'listid'),)


class Message(models.Model):
    messageid = models.CharField(db_column='messageID', primary_key=True, max_length=16)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=128, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    messagecat = models.CharField(db_column='messageCat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hasread = models.IntegerField(db_column='hasRead')  # Field name made lowercase.
    couponid = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='couponID')  # Field name made lowercase.

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
    ucoin = models.IntegerField(db_column='UCoin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
