# encoding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Producesan(models.Model):
    name = models.CharField(max_length=16, verbose_name='名称', null=True, blank=True)
    serial_number = models.CharField(max_length=16, verbose_name='序列号', null=True, blank=True)
    manage_ip = models.CharField(max_length=64, verbose_name='管理ip', null=True, blank=True)
    computer_room = models.CharField(max_length=16, verbose_name='机房', null=True, blank=True)
    frame = models.CharField(max_length=16, verbose_name='机架', null=True, blank=True)
    purpose = models.CharField(max_length=128, verbose_name='用途', null=True, blank=True)
    type = models.CharField(max_length=32, verbose_name='型号', null=True, blank=True)
    environmental = models.CharField(max_length=16, verbose_name='环境', null=True, blank=True)
    warranty_level = models.CharField(max_length=16, verbose_name='保修级别', null=True, blank=True)
    landing_mode = models.CharField(max_length=16, verbose_name='登陆方式', null=True, blank=True)
    subordinate_departments = models.CharField(max_length=32, verbose_name='所属部门', null=True, blank=True)
    produce_date = models.CharField(max_length=32, verbose_name='投产日期', null=True, blank=True)
    example_number = models.CharField(max_length=64, verbose_name='实例号', null=True, blank=True)
    examples = models.CharField(max_length=16, verbose_name='实例状', null=True, blank=True)
    instance_port = models.CharField(max_length=64, verbose_name='实例端口', null=True, blank=True)

    class Meta:
        """生产SAN"""
        db_table = 'produce_san'


class Producenas(models.Model):
    colony = models.CharField(max_length=32, verbose_name='集群', null=True, blank=True)
    nose = models.CharField(max_length=32, verbose_name='机头', null=True, blank=True)
    serial_number = models.CharField(max_length=64, verbose_name='序列号', null=True, blank=True)
    nose_manage_ip = models.CharField(max_length=64, verbose_name='机头管理ip', null=True, blank=True)
    colony_manage_ip = models.CharField(max_length=64, verbose_name='集群管理ip', null=True, blank=True)
    service_ip = models.CharField(max_length=128, verbose_name='服务ip', null=True, blank=True)
    computer_room = models.CharField(max_length=16, verbose_name='机房', null=True, blank=True)
    frame = models.CharField(max_length=16, verbose_name='机架', null=True, blank=True)
    purpose = models.CharField(max_length=128, verbose_name='用途', null=True, blank=True)
    type = models.CharField(max_length=32, verbose_name='型号', null=True, blank=True)
    environmental = models.CharField(max_length=16, verbose_name='环境', null=True, blank=True)
    warranty_level = models.CharField(max_length=16, verbose_name='保修级别', null=True, blank=True)
    landing_mode = models.CharField(max_length=16, verbose_name='登陆方式', null=True, blank=True)
    subordinate_departments = models.CharField(max_length=32, verbose_name='所属部门', null=True, blank=True)
    produce_date = models.CharField(max_length=32, verbose_name='投产日期', null=True, blank=True)


    class Meta:
        """生产NAS"""
        db_table = 'produce_nas'


class Testsan(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称', null=True, blank=True)
    serial_number = models.CharField(max_length=32, verbose_name='序列号', null=True, blank=True)
    manage_ip = models.CharField(max_length=64, verbose_name='管理ip', null=True, blank=True)
    computer_room = models.CharField(max_length=16, verbose_name='机房', null=True, blank=True)
    frame = models.CharField(max_length=16, verbose_name='机架', null=True, blank=True)
    purpose = models.CharField(max_length=128, verbose_name='用途', null=True, blank=True)
    type = models.CharField(max_length=32, verbose_name='型号', null=True, blank=True)
    environmental = models.CharField(max_length=16, verbose_name='环境', null=True, blank=True)
    warranty_level = models.CharField(max_length=16, verbose_name='保修级别', null=True, blank=True)
    landing_mode = models.CharField(max_length=16, verbose_name='登陆方式', null=True, blank=True)
    subordinate_departments = models.CharField(max_length=32, verbose_name='所属部门', null=True, blank=True)
    produce_date = models.CharField(max_length=32, verbose_name='投产日期', null=True, blank=True)

    class Meta:
        """测试SAN"""
        db_table = 'test_san'


class Testnas(models.Model):
    colony = models.CharField(max_length=32, verbose_name='集群', null=True, blank=True)
    nose = models.CharField(max_length=32, verbose_name='机头', null=True, blank=True)
    serial_number = models.CharField(max_length=64, verbose_name='序列号', null=True, blank=True)
    nose_manage_ip = models.CharField(max_length=64, verbose_name='机头管理ip', null=True, blank=True)
    colony_manage_ip = models.CharField(max_length=64, verbose_name='集群管理ip', null=True, blank=True)
    service_ip = models.CharField(max_length=256, verbose_name='服务ip', null=True, blank=True)
    computer_room = models.CharField(max_length=16, verbose_name='机房', null=True, blank=True)
    frame = models.CharField(max_length=16, verbose_name='机架', null=True, blank=True)
    purpose = models.CharField(max_length=128, verbose_name='用途', null=True, blank=True)
    type = models.CharField(max_length=32, verbose_name='型号', null=True, blank=True)
    environmental = models.CharField(max_length=16, verbose_name='环境', null=True, blank=True)
    warranty_level = models.CharField(max_length=16, verbose_name='保修级别', null=True, blank=True)
    landing_mode = models.CharField(max_length=16, verbose_name='登陆方式', null=True, blank=True)
    produce_date = models.CharField(max_length=32, verbose_name='投产日期', null=True, blank=True)
    class Meta:
        """测试NAS"""
        db_table = 'test_nas'
