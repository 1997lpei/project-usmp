# encoding:utf-8
from django.shortcuts import render
import sys
import os
import time
import datetime
import paramiko
import multiprocessing
import django
import random
import logging
sys.path.extend(['/home/liu/PycharmProjects/USMP'])
os.environ["DJANGO_SETTINGS_MODULE"] =  "USMP.settings"
django.setup()
from index.models import *
# Create your views here.
#########全局变量##########
nas_list_path = '/home/liu/PycharmProjects/USMP/initdb/nas_list.txt'
user = 'admin'
password = 'cl*****Z'
port = 22
logger = logging.getLogger('django')
##########NAS命令##########
cmdClusterIdentityShow = "cluster identity show"
cmdNodeShow = 'node show -fields node,serialnumber,nvramid,health,eligibility'
cmdClusterIdentityUuidShow = 'cluster identity show -fields uuid'
cmdAggrShow = 'aggr show -fields aggregate,cluster-id,state,owner-id,size,usedsize,percent-used,physical-used,physical-used-percent,availsize,root,raidtype,maxraidsize'
cmdSvmShow = 'vserver show -fields vserver,uuid,admin-state'
cmdVolShow = 'vol show -fields volume,aggregate,size,available,percent-used,node,junction-path,state,is-cluster-volume'

def sshConnect(ip):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user,password)
        getClusterInfoFromNas(ssh)
        getNodeInfoFromNas(ssh)
        getAggrInfoFromNas(ssh)
        getSvmInfoFromNas(ssh)
        getVolInfoFromNas(ssh)
        ssh.close()
        return 'SUCCESS'
    except Exception as e :
        logger.error(e)
        return str(e)

def clearDb():
    NasCluster.objects.all().delete()

def getRandomUuid():
    seed = '1234567890qwertyuiopasdfghjklzxcvbnm'
    now = str(int(time.time()))
    uuid = ''
    for i in range(6):
        uuid = uuid + random.choice(seed)
    uuid = uuid + '-'
    for i in range(6):
        uuid = uuid + random.choice(seed)
    uuid = uuid + '-'
    for i in range(6):
        uuid = uuid + random.choice(now)
    return uuid

def getSizeToBytes(size):
    if 'TB' in size :
        result = int(float(size.split('TB')[0]) * 1024 * 1024 * 1024 * 1024)
    elif 'GB' in size :
        result = int(float(size.split('GB')[0]) * 1024 * 1024 * 1024)
    elif 'MB' in size :
        result = int(float(size.split('MB')[0]) * 1024 * 1024)
    elif 'KB' in size :
        result = int(float(size.split('KB')[0]) * 1024)
    else :
        result = int(float(size.split('B')[0]))
    return result

def getClusterInfoFromNas(ssh):
    clusterinfo = {'uuid':'','name':'','serialNumber':'','updatetime':''}
    stdin, stdout, stderr = ssh.exec_command(cmdClusterIdentityShow)
    for line in stdout.readlines():
        if 'Cluster UUID' in line :
            clusterinfo['uuid']=line.strip().split(':')[1].lstrip()
        elif 'Cluster Name' in line :
            clusterinfo['name']=line.strip().split(':')[1].lstrip()
        elif 'Cluster Serial Number' in line :
            clusterinfo['serialNumber']=line.strip().split(':')[1].lstrip()
        clusterinfo['updatetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    putClusterInfoIntoDb(clusterinfo)

def putClusterInfoIntoDb(clusterinfo):
    NasCluster(uuid=clusterinfo['uuid'],name=clusterinfo['name'],serialnumber=clusterinfo['serialNumber'],updatetime=clusterinfo['updatetime']).save()
    return True

def getNodeInfoFromNas(ssh):
    nodeinfolist = []
    stdin, stdout, stderr = ssh.exec_command(cmdClusterIdentityUuidShow)
    clusterid = stdout.readlines()[2:-1][0].strip()
    stdin,stdout,stderr = ssh.exec_command(cmdNodeShow)
    for line in stdout.readlines()[2:-2]:
        info = {'uuid': '', 'name': '', 'serialNumber': '', 'state': '', 'clusterid': '','updatetime':''}
        name = line.strip().split()[0]
        serialNumber = line.strip().split()[1]
        uuid = line.strip().split()[2]
        state = ''
        if line.strip().split()[3] == 'true' and line.strip().split()[4] == 'true' :
            state = 'OK'
        info['name'] = name
        info['uuid'] = uuid
        info['serialNumber'] = serialNumber
        info['state'] = state
        info['clusterid'] = clusterid
        info['updatetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        nodeinfolist.append(info)
    putNodeInfoIntoDb(nodeinfolist)

def putNodeInfoIntoDb(nodeinfolist):
    for nodeinfo in nodeinfolist :
        NasNode(uuid=nodeinfo['uuid'],name=nodeinfo['name'],clusterid=NasCluster.objects.get(uuid=nodeinfo['clusterid']),\
                serialnumber=nodeinfo['serialNumber'],state=nodeinfo['state'],updatetime=nodeinfo['updatetime']).save()
    return True

def getAggrInfoFromNas(ssh):
    aggrinfolist = []
    stdin, stdout, stderr = ssh.exec_command(cmdAggrShow)
    for line in stdout.readlines()[2:-2]:
        info = {'name':'','sizeavail':'','clusterid':'','raidsize':'','nodeid':'','sizeusedpercent':'','raidtype':'','isrootaggregate':'','sizetotal':'','state':'','sizeused':'','updatetime':''}
        info['name'] = line.strip().split()[0]
        info['sizeavail'] = getSizeToBytes(line.strip().split()[1])
        info['clusterid'] = line.strip().split()[2]
        info['raidsize'] = line.strip().split()[3]
        info['nodeid'] = line.strip().split()[4]
        info['sizeusedpercent'] = line.strip().split()[5].split('%')[0]
        info['raidtype'] = line.strip().split()[6]
        info['isrootaggregate'] = line.strip().split()[7]
        info['sizetotal'] = getSizeToBytes(line.strip().split()[8])
        info['state'] = line.strip().split()[9]
        info['sizeused'] = getSizeToBytes(line.strip().split()[10])
        info['uuid'] = getRandomUuid()
        aggrinfolist.append(info)
        info['updatetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    putAggrInfoIntoDb(aggrinfolist)

def putAggrInfoIntoDb(aggrinfolist):
    for aggrinfo in aggrinfolist :
        NasAggregate(uuid=aggrinfo['uuid'],
                     name=aggrinfo['name'],
                     clusterid=NasCluster.objects.get(uuid=aggrinfo['clusterid']),
                     nodeid=NasNode.objects.get(uuid=aggrinfo['nodeid']),
                     state=aggrinfo['state'],
                     sizetotal = aggrinfo['sizetotal'],
                     sizeused = aggrinfo['sizeused'],
                     sizeavail = aggrinfo['sizeavail'],
                     sizeusedpercent = aggrinfo['sizeusedpercent'],
                     sizeavailpercent = 100.0 - float(aggrinfo['sizeusedpercent']),
                     raidsize = aggrinfo['raidsize'],
                     raidtype = aggrinfo['raidtype'],
                     isrootaggregate = aggrinfo['isrootaggregate'],
                     updatetime = aggrinfo['updatetime']
                     ).save()

def getSvmInfoFromNas(ssh):
    svminfolist = []
    stdin, stdout, stderr = ssh.exec_command(cmdClusterIdentityUuidShow)
    clusterid = stdout.readlines()[2:-1][0].strip()
    stdin, stdout, stderr = ssh.exec_command(cmdSvmShow)
    for line in stdout.readlines()[2:-2]:
        info = {'uuid':'','name':'','state':'','clusterid':'','updatetime':''}
        info['name'] = line.strip().split()[0]
        info['uuid'] = line.strip().split()[1]
        if line.strip().split()[2] == '-' :
            info['state'] = 'unkown'
        else:
            info['state'] = line.strip().split()[2]
        info['clusterid'] = clusterid
        info['updatetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        svminfolist.append(info)
    putSvmInfoIntoNas(svminfolist)

def putSvmInfoIntoNas(svminfolist):
    for svminfo in svminfolist:
        NasVserver(uuid=svminfo['uuid'],name=svminfo['name'],state=svminfo['state'],clusterid=NasCluster.objects.get(uuid=svminfo['clusterid']),updatetime=svminfo['updatetime']).save()

def getVolInfoFromNas(ssh):
    volinfolist = []
    stdin, stdout, stderr = ssh.exec_command(cmdClusterIdentityUuidShow)
    clusterid = stdout.readlines()[2:-1][0].strip()
    stdin, stdout, stderr = ssh.exec_command(cmdVolShow)
    for line in stdout.readlines()[2:-2]:
        info = {'clusterid':'','uuid':'','name':'','vserverid':'','nodeid':'','aggregateid':'','sizetotal':'',\
                    'sizeused':'','sizeusedpercent':'','sizeavail':'','sizeavailpercent':'','state':'','junctionpath':'','isvserverroot':'','updatetime':''}
        info['vserverid'] = line.strip().split()[0]
        info['name'] = line.strip().split()[1]
        info['aggregateid'] = line.strip().split()[2]
        info['sizetotal'] = getSizeToBytes(line.strip().split()[3])
        info['state'] = line.strip().split()[4]
        info['isvserverroot'] = line.strip().split()[5]
        info['junctionpath'] = line.strip().split()[6]
        info['sizeavail'] = getSizeToBytes(line.strip().split()[7])
        info['sizeusedpercent'] = float(line.strip().split()[8].split('%')[0])
        info['nodeid'] = line.strip().split()[9]
        info['clusterid'] = clusterid
        info['sizeused'] = info['sizetotal'] - info['sizeavail']
        info['sizeavailpercent'] = 100.0 - float(info['sizeusedpercent'])
        info['uuid'] = getRandomUuid()
        info['updatetime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        volinfolist.append(info)
    putVolInfoIntoDb(volinfolist)

def putVolInfoIntoDb(volinfolist):
    for volinfo in volinfolist:
        NasVolume(uuid=volinfo['uuid'],
                  name=volinfo['name'],
                  clusterid=NasCluster.objects.get(uuid=volinfo['clusterid']),
                  vserverid=NasVserver.objects.get(name=volinfo['vserverid']),
                  nodeid=NasNode.objects.get(name=volinfo['nodeid']),
                  aggregateid=NasAggregate.objects.get(name=volinfo['aggregateid']),
                  sizetotal=volinfo['sizetotal'],
                  sizeused=volinfo['sizeused'],
                  sizeusedpercent=volinfo['sizeusedpercent'],
                  sizeavail=volinfo['sizeavail'],
                  sizeavailpercent=volinfo['sizeavailpercent'],
                  isvserverroot=volinfo['isvserverroot'],
                  state=volinfo['state'],
                  junctionpath=volinfo['junctionpath'],
                  updatetime=volinfo['updatetime']
                  ).save()

def initNasDb() :
    try:
        ip_list = []
        nas_list = open(nas_list_path, 'r')
        for line in nas_list.readlines():
            if line.strip():
                ip_list.append(line.strip().split(':')[1])
        nas_list.close()
        starttime = time.time()
        clearDb()
        pool = multiprocessing.Pool(3)
        for ip in ip_list:
            result = pool.apply_async(sshConnect,(ip,))
        pool.close()
        pool.join()
        if "Deadlock found when trying to get lock" in result.get() :
            return 'DeadLockHappened'
        endtime = time.time()
        logger.info('run time : %f S' % (endtime - starttime))
        return result.get()
    except Exception as e:
        logger.error(e)
        return 'Failed'
