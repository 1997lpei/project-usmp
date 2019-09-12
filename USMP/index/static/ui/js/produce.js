/**
 main function to initiate template pages by self
 **/


/* 获取 生产SAN数据 */
function getProduceSanData() {

    // 获取数据
    $('#get_produce_san_data').DataTable({
        "bLengthChange": false,
        "bAutoWidth": false,
        "ajax": {
            "url": "/getproducesan/",
            "type": "get",
            "dataType": "json"
        },
        "columns": [
            {
                "data": "id",
                "orderable": false,
                "width": "2%",
                "render": function (data, type, row, meta) {
                    return data = '<input type="checkbox" name="check" data-id="' + data + '">';
                }
            },
            {"data": "name"},
            {"data": "serial_number"},
            {"data": "manage_ip"},
            {"data": "type"},
            {"data": "subordinate_departments"},
            {
                "data": "id",
                "orderable": false,
                "width": "10%",
                "defaultContent": "",
                "render": function (data, type, row, meta) {
                    return data = '<button class="btn btn-info btn-sm edit" data-id=' + data + '><i class="fa fa-pencil"></i>编辑</button>';
                    // + '<button class="btn btn-danger btn-sm delete" data-id=' + data + '><i class="fa fa-trash-o"></i>删除</button>';
                }
            }
        ]
    });

    // 渲染数据
    $("#get_produce_san_data tbody").on('click', '.edit', function () {
        var edit_id = $(this).attr('data-id');
        $.ajax({
            "url": "/getdatainfo/",
            "type": "get",
            "dataType": "json",
            "data": {
                "edit_id": edit_id,
                "type": 'produce_san'
            },
            success: function (data) {
                if (data['status'] == 200) {
                    //渲染数据到页面
                    $("#id").val(data['data'].id);
                    $("#name").val(data['data'].name);
                    $("#serial_number").val(data['data'].serial_number);
                    $("#manage_ip").val(data['data'].manage_ip);
                    $("#computer_room").val(data['data'].computer_room);
                    $("#frame").val(data['data'].frame);

                    $("#purpose").val(data['data'].purpose);
                    $("#type").val(data['data'].type);
                    $("#environmental").val(data['data'].environmental);
                    $("#warranty_level").val(data['data'].warranty_level);
                    $("#landing_mode").val(data['data'].landing_mode);

                    $("#subordinate_departments").val(data['data'].subordinate_departments);
                    $("#produce_date").val(data['data'].produce_date);
                    $("#example_number").val(data['data'].example_number);
                    $("#examples").val(data['data'].examples);
                    $("#instance_port").val(data['data'].instance_port);
                } else {
                    alert(data.msg)
                }
            }
        });
        layer.open({
            //展示数据
            title: '编辑',
            area: '500px',
            type: 1,
            content: $('#form')
        })
    });

    // 导出
    $("#export").on('click', function () {
        send_export_ajax('/datatoexcel/','produce_san')
    });

    // 删除
    $("#delete").click(function () {
        send_delete_ajax("/getproducesan/")
    });

    // 弹出增加框
    $("#add").on('click', function () {
        raise_box()
    });

    // 增加
    $("#save_san").on('click', function () {
        var url = "/getproducesan/";
        var values = $('#addValue_san').val();
        send_add_ajax(url, values)
    });


}

/* 获取生产NAS数据 */
function getProduceNasData() {

    // 获取数据
    $('#get_produce_nas_data').DataTable({
        "bLengthChange": false,
        "bAutoWidth": false,
        "ajax": {
            "url": "/getproducenas/",
            "type": "get",
            "dataType": "json"
        },
        "columns": [
            {
                "data": "id",
                "orderable": false,
                "width": "2%",
                "render": function (data, type, row, meta) {
                    return data = '<input type="checkbox" name="check" data-id="' + data + '">';
                }
            },
            {"data": "colony"},
            {"data": "serial_number"},
            {"data": "purpose"},
            {"data": "type"},
            {"data": "subordinate_departments"},
            {
                "data": "id",
                "orderable": false,
                "width": "10%",
                "defaultContent": "",
                "render": function (data, type, row, meta) {
                    return data = '<a class="btn btn-info btn-sm edit" data-id=' + data + '><i class="fa fa-pencil"></i>编辑</a>';
                    // + '<button class="btn btn-danger btn-sm nas_delete" data-id=' + data + '><i class="fa fa-trash-o"></i>删除</button>';
                }
            }
        ]
    });

    // 渲染数据
    $("#get_produce_nas_data tbody").on('click', '.edit', function () {
        var edit_id = $(this).attr('data-id');
        $.ajax({
            "url": "/getdatainfo/",
            "type": "get",
            "dataType": "json",
            "data": {
                "edit_id": edit_id,
                "type": "produce_nas"
            },
            success: function (data) {
                if (data['status'] == 200) {
                    //渲染数据到页面
                    $("#id").val(data['data'].id);
                    $("#colony").val(data['data'].colony);
                    $("#nose").val(data['data'].nose);
                    $("#serial_number").val(data['data'].serial_number);
                    $("#nose_manage_ip").val(data['data'].nose_manage_ip);
                    $("#colony_manage_ip").val(data['data'].colony_manage_ip);

                    $("#service_ip").val(data['data'].service_ip);
                    $("#computer_room").val(data['data'].computer_room);
                    $("#frame").val(data['data'].frame);
                    $("#purpose").val(data['data'].purpose);
                    $("#type").val(data['data'].type);

                    $("#environmental").val(data['data'].environmental);
                    $("#warranty_level").val(data['data'].warranty_level);
                    $("#landing_mode").val(data['data'].landing_mode);
                    $("#subordinate_departments").val(data['data'].subordinate_departments);
                    $("#produce_date").val(data['data'].produce_date);

                } else {
                    alert(data.msg)
                }
            }
        });
        layer.open({
            //展示数据
            title: '编辑',
            area: '500px',
            type: 1,
            content: $('#form')
        })
    });

    // 导出数据
    $("#nas_export").on('click', function () {
        send_export_ajax('/datatoexcel/','produce_nas')
    });

    // 删除
    $("#nas_delete").click(function () {
        send_delete_ajax('/getproducenas/')
    });

    // 弹出增加框
    $("#nas_add").on('click', function () {
        raise_box()
    });

    // 增加
    $("#save_nas").on('click', function () {
        var url = "/getproducenas/";
        var values = $('#addValue').val();
        send_add_ajax(url, values)
    })
}

// 修改
layui.use('form', function () {
    var form = layui.form;

    form.on('submit(save_update_nas)', function (data) {
        send_update_ajax("/getproducenas/", data);
    });

    form.on('submit(save_update_san)', function (data) {
        send_update_ajax("/getproducesan/", data);
    })
});



// 弹出增加狂
function raise_box() {
    layer.open({
        //展示数据
        title: '增加',
        area: '550px',
        type: 1,
        content: $('#addform')
    })
}

// 增加
function send_add_ajax(url, values) {
    if (values == '') {
        alert('请写入要添加的数据')
    } else {
        if (confirm("您确定要添加吗?")) {
            $.ajax({
                "url": url,
                "type": "POST",
                "dataType": "json",
                "data": {
                    "values": values
                },
                success: function (data) {
                    if (data['status'] == 200) {
                        alert(data.msg);
                        window.location.reload(true)
                    } else {
                        alert(data.msg)
                    }
                }
            })
        }
    }
}

// 修改
function send_update_ajax(url, data) {
    $.ajax({
        "url": url,
        "type": "put",
        "dataType": "json",
        "data": data.field,
        success: function (data) {
            if (data.status == 200) {
                alert(data.msg);
                window.location.reload(true)
            } else {
                alert(data.msg)
            }

        }
    })
}

//导出
function send_export_ajax(url,type) {
    var checkList = []; //选中的复选框data-id
    $("input[type='checkbox']").each(function () {
        if ($(this).is(":checked")) {
            checkList.push($(this).attr('data-id'))
        }
    });
    var length = checkList.length;

    if (length > 0) {
        $.ajax({
            "url": url,
            "type": "POST",
            "dataType": "json",
            "data": {
                "checkList": JSON.stringify(checkList),
                "type" : type
            },
            success: function (data) {
                if (data.status == 200) {
                    window.open(data.url)
                } else {
                    alert(data.msg)
                }
            }
        })
    } else {
        alert('请选择要导出的数据')
    }
}

//删除
function send_delete_ajax(url) {
    var checkList = []; //选中的复选框data-id
        $("input[type='checkbox']").each(function () {
            if ($(this).is(":checked")) {
                checkList.push($(this).attr('data-id'))
            }
        });

        var length = checkList.length;
        if (length > 0) {
            if (confirm('警告！,删除后不可恢复,您确定要删除吗？')) {
                $.ajax({
                    "url": url,
                    "type": "delete",
                    "dataType": "json",
                    "data": {
                        "checkList": JSON.stringify(checkList)
                    },
                    success: function (data) {
                        if (data['status'] == 200) {
                            alert(data.msg);
                            window.location.reload(true)
                        } else {
                            alert(data.msg)
                        }
                    }
                })
            }
        } else {
            alert('请选择要删除的数据')
        }
}







