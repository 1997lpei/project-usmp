# encoding:utf-8
"""USMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from xml.dom.minidom import _in_document

from django.conf.urls import url
from django.contrib import admin

from USMP import settings
from index import views as index_view
from nas import views as nas_view
from storage import views as sto_view
from app01 import views as app_view

urlpatterns = [
    # url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view.index),
    url(r'^welcome/$', index_view.welcome),
    url(r'gotoupdatenasdb/$', index_view.goToUpdateNasDb),  # 返回NAS数据库刷新页面
    url(r'updatenasdb/$', nas_view.updateNasDb),  # NAS数据库刷新
    url(r'^initindexbar/$', index_view.initIndexBar),  # 更新左侧导航栏
    url(r'^gotonasclusterinfopage', nas_view.goToNasClusterInfoPage),  # 返回nas cluster页面
    url(r'^gotostorageinfopage', sto_view.goToStorageInfoPage),  # 返回存储详细信息页面
    url(r'^getnasclusterinfo/$', nas_view.getNasClusterInfo),  # 获取nas概要信息
    url(r'^getUsedPercentOfVolume/$', nas_view.getUsedPercentOfVolume),  # 获取volume使用率 column图
    url(r'^getUsedPercentOfAggr/$', nas_view.getUsedPercentOfAggr),  # 获取volume使用率 column图
    url(r'^getvolumefullinfo/$', nas_view.getVolumeFullInfo),  # 获取volume详细信息 表格
    url(r'^getnastopology', nas_view.getNasTopology),  # 返回nas 拓扑页
    url(r'gotoupdatestoragedb/$', index_view.goToUpdateStorageDb),  # 存储配置上传/刷新数据库/创建配置EXCE
    url(r'updatestoragedb/$', sto_view.updateStorageDb),  # 存储配置上传/刷新数据库/创建配置EXCE
    url(r'^getldevlist/$', sto_view.getldevlist),  # 获取某台存储LDEV信息
    url(r'^updatePercentOfused_pie/$', sto_view.updatePercentOfused_pie),  # 获取某台存储LDEV信息
    url(r'^updateInfoOfused_bar/$', sto_view.updateInfoOfused_bar),  # 获取某台存储LDEV信息
    url(r'^updateInfoOfLdev_column/$', sto_view.updateInfoOfLdev_column),  # 获取某台存储LDEV信息
    url(r'delstorageinfo/$', index_view.delstorageinfo),  # 删除存储
    url(r'^getiostatlog/$', index_view.getiostatlog),  # 显示IOSTAT图
    url(r'^getiostatoption/$', index_view.getiostatoption),  # 根据iostat日志获取参数
    url(r'^iostatloginit/$', index_view.iostatloginit),  # 返回iostat页面
    url(r'^linecheck/$', index_view.lineCheck),  # 返回iostat页面
    url(r'^upload/$', index_view.uploadiostatlog),  # 上传iostat日志
    url(r'^topology/$', sto_view.topology),  # 返回拓扑页
    url(r'^gettopology/$', sto_view.gettopology),  # 获取某台存储拓扑图

    url(r'getnetappnasfailoverstatus/$', nas_view.getNetappNasFailoverStatus),  # 获取 Netapp Nas Failover Status
    url(r'getnetappnasfsused/$', nas_view.getNetappNasFsUsed),  # 获取 Netapp Nas Failover Status
    url(r'getnetappnashealthstatus/$', nas_view.getNetappNasHealthStatus),  # 获取 Netapp Nas health Status
    url(r'getnetappnasevent/$', nas_view.getNetappNasEvent),  # 获取 Netapp Nas health Status

    url(r'produce_san/$', app_view.produce_san),  # 返回生产SAN数据界面
    url(r'produce_nas/$', app_view.produce_nas),  # 返回生产NAS数据界面

    url(r'test_san/$', app_view.test_san),  # 返回测试SAN数据界面
    url(r'test_nas/$', app_view.test_nas),  # 返回测试NAS数据界面

    url(r'getproducesan/$', app_view.getProduceSan.as_view()),  # 生产SAN数据增删改查
    url(r'getproducenas/$', app_view.getProduceNas.as_view()),  # 生产NAS数据增删改查

    url(r'getdatainfo/$', app_view.getDataInfo),  # 获取SAN数据详情
    url(r'datatoexcel/$', app_view.dataToExcel),  # 导出excel数据

    url(r'gettestsan/$', app_view.getTestSan.as_view()),  # 获取测试SAN数据
    url(r'gettestnas/$', app_view.getTestNas.as_view()),  # 获取测试NAS数据
]

if settings.DEBUG:
    # 获取静态文件
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
