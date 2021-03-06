# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brandid', models.AutoField(db_column='brandID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'brand',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catid', models.AutoField(db_column='catID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('couponid', models.CharField(db_column='couponID', max_length=16, primary_key=True, serialize=False)),
                ('listprice', models.DecimalField(blank=True, db_column='listPrice', decimal_places=0, max_digits=10, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('product', models.CharField(blank=True, max_length=16, null=True)),
                ('discount', models.CharField(blank=True, max_length=16, null=True)),
                ('stat', models.CharField(blank=True, max_length=7, null=True)),
            ],
            options={
                'db_table': 'coupon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Couponlist',
            fields=[
                ('listid', models.AutoField(db_column='listID', primary_key=True, serialize=False)),
                ('stat', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'couponlist',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'limit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Messege',
            fields=[
                ('messegeid', models.CharField(db_column='messegeID', max_length=16, primary_key=True, serialize=False)),
                ('userid', models.CharField(blank=True, db_column='userID', max_length=16, null=True)),
                ('content', models.CharField(blank=True, max_length=128, null=True)),
                ('time', models.DateField(blank=True, null=True)),
                ('messagecat', models.CharField(blank=True, db_column='messageCat', max_length=10, null=True)),
            ],
            options={
                'db_table': 'messege',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=16, primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('phonenum', models.CharField(blank=True, db_column='phoneNum', max_length=11, null=True, unique=True)),
                ('gender', models.CharField(max_length=1)),
                ('avatar', models.CharField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(blank=True, max_length=32, null=True, unique=True)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Listitem',
            fields=[
                ('couponid', models.ForeignKey(db_column='couponID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='UHuiWebApp.Coupon')),
            ],
            options={
                'db_table': 'listitem',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='limit',
            name='couponid',
            field=models.ForeignKey(blank=True, db_column='couponID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UHuiWebApp.Coupon'),
        ),
        migrations.AddField(
            model_name='couponlist',
            name='userid',
            field=models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.DO_NOTHING, to='UHuiWebApp.User'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='brandid',
            field=models.ForeignKey(blank=True, db_column='brandID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UHuiWebApp.Brand'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='catid',
            field=models.ForeignKey(blank=True, db_column='catID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UHuiWebApp.Category'),
        ),
        migrations.AddField(
            model_name='listitem',
            name='listid',
            field=models.ForeignKey(db_column='listID', on_delete=django.db.models.deletion.DO_NOTHING, to='UHuiWebApp.Couponlist'),
        ),
        migrations.AlterUniqueTogether(
            name='listitem',
            unique_together=set([('couponid', 'listid')]),
        ),
    ]
