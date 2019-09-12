# encoding:utf-8

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from models import *
from app01.common.response import CommonResponse
from app01.common.superclass import SuperView
from app01.units.forms import get_excel
from app01.units.forms import get_select_data
from app01.units.forms import handle_get
from app01.units.forms import handle_post
from app01.units.forms import handle_delete
from app01.units.forms import handle_put


# Create your views here.
def produce_san(request):
    return render(request, 'producesan.html')


def produce_nas(request):
    return render(request, 'producenas.html')


def test_san(request):
    return render(request,'')


def test_nas(request):
    return render(request,'')


def test(request):
    return render(request, 'testdata.html')


class getProduceSan(SuperView):
    """生产SAN 增删改查"""

    def post(self, request):
        # 增加
        response = handle_post(request,Producesan)
        return JsonResponse(response)

    def delete(self, request):
        # 删除
        response = handle_delete(request, Producesan)
        return JsonResponse(response)

    def put(self, request):
        # 修改
        response = handle_put(request, Producesan)
        return JsonResponse(response)

    def get(self, request):
        # 查询
        response = handle_get(Producesan)
        return JsonResponse(response)


class getProduceNas(SuperView):
    """生产NAS 增删改查"""

    def post(self, request):
        # 增加
        response = handle_post(request,Producenas)
        return JsonResponse(response)

    def delete(self, request):
        # 删除
        response = handle_delete(request, Producenas)
        return JsonResponse(response)

    def put(self, request):
        # 修改
        response = handle_put(request, Producenas)
        return JsonResponse(response)

    def get(self, request):
        # 查询
        response = handle_get(Producenas)
        return JsonResponse(response)


def getDataInfo(request):
    """数据详情"""
    response = CommonResponse()
    edit_id = request.GET.get('edit_id')
    type = request.GET.get('type')
    try:
        if type == 'produce_san':
            data = Producesan.objects.get(id=edit_id)
        elif type == 'produce_nas':
            data = Producenas.objects.get(id=edit_id)

        response.data = model_to_dict(data)
        return JsonResponse(response.get)

    except Exception as e:
        # logger.error(e)
        response.status = 201
        response.msg = '数据展示出错..'
        return JsonResponse(response.get)


@csrf_exempt
def dataToExcel(request):
    """数据导出"""
    response = CommonResponse()
    type = request.POST.get('type')
    checkList = request.POST.get('checkList')

    try:
        if type == 'produce_san':
            producesan_list = get_select_data(checkList, Producesan)
            url = get_excel('produce_SAN', producesan_list, Producesan)

        elif type == 'produce_nas':
            producenas_list = get_select_data(checkList, Producenas)
            url = get_excel('produce_NAS', producenas_list, Producenas)

        response.url = url
        return JsonResponse(response.get)
    except Exception as e:
        # logger.error(e)
        print e
        response.status = 201
        response.mas = '导出失败,请检查错误日志'
        return JsonResponse(response.get)


class getTestSan(SuperView):
    """测试SAN数据增删改查"""

    pass


class getTestNas(SuperView):
    """测试NAS数据增删改查"""

    pass
