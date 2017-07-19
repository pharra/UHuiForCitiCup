# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UHuiWebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageid', models.CharField(db_column='messageID', max_length=16, primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=128, null=True)),
                ('time', models.DateField(blank=True, null=True)),
                ('messagecat', models.CharField(blank=True, db_column='messageCat', max_length=10, null=True)),
                ('hasread', models.IntegerField(db_column='hasRead')),
                ('hassend', models.IntegerField(db_column='hasSend')),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Messege',
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='coupon',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='couponlist',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='limit',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='listitem',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]
