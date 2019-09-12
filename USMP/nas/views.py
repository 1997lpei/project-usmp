# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from index.models import *
import json
import initdb.initNasDb
import paramiko
import re
import threading
import multiprocessing
import datetime
import logging
netapp_nas_list_path = "C:\\my_projects\\USMP\\USMP\\initdb\\nas_list.txt"
# Create your views here.
logger = logging.getLogger('django')
# 返回netapp nas页面
def goToNasClusterInfoPage(request):
    context = {'cluster':"none"}
    nas_name =  request.GET.get('cluster')
    context['cluster'] = nas_name
    return render(request, 'netappnas.html',context)

# 获取nas详细信息
@csrf_exempt
def getNasClusterInfo(request):
    cluster_name = request.POST.get('cluster_name')
    result_csv = {"node_list":[],"aggr_list":[],"svm_list":[],"vol_count":0}
    if cluster_name == "":
        result_csv = {"node_list": [], "aggr_list": [], "svm_list": [], "vol_count": 0}
    else:
        cluster = NasCluster.objects.get(name=cluster_name)
        for aggr in cluster.nasaggregate_set.all() :
            result_csv['aggr_list'].append(aggr.name)
        for node in cluster.nasnode_set.all() :
            result_csv['node_list'].append(node.name)
        for svm in cluster.nasvserver_set.all() :
            result_csv['svm_list'].append(svm.name)
        result_csv['vol_count'] = len(cluster.nasvolume_set.all())
    return HttpResponse(json.dumps(result_csv), content_type='application/json')

# 获取volume使用率 column图
@csrf_exempt
def getUsedPercentOfVolume(request):
    cluster_name = request.POST.get("cluster_name")
    result = {"xaxis": [], "percent": [], "size": [], "used": []}
    try:
        cluster = NasCluster.objects.get(name=cluster_name)
        for var in cluster.nasvolume_set.all() :
            result['xaxis'].append(var.name)
            percent = round((float(var.sizeused) / float(var.sizetotal) * 100 ),2)
            result['percent'].append(percent)
            result['size'].append(round(float(var.sizetotal)/1024/1024/1024,2))
            result['used'].append(round(float(var.sizeused)/1024/1024/1024, 2))
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 获取aggr使用率 column图
@csrf_exempt
def getUsedPercentOfAggr(request):
    cluster_name = request.POST.get("cluster_name")
    result = {"xaxis" : [],"percent" : [],"size" : [],"used" : []}
    try:
        cluster = NasCluster.objects.get(name=cluster_name)
        for aggr in cluster.nasaggregate_set.all() :
            result['xaxis'].append(aggr.name)
            percent = round((float(aggr.sizeused) / float(aggr.sizetotal) * 100 ),2)
            result['percent'].append(percent)
            result['size'].append(round(float(aggr.sizetotal)/1024/1024/1024,2))
            result['used'].append(round(float(aggr.sizeused)/1024/1024/1024, 2))
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 获取nas详细信息
@csrf_exempt
def getVolumeFullInfo(request):
    cluster_name = request.POST.get('param')
    datacsv = []
    if cluster_name == "":
        ldev_info = {"volname": "none", "vserver": "none", "size": "none", "available": "none", "used": "none"}
    else:
        cluster = NasCluster.objects.get(name=cluster_name)
        for volume in cluster.nasvolume_set.all():
            vol_info = \
                {"cluster":cluster_name,
                 "volume": volume.name,
                 "vserver": volume.vserverid.name,
                 "aggregate":volume.aggregateid.name,
                 "node":volume.nodeid.name,
                 "vol_size": round(float(volume.sizetotal)/1024/1024/1024,2),
                 "vol_availsize": round(float(volume.sizeavail)/1024/1024/1024,2),
                 "vol_usedsize": round(float(volume.sizeused)/1024/1024/1024,2)}
            datacsv.append(vol_info)
        result_csv = {"data": datacsv}
    return HttpResponse(json.dumps(result_csv), content_type='application/json')

# 返回拓扑页
def getNasTopology(request):
    return render(request, 'nastopology.html')

# NAS数据库刷新
@csrf_exempt
def updateNasDb(request):
    if initdb.initNasDb.initNasDb()== 'SUCCESS':
        return HttpResponse(json.dumps("success"), content_type='application/json')
    elif initdb.initNasDb.initNasDb() == 'DeadLockHappened':
        return HttpResponse(json.dumps("DeadLockHappened"), content_type='application/json')
    else:
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 获取 NAS Failover 状态
@csrf_exempt
def getNetappNasFailoverStatus(request):
    try:
        datacsv = []
        file = open(netapp_nas_list_path, 'r')
        cluster_dict = {}
        for line in file.readlines():
            if line.strip():
                cluster_dict[line.split(':')[0].strip()] = line.split(':')[1].strip()
        file.close()
        for key in cluster_dict :
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(cluster_dict[key], 22, 'admin', 'cl0udCCZ')
            stdin, stdout, stderr = ssh.exec_command("storage failover show")
            stdout_result = stdout.read()
            for line in stdout_result.split('\n'):
                if 'Takeover' not in line and 'Partner' not in line and '---' not in line and 'displayed' not in line and len(line) > 1:
                    print line
                    faileover_status = {'node': '', 'ip': '', 'takeover_possible': '', 'partner': ''}
                    faileover_status['node'] = line.split()[0]
                    faileover_status['ip'] = cluster_dict[key]
                    faileover_status['takeover_possible'] = line.split()[2]
                    faileover_status['partner'] = line.split()[1]
                    datacsv.append(faileover_status)
            ssh.close()
        result_csv = {"data" : datacsv}
        logger.info("getNetappNasFailoverStatus : successfully")
    except Exception as e:
        print e
        logger.error(e)
        result_csv = {"data": ""}
    return HttpResponse(json.dumps(result_csv), content_type='application/json')

# 获取 NAS 文件系统使用率
@csrf_exempt
def getNetappNasFsUsed(request):
    try:
        datacsv = []
        file = open(netapp_nas_list_path, 'r')
        cluster_dict = {}
        for line in file.readlines():
            if line.strip():
                cluster_dict[line.split(':')[0].strip()] = line.split(':')[1].strip()
        file.close()
        for key in cluster_dict:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(cluster_dict[key], 22, 'admin', 'cl0udCCZ')
            stdin, stdout, stderr = ssh.exec_command("vol show")
            stdout_list = stdout.read()
            for line in stdout_list.split('\n'):
                if 'Used%' not in line and '---' not in line and 'displayed' not in line and len(line) > 1:
                    volume_info = {'cluster': '', 'volume': '', 'size': '', 'available': '', 'percentofused': ''}
                    volume_info['cluster'] = key
                    volume_info['volume'] = line.split()[1]
                    volume_info['size'] = line.split()[5]
                    volume_info['available'] = line.split()[6]
                    volume_info['percentofused'] = line.split()[7]
                    datacsv.append(volume_info)
            ssh.close()
        result_csv = {"data": datacsv}
        logger.info('getNetappNasFsUsed : successfully' )
    except Exception as e:
        logger.error(e)
        result_csv = {"data": ""}
    return HttpResponse(json.dumps(result_csv), content_type='application/json')

# 获取 NAS Failover 状态
@csrf_exempt
def getNetappNasHealthStatus(request):
    try:
        datacsv = []
        file = open(netapp_nas_list_path, 'r')
        cluster_dict = {}
        for line in file.readlines():
            if line.strip():
                cluster_dict[line.split(':')[0].strip()] = line.split(':')[1].strip()
        file.close()
        for key in cluster_dict :
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(cluster_dict[key], 22, 'admin', 'cl0udCCZ')
            stdin, stdout, stderr = ssh.exec_command("cluster show")
            stdout_result = stdout.read()
            for line in stdout_result.split('\n'):
                if 'Health' not in line and '---' not in line and 'displayed' not in line and len(line) > 1:
                    health_status = {'node': '', 'ip': '', 'health': ''}
                    health_status['node'] = line.split()[0]
                    health_status['health'] = line.split()[1]
                    health_status['ip'] = cluster_dict[key]
                    datacsv.append(health_status)
            ssh.close()
        result_csv = {"data": datacsv}
        logger.info('getNetappNasHealthStatus : successfully')
    except Exception as e:
        logger.error(e)
        result_csv = {"data": ""}
    return HttpResponse(json.dumps(result_csv), content_type='application/json')

# 获取 NAS 日志
@csrf_exempt
def getNetappNasEvent(request):
    try:
        today = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%m/%d/%Y %H:%M:%S")
        cmd = 'event log show -time \"' + yesterday + '\"..\"' + today + '\" -severity <=WARNING'
        datacsv = []
        file = open(netapp_nas_list_path, 'r')
        cluster_dict = {}
        for line in file.readlines():
            if line.strip():
                cluster_dict[line.split(':')[0].strip()] = line.split(':')[1].strip()
        file.close()
        for key in cluster_dict :
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(cluster_dict[key], 22, 'admin', 'cl0udCCZ')
            stdin, stdout, stderr = ssh.exec_command(cmd)
            stdout_result = stdout.read()
            for line in stdout_result.split('\n'):
                if 'Severity' not in line and '---' not in line and 'displayed' not in line and len(line) > 1:
                    event = {'cluster':'','time': '','severity': '','event':''}
                    event_info = line.split()
                    event['cluster'] = key
                    event['time'] = event_info[0] + ' ' + event_info[1]
                    event['severity'] = event_info[3]
                    event['event'] = event_info[4:]
                    datacsv.append(event)
            ssh.close()
        result_csv = {"data": datacsv}
        logger.info('getNetappNasHealthStatus : successfully')
    except Exception as e:
        logger.error(e)
        result_csv = {"data": ""}
    return HttpResponse(json.dumps(result_csv), content_type='application/json')