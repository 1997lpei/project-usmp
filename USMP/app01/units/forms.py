#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/9/3下午3:36
# @Author :刘佩
# @Email  :2092357412@qq.com
# @File   :forms.py

"""可复用功能函数"""
import json
import os

from django.http import QueryDict
from openpyxl import Workbook
import datetime

from django.forms import model_to_dict
from USMP import settings
from app01.common.response import CommonResponse


def save_file_path(file_name):
    """
    文件导出路径
    :param: file_name 存放文件夹名称
    :return:
    """

    time = datetime.datetime.today().date()
    path = os.path.join(settings.MEDIA_ROOT, str(time), file_name)
    if not os.path.exists(path):
        # 不存在则创建
        os.makedirs(path)

    name = datetime.datetime.today().strftime('%Y%m%d%H%M%S') + '.xlsx'
    file_path = os.path.join(path, name)
    return file_path


def get_dict_data(model_datas):
    """
    格式化数据
    :param model_datas: 查询到的列表数据
    :return:
    """
    data_list = []
    for model_data in model_datas:
        data_list.append(model_to_dict(model_data))
    response = CommonResponse()
    response.data = data_list
    return response.get


def get_excel(excel_name, data, model):
    """
    导出excel表
    :param excel_name 表存放的文件夹名称
    :param data: 查询到的数据
    :param model
    :return:
    """
    verbose_name = [field.verbose_name for field in model._meta.fields if field.attname != 'id']
    res = [field.attname for field in model._meta.fields if field.attname != 'id']

    r = []
    # 以列表嵌套的形式取出所有数据
    for i_dict in data:
        tmp = []
        for key in res:
            tmp.append(i_dict[key])
        r.append(tmp)

    wb = Workbook()
    sheet = wb.active
    # sheet.title = sheet_name
    # 写入表头
    sheet.append(verbose_name)
    for obj in r:
        # 导入数据
        sheet.append(obj)

    file_path = save_file_path(excel_name)
    wb.save(file_path)
    # 返回文件保存路径
    url = os.path.join(settings.MEDIA_URL, file_path.split(settings.MEDIA_URL)[-1])
    return url


    # wb = xlwt.Workbook()
    # sheet = wb.add_sheet(excel_name, cell_overwrite_ok=True)
    # today = datetime.datetime.today()
    # for i in xrange(len(data)):
    #     for j in xrange(len(data[i].values())):
    #         sheet.write(i, j, data[i].values()[j])
    # # 运行后会在当前目录生成一个.xls文件
    # # wb.save(str(today) + '.xls')
    # sio = StringIO.StringIO()
    # wb.save(sio)
    # sio.seek(0)
    # response = HttpResponse(sio.getvalue())
    # response['Content-Type'] = 'application/vnd.ms-excel'
    # response['Content-Disposition'] = 'attachment;filename=%s.xlsx'.format(str(today))
    # return response


def get_select_data(checkList,model):
    """
    获取要执行操作的数据
    :param checkList: 选中的数据id列表(json)
    :param model:  数据模型
    :return:
    """
    model_data_list = []
    # 转化为python数据类型
    checkList = json.loads(checkList)
    for id in checkList:
        model_data = model.objects.filter(pk=int(id))
        if model_data.first:
            # 以列表嵌套字典的形式返回
            model_data_list.append(model_to_dict(model_data.first()))
    return model_data_list


def handle_get(model):
    """
    查询操作
    :param model: 数据模型
    :return:
    """
    model_data = model.objects.all()
    response = get_dict_data(model_data)
    return response


def handle_delete(request,model):
    """
    删除操作
    :param request:
    :param model: 数据模型
    :return:
    """
    response = CommonResponse()
    put = QueryDict(request.body)
    checkList = put.get('checkList')
    # 转化为python数据类型
    checkList = json.loads(checkList)
    try:
        for id in checkList:
            model.objects.get(pk=int(id)).delete()
        response.msg = '删除成功'
    except Exception as e:
        # logger.error(e)
        response.msg = '删除失败,请检查错误日志'
        response.status = 201
    return response.get


def handle_put(request,model):
    """
    修改操作
    :param request:
    :param model: 数据模型
    :return:
    """
    response = CommonResponse()
    data = QueryDict(request.body)
    res = {k: v for k, v in data.items()}
    edit_id = res.get('id')
    try:
        model.objects.filter(id=edit_id).update(**res)
        response.msg = '修改成功'
    except Exception as e:
        # logger.error(e)
        response.msg = '修改失败,请检查错误日志'
        response.status = 201
    return response.get


def handle_post(request,model):
    """
    增加操作
    :param request:
    :param model: 数据模型
    :return:
    """
    response = CommonResponse()
    values = request.POST.get('values')
    try:
        # 以&切割,拿到参数
        value_list = values.split('&')
        for value in value_list:
            # 以|切割 去掉两边空格
            value = value.split('|')
            value = [x.strip() for x in value]
            # 拿到模型所有的字段
            res = [field.attname for field in model._meta.fields if field.attname != 'id']

            # 处理成字典数据
            res_dict = {res[i]: value[i] for i in range(len(res))}
            obj = model(**res_dict)
            obj.save()
        response.msg = '添加成功'
    except Exception as e:
        # logger.error(e)
        print e
        response.msg = '添加失败,请检查错误日志'
        response.status = 201

    return response.get




if __name__ == '__main__':
    pass
