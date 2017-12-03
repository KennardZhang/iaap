# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_printer_page_ranges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='host_name',
            field=models.CharField(blank=True, help_text='主机名', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='page_ranges',
            field=models.CharField(help_text='页面范围命令', max_length=128),
        ),
        migrations.AlterField(
            model_name='printer',
            name='port',
            field=models.IntegerField(blank=True, help_text='端口', null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='username',
            field=models.CharField(blank=True, help_text='用户名', max_length=128, null=True),
        ),
    ]
