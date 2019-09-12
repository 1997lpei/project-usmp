# encoding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q
import json
from initdb.initStorageDb import importdata
from index.models import *
# Create your views here.

# 刷新存储LDEV数据库
@csrf_exempt
def updateStorageDb(request):
    selectedfiles = json.loads(request.POST.get('selectedfiles'))
    try:
        import_db = importdata(selectedfiles)
        import_db.dataproc()
        import_db.importtodata()
        return HttpResponse(json.dumps("success"), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 返回hds storage页面
def goToStorageInfoPage(request):
    context = {'storage_name':"none"}
    storage =  request.GET.get('storage')
    context['storage_name'] = storage
    return render(request, 'storageinfo.html',context)

# 获取某台存储LDEV信息
@csrf_exempt
def getldevlist(request):
    storage_serial = request.POST.get('param')
    datacsv = []
    if storage_serial == "":
        ldev_info = {"serial": "none", "ldev": "none", "vol_capacity": "none", "ports": "none", "raid_groups": "none",
                     "hostname": "none", "hlun_id": "none"}
    else:
        ldev_list = LdevList.objects.filter(serial=storage_serial)
        for var in ldev_list:
            ldev_info = {"serial": var.serial, "ldev": var.ldev, "vol_capacity": var.vol_capacity, "ports": var.ports,
                         "raid_groups": var.raid_groups, "hostname": var.hostname, "hlun_id": var.hlun_id}
            datacsv.append(ldev_info)
        result_csv = {"data": datacsv}
    return HttpResponse(json.dumps(result_csv), content_type='application/json')

# 获取某台存储上总体使用率 饼图
@csrf_exempt
def updatePercentOfused_pie(request):
    storage_serial = request.POST.get("storage_serial")
    total_capacity = 0
    used_capacity = 0
    unused_capacity = 0
    datacsv = []
    try:
        ldev_list = LdevList.objects.filter(serial=storage_serial).values("ldev", "hostname", "vol_capacity").distinct()
        for var in ldev_list:
            total_capacity = total_capacity + var["vol_capacity"]
            if not var["hostname"]:
                unused_capacity = unused_capacity + var["vol_capacity"]
            else:
                used_capacity = used_capacity + var["vol_capacity"]
        datacsv.append({"name": "未使用", "y": unused_capacity})
        datacsv.append({"name": "已使用", "y": used_capacity})
        return HttpResponse(json.dumps(datacsv), content_type='application/json')
    except LdevList.DoesNotExist as e:
        print e
        return HttpResponse(json.dumps("LdevList 结果为空！"), content_type='application/json')

# 获取存储总体使用率 bart图
@csrf_exempt
def updateInfoOfused_bar(request):
    storage_serial = request.POST.get("storage_serial")
    result = {"xaxis":[],"data":[]}
    try:
        ldev_list = LdevList.objects.filter(serial=storage_serial).values("ldev", "hostname", "vol_capacity").distinct()
        vol_capacity_list = LdevList.objects.filter(Q(serial=storage_serial) & Q(hostname__isnull=False)).values("vol_capacity").distinct()
        used_count = [0 for x in range(0,len(vol_capacity_list))]
        unused_count = [0 for x in range(0,len(vol_capacity_list))]
        result["data"] = [[],[]]
        result["xaxis"] = [0 for x in range(0, len(vol_capacity_list))]
        for var in ldev_list:
            for n in range(len(vol_capacity_list)):
                 if var["vol_capacity"] == vol_capacity_list[n]["vol_capacity"]:
                    if not var["hostname"]:
                        unused_count[n] = unused_count[n] + 1
                    else:
                        used_count[n] = used_count[n] + 1
        for n in range(len(vol_capacity_list)):
            result["xaxis"][n] = vol_capacity_list[n]["vol_capacity"]
        result["data"][0] = used_count
        result["data"][1] = unused_count
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        raise e
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 获取存储上hostgroup使用ldev情况 column图
@csrf_exempt
def updateInfoOfLdev_column(request):
    storage_serial = request.POST.get("storage_serial")
    host_dict = {}
    try:
        host_list = LdevList.objects.filter(Q(serial=storage_serial) & Q(hostname__isnull=False)).order_by("hostname").values("hostname").distinct()
        ldev_list = LdevList.objects.filter(Q(serial=storage_serial) & Q(hostname__isnull=False)).values("ldev","hostname","vol_capacity").distinct()
        vol_capacity_list = LdevList.objects.filter(Q(serial=storage_serial) & Q(hostname__isnull=False)).values("vol_capacity").distinct()
        for var in host_list:
            host_dict[var["hostname"]] = [0 for x in range(0,len(vol_capacity_list))]
        result = {"name": [0 for x in range(0,len(vol_capacity_list))], "data": [ [] for x in range(0,len(vol_capacity_list))], "xaxis": []}
        for var in ldev_list:
            for n in range(len(vol_capacity_list)):
                if var["vol_capacity"] == vol_capacity_list[n]["vol_capacity"]:
                    host_dict[var["hostname"]][n] = host_dict[var["hostname"]][n] + 1
        for n in range(len(vol_capacity_list)):
            result["name"][n] = vol_capacity_list[n]["vol_capacity"]
        for var in host_list:
            result["xaxis"].append(var["hostname"])
            for n in range(len(vol_capacity_list)):
                result["data"][n].append(host_dict[var["hostname"]][n])

        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        raise e
        return HttpResponse(json.dumps("failed"), content_type='application/json')

# 返回拓扑页
def topology(request):
    return render(request, 'topology.html')

# 获取某台存储拓扑图
@csrf_exempt
def gettopology(request):
    try:
        storage = request.POST.get("storage")
        print storage
        raid_group_list = LdevList.objects.filter(serial=storage).values("raid_groups").distinct()
        hostname_list = LdevList.objects.filter(serial=storage).values("hostname").distinct()
        result = {"nodes":[],"edges":[]}
        nodes = []
        edges = []
        storage_node = {"id": storage, "x": 0, "y": 0, "size": 5, "color": '#666',"label":storage}
        nodes.append(storage_node)
        edge_id = 0

        posion_x = -60
        for hostname in hostname_list:
            posion_x = posion_x + 100/len(hostname_list)
            posion_y = -35
            if hostname["hostname"] :
                node = {"id": hostname["hostname"], "x": posion_x, "y": posion_y, "size": 5, "color": '#666',"label":hostname["hostname"]}
                nodes.append(node)

        posion_x = -50
        n = 0
        for raid_group in raid_group_list :
            n = n + 1
            posion_x = posion_x + 100/len(raid_group_list)
            posion_y = -5
            if raid_group["raid_groups"]:
                node = {"id": raid_group["raid_groups"], "x": posion_x, "y": posion_y, "size": 5, "color": '#666',"label":raid_group["raid_groups"]}
                nodes.append(node)
                ldev_list = LdevList.objects.filter(Q(serial=storage) & Q(raid_groups = raid_group["raid_groups"])).values("ldev").distinct()
                posion_x_ldev = -50
                for ldev in ldev_list:
                    posion_x_ldev = posion_x_ldev + 100 / len(ldev_list)
                    posion_y_ldev = -10 + (-1 * n)
                    if ldev["ldev"] :
                        node = {"id": ldev["ldev"], "x": posion_x_ldev, "y": posion_y_ldev, "size": 5, "color": '#666',"label": ldev["ldev"]}
                        nodes.append(node)
                        edge_id = edge_id + 1
                        edge = {"id": edge_id, "source": raid_group["raid_groups"],
                                "target": ldev["ldev"], "size": 1, "color": '#ccc'}
                        edges.append(edge)

        for raid_group in raid_group_list :
            edge_id = edge_id + 1
            if raid_group["raid_groups"]:
                edge = {"id": edge_id, "source": storage, "target": raid_group["raid_groups"], "size": 1, "color": '#ccc'}
                edges.append(edge)

        for hostname in hostname_list :
            if hostname["hostname"] :
                hostname_ldev_list = LdevList.objects.filter(Q(serial=storage) & Q(hostname = hostname["hostname"])).values("ldev").distinct()
                for hostname_ldev in hostname_ldev_list :
                    if hostname_ldev["ldev"] :
                        edge_id = edge_id + 1
                        edge = {"id": edge_id, "source": hostname["hostname"], "target": hostname_ldev["ldev"], "size": 1,"color": '#ccc'}
                        edges.append(edge)
        '''
        for raid_group in raid_group_list :
            if raid_group["raid_groups"]:
                raidgroup_hostname_list = LdevList.objects.filter(Q(serial=storage) & Q(raid_groups=raid_group["raid_groups"])).values("hostname").distinct()
                for raidgroup_hostname in raidgroup_hostname_list :
                    edge_id = edge_id + 1
                    if raidgroup_hostname["hostname"]:
                        edge = {"id": edge_id, "source": raid_group["raid_groups"], "target": raidgroup_hostname["hostname"], "size": 1, "color": '#ccc'}
                        edges.append(edge)
        '''
        result["nodes"] = nodes
        result["edges"] = edges
        return HttpResponse(json.dumps(result),content_type="application/json")
    except Exception as e :
        print e
        return HttpResponse(json.dumps("failed"),content_type="application/json")