#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/2下午3:28
# @Author :刘佩
# @Email  :2092357412@qq.com
# @File   :excel.py

import django
import os
import sys
import xlrd



# 导入django环境
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'USMP.settings')
sys.path.insert(0, BASE_DIR)
django.setup()


from app01.models import Producesan,Producenas,Testsan,Testnas

def get_sheet_names(path):
    """
    打开表格,拿到所有的工作薄名称
    :param path: 表格路径
    :return:
    """
    wb = xlrd.open_workbook(filename=path)
    sheet_names = wb.sheet_names()
    return sheet_names


def open_excel(path, sheet_name):
    """
    按工作薄名称打开
    :param path: 表格路径
    :param sheet_name: 工作薄名称
    :return:
    """
    wb = xlrd.open_workbook(filename=path)
    wb_data = wb.sheet_by_name(sheet_name)
    return wb_data


def get_model_data(wb_data, model):
    """

    :param wb_data: 获取的表格数据
    :param model: 模型名称
    :return:
    """
    rows = wb_data.nrows
    # 拿到模型所有的字段
    keys = [field.attname for field in model._meta.fields]
    keys.remove('id')
    result = []
    for row in range(1, rows):
        dict = {}
        for key, value in zip(keys, wb_data.row_values(row)):
            dict[key] = value
        result.append(dict)
    return result


def data_to_db(data, model):
    """
    数据存入MySQL
    :param data: 字典数据
    :param model: 模型名称
    :return:
    """
    print len(data)
    objs = [model(**obj) for obj in data]
    try:
        # 批量插入
        model.objects.bulk_create(objs)
    except Exception as e:
        print e
        for obj in objs:
            # 一条条插入
            try:
                obj.save()
            except Exception as e1:
                print e1


if __name__ == '__main__':

    path = '/home/liu/Downloads/info.xlsx'

    # 拿到表格所有的工作薄名称
    # sheet_names = get_sheet_names(path)

    wb_data = open_excel(path, u'生产NAS')
    data = get_model_data(wb_data, Producenas)
    data_to_db(data, Producenas)






# def open_excel(file_path, sheet_name):
#     """
#     打开excel表格
#     :param file_path: 表格路径
#     :param sheet_name: 工作薄名程
#     :return:
#     """
#     wb = xlrd.open_workbook(filename=file_path)
#     wb_data = wb.sheet_by_name(sheet_name)
#     return wb_data
#
#
# def get_model_data(wb_data):
#     """
#     获取生产SAN数据
#     :param data:
#     :return:
#     """
#     rows = wb_data.nrows
#     # 拿到模型字段名称
#     keys = [filed.attname for filed in Producesan._meta.fields]
#     keys.remove('id')
#     result = []
#     for row in range(1, rows):
#         dict = {}
#         for key, value in zip(keys, wb_data.row_values(row)):
#             dict[key] = value
#         result.append(dict)
#     return result
#
#
# def data_to_db(data):
#     """
#     生产SAN数据存入MySQL
#     :param data: 字典数据
#     :return:
#     """
#     objs = [Producesan(**obj) for obj in data]
#     try:
#         # 批量插入
#         Producesan.objects.bulk_create(objs)
#     except Exception as e:
#         print e
#         for obj in objs:
#             # 一条条插入
#             obj.save()
#
#
# if __name__ == '__main__':
#
#     path = '/home/liu/Downloads/info.xlsx'
#     # 生产SAN数据
#     producesan_wb_data = open_excel(path,u'生产SAN')
#     producesan_data = get_model_data(producesan_wb_data)
#     data_to_db(producesan_data)
