# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171203_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printjobs',
            name='is_printed',
        ),
        migrations.AddField(
            model_name='printjobs',
            name='payment',
            field=models.IntegerField(choices=[(1, '余额支付'), (2, '线上支付'), (99, '我是管理员')], default=1, help_text='支付方式'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printjobs',
            name='status',
            field=models.IntegerField(choices=[(0, '已完成'), (1, '未完成')], default=0, help_text='任务状态'),
            preserve_default=False,
        ),
    ]
