# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from index.models import *
import json
import os
import logging
from django.db.models import Q
from iostat import iostat
# Create your views here.
logger = logging.getLogger('django')
# 返回首页
def index(request):
    return render(request, 'index.html')

# 返回欢迎页
def welcome(request):
    return render(request, 'welcome.html')

# 刷新存储配置
def goToUpdateStorageDb(request):
    try:
        if request.method == "POST":
            path = "initdb/uploadfiles/storageconf/"
            if not os.path.exists(path):
                os.makedirs(path)
            for file in request.FILES.getlist('selectFile') :
                filename = str(file)
                logger.info('selectFile : %s' % filename)
                with open(path+filename,'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            logger.info('storage conf has been uploaded to /usr/local/apache2/htdocs/USMP/initdb/uploadfiles/storageconf/')
    except Exception as e:
        logger.error(e)
    return render(request, 'updatestorageconf.html')

# 刷新nas配置
def goToUpdateNasDb(request):
    return render(request, 'updatenasconf.html')

# 更新左侧导航栏
@csrf_exempt
def initIndexBar(request):
    nas_cluster_list = []
    hds_storage_list = []
    nas_cluster_result = NasCluster.objects.all().order_by('name').values('name').distinct()
    ldev_list_result = LdevList.objects.all().order_by('serial').values('serial').distinct()
    for cluster in nas_cluster_result:
        nas_cluster_list.append(cluster['name'])
    for storage in ldev_list_result:
        hds_storage_list.append(storage['serial'])
    result_list = {"nas_cluster_list": nas_cluster_list, "hds_storage_list": hds_storage_list}
    return HttpResponse(json.dumps(result_list), content_type='application/json')

# 删除存储
def delstorageinfo(request):
    storage_serial = request.GET.get("storage_serial")
    context = {'result': "请输入各项参数"}
    if storage_serial :
        try:
            for serial in storage_serial.split(',') :
                print serial
                if LdevList.objects.filter(Q(serial=serial)).values("serial") :
                    LdevList.objects.filter(Q(serial=serial)).delete()
                    logger.info('storage has been deleted : %s' % serial)
                    context['result'] = "删除成功,可再次删除"
                else:
                    context['result'] = serial + "删除失败,该存储不存在，请检查参数输入是否正确"
        except Exception as e:
            logger.error(e)
            context['result'] = "删除失败,请检查参数输入是否正确"
        return render(request, 'delstorageinfo.html',context)
    else:
        return render(request, 'delstorageinfo.html', context)

# 返回iostat页面
def iostatloginit(request):
    return render(request, 'iostatlog.html')

# 显示IOSTAT图
@csrf_exempt
def getiostatlog(request):
    try :
        performance_option = iostat.cls_iostatlog["option"]
        time_list = iostat.cls_iostatlog["date"]
        n = performance_option.index(request.POST.get("option"))
        result = {}
        data = []
        disks = request.POST.getlist("disks")
        for disk in disks :
            for var in time_list:
                data.append(iostat.cls_iostatlog["data"][var][disk][n])
            result[disk] = data
            data = []
        result["date"] = time_list
    except Exception as e  :
        logger.error(e)
        result = {"date":[],"data":[]}
    logger.info('iostat log has been displayed ')
    return HttpResponse(json.dumps(result), content_type='application/json')

# 根据iostat日志获取参数
@csrf_exempt
def getiostatoption(request):
    try:
        filename = request.POST.get("filename")
        disk_iostat = iostat()
        result = disk_iostat.getoption(filename)
        iostat.cls_iostatlog = result
        logger.info('iostat option has been got')
        return HttpResponse(json.dumps(result), content_type="application/json")
    except Exception as e:
        logger.error(e)
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 上传iostat日志
@csrf_exempt
def uploadiostatlog(request):
    try:
        if request.method == "POST":
            path = "/home/liu/PycharmProjects/USMP/uploadfiles"
            if not os.path.exists(path):
                os.makedirs(path)
            for file in request.FILES.getlist('iostat_selectFile') :
                filename = str(file)
                with open(path+filename,'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
        logger.info('iostat log has been uploaded')
        return HttpResponse(json.dumps("success"), content_type='application/json')
    except Exception as e:
        logger.error(e)
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 返回二线检查页面
def lineCheck(request):
    return render(request, 'linecheck.html')


