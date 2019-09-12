/**
main function to initiate template pages by self
**/


/* 获取 NAS Failover 状态 */
function getNetappNasFailoverStatus (){
    $('#netapp_nas_failover_status_table').DataTable({
        "bLengthChange":false,
        "bAutoWidth":false,
        "ajax" : {
            "url" : "/getnetappnasfailoverstatus/",
            "type" : "POST",
            "dataType" : "json"
        },
        "columns" : [
            {"data" : "node"},
            {"data" : "ip"},
            {"data" : "takeover_possible"},
            {"data" : "partner"}
            ]
    });
}

/* 获取 NAS 文件系统使用率*/
function getNetappNasFsUsed (){
    $('#netapp_nas_fs_used_table').DataTable({
        "bLengthChange":false,
        "bAutoWidth":false,
        "order":[[4,"desc"]],
        "ajax" : {
            "url" : "/getnetappnasfsused/",
            "type" : "POST",
            "dataType" : "json"
        },
        "columns" : [
            {"data" : "cluster"},
            {"data" : "volume"},
            {"data" : "size"},
            {"data" : "available"},
            {"data" : "percentofused"}
            ]
    });
}

/* 获取 NAS Failover 状态 */
function getNetappNasHealthStatus (){
    $('#netapp_nas_health_status_table').DataTable({
        "bLengthChange":false,
        "bAutoWidth":false,
        "ajax" : {
            "url" : "/getnetappnashealthstatus/",
            "type" : "POST",
            "dataType" : "json"
        },
        "columns" : [
            {"data" : "node"},
            {"data" : "ip"},
            {"data" : "health"}
            ]
    });
}

/* 获取 NAS 日志*/
function getNetappNasEvent (){
    $('#netapp_nas_event_table').DataTable({
        "bLengthChange":false,
        "bAutoWidth":false,
        "ajax" : {
            "url" : "/getnetappnasevent/",
            "type" : "POST",
            "dataType" : "json"
        },
        "columns" : [
            {"data" : "cluster"},
            {"data" : "time"},
            {"data" : "severity"},
            {"data" : "event"}
            ]
    });
}
