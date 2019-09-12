var TableManage = function () {
    return {
        //main function to initiate the module
        init: function () {
            var oTable = $('#storage_list_table').DataTable({
                "destroy": true,
                "iDisplayLength": 10,
                "sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
                "ajax" : {
                    "url" : "/init/",
                    "type" : "POST",
                    "data" : {
                        "param" : "none"
                     },
                     "dataType" : "json"
                },
                "columnDefs" : [{
                    "targets" : -1,
                    "data" : null,
                    "render" : function(data,type,row) {
                        var html = "<a class='up btn btn-default btn-xs' id='login'> 登录</a>";
                        return html;
                    }
               }],
                "columns" : [
                {"data" : "storage"},
                {"data" : "serial"},
                {"data" : "ip"},
                {"data" : "user"},
                {"data" : "password"},
                {"data" : "content"},
                {"data" : "tel"},
                {"data" : "location"},
                {}
                ]
            });

            var oTable_ldevlist = $('#ldev_list_table').DataTable({
                "destroy": true,
                "iDisplayLength": 10,
                "sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
                "ajax" : {
                    "url" : "/initldevlist/",
                    "type" : "POST",
                    "data" : {
                        "param" : "none"
                     },
                     "dataType" : "json"
                },
                "columnDefs" : [{
                    "targets" : -1,
                    "data" : null,
               }],
                "columns" : [
                {"data" : "serial"},
                {"data" : "ldev"},
                {"data" : "vol_capacity"},
                {"data" : "ports"},
                {"data" : "raid_groups"},
                {"data" : "hostname"},
                {"data" : "hlun_id"},
                ]
            });

            jQuery('.page-sidebar').on('click', ' li > a', function (e) {
                e.preventDefault();
                var storage_type = $(this).parents('li').attr("name");
                var url = $(this).attr("href");
                var menuContainer = jQuery('.page-sidebar ul');
                var pageContent = $('.page-content');
                var pageContentBody = $('.page-content .page-content-body');

                menuContainer.children('li.active').removeClass('active');
                menuContainer.children('arrow.open').removeClass('open');

                $(this).parents('li').each(function () {
                    $(this).addClass('active');
                    $(this).children('a > span.arrow').addClass('open');
                });
                $(this).parents('li').addClass('active');
                if($(this).next().hasClass('sub-menu') == false) {
                    if ($(this).parents('li').attr("id") == "createconf"){
                        $("#tab_3").css('display','none');
                        $("#tab_3_1").css('display','block');
                        $("#tab_3_2").css('display','none');
                        $("#allocation_div_1").css('display','none');
                        $("#allocation_plan_div1").css('display','block');
                        $("#chart_storage").css('display','none');
                        $("#chart_hostgroup").css('display','none');
                        $("#tab_iostat").css('display','none');
                        $("#chart_iostat").css('display','none');
                    }else if ($(this).parents('li').attr("id") == "allocation"){
                        $("#tab_3").css('display','none');
                        $("#tab_3_1").css('display','none');
                        $("#tab_3_2").css('display','block');
                        $("#allocation_div_1").css('display','block');
                        $("#allocation_plan_div1").css('display','block')
                        $("#chart_storage").css('display','none');
                        $("#chart_hostgroup").css('display','none');
                        $("#tab_iostat").css('display','none');
                        $("#chart_iostat").css('display','none');

                    }else if ($(this).parents('li').attr("id") == "iostatlog_li"){
                        $("#tab_3").css('display','none');
                        $("#tab_3_1").css('display','none');
                        $("#tab_3_2").css('display','none');
                        $("#allocation_div_1").css('display','none');
                        $("#allocation_plan_div1").css('display','none')
                        $("#chart_storage").css('display','none');
                        $("#chart_hostgroup").css('display','none');
                        window.open("iostatloginit");
                        //$("#tab_iostat").css('display','block');
                        //$("#chart_iostat").css('display','block');
                        
                    }else if($(this).parents('li').attr("id") == "topology_li"){
                        $("#tab_3").css('display','none');
                        $("#tab_3_1").css('display','none');
                        $("#tab_3_2").css('display','none');
                        $("#allocation_div_1").css('display','none');
                        $("#allocation_plan_div1").css('display','none')
                        $("#chart_storage").css('display','none');
                        $("#chart_hostgroup").css('display','none');
                        window.open("topology");
                    }else if($(this).parents('li').attr("id") == "savestoragelist_li"){
                        $("#tab_3").css('display','none');
                        $("#tab_3_1").css('display','none');
                        $("#tab_3_2").css('display','none');
                        $("#allocation_div_1").css('display','none');
                        $("#allocation_plan_div1").css('display','none')
                        $("#chart_storage").css('display','none');
                        $("#chart_hostgroup").css('display','none');
                        $("#savestoragelist_div").css('display','block')
                        $("#storage_name").val("")
                        $("#storage_serial").val("")
                        $("#storage_option").val("")
                        $("#storage_postion").val("")
                    }else {
                        var storage = $(this).text();
                        oTable.settings()[0].ajax.data['param'] = storage;
                        oTable.ajax.url('/getstorageinfo/').load();
                        oTable_ldevlist.settings()[0].ajax.data['param'] = storage;
                        oTable_ldevlist.ajax.url('/getldevlist/').load();
                        $("#tab_3_2").css('display','block');
                        $("#allocation_div_1").css('display','none');
                        $("#allocation_plan_div1").css('display','none');
                        $("#chart_storage").css('display','block');
                        $("#chart_hostgroup").css('display','block');
                        $("#tab_iostat").css('display','none');
                        $("#chart_iostat").css('display','none');

                        updatechartstorage(storage);
                        updatechartldev(storage);
                        updatecharthostgroup(storage);
                    }

                }else{
                    if (storage_type != "function_zone"){
                        oTable.settings()[0].ajax.data['param'] = storage_type;
                        oTable.ajax.url('/getstoragelistbytype/').load();
                        $("#tab_3").css('display','block');
                        $("#tab_3_1").css('display','none');
                        $("#tab_3_2").css('display','none');
                        $("#allocation_div_1").css('display','none');
                        $("#allocation_plan_div1").css('display','none');
                        $("#chart_storage").css('display','none');
                        $("#chart_hostgroup").css('display','none');
                        $("#tab_iostat").css('display','none');
                    }
                }

            });

            $('#storage_list_table tbody').on( 'click', 'a#login', function () {
                var data = oTable.row($(this).parents('tr')).data();
                window.open(data["ip"]);
            } );

            // handle the search submit
            $('.sidebar-search .submit').on('click', function (e) {
                e.preventDefault();
                var keyword = $('#search_input').val();
                oTable.settings()[0].ajax.data['param'] = keyword;
                oTable.ajax.url('/search/').load();
            });

            // handle the search query submit on enter press
            $('.page-sidebar').on('keypress', '.sidebar-search input', function (e) {
                if (e.which == 13) {
                    var keyword = $('#search_input').val();
                    oTable.settings()[0].ajax.data['param'] = keyword;
                    oTable.ajax.url('/search/').load();
                    return false; //<---- Add this line
                }
            });

            files_array = new Array("");
            $("#selectFile_a").on("change","input[type='file']",function(){
                var selectedfiles = $("#selectFile")[0].files;               
                $("p").remove();
                for (var i = selectedfiles.length - 1; i >= 0; i--) {
                    $("#tab_2_1").append("<p>" + selectedfiles[i].name + "</p>")
                    files_array[i] = selectedfiles[i].name
                }
                var form = new FormData($("#upload_conf_form")[0])
                $("#spinner_section").css("display","block");
                $.ajax({
                    url:"/uploadconf/",
                    type:'post',
                    data:form,
                    processData:false,
                    contentType:false,
                    success:function (result) {
                        $("#spinner_section").css("display","none");
                    }
                })
            });
            
            $("#createconf_button").click(function(){
                $("#spinner_section").css("display","block");
                    $.ajax({
                        type:"POST",
                        url:"/createconf/",
                        data:{"selectedfiles":JSON.stringify(files_array)},
                        traditional: true,
                        dataType:"json",
                        success:function(result){
                            $("#spinner_section").css("display","none");
                            if (result == "success") {
                                alert("完成！\n文件位置:\nstoragelist\\uploads\\gconf\\ldevlist_book.xlsx")
                            }else {
                                alert("失败!")
                            }
                            
                    }
                })
            });

            $("#importto_database_button").click(function(){
                $("#spinner_section").css("display","block");
                    $.ajax({
                        type:"POST",
                        url:"/importdb/",
                        data:{"selectedfiles":JSON.stringify(files_array)},
                        traditional: true,
                        dataType:"json",
                        success:function(result){
                            $("#spinner_section").css("display","none");
                            if (result == "success") {
                                alert("完成！")
                            }else {
                                alert("失败!")
                            }
                            
                    }
                })
            });

            $("#allocation_submit").click(function(){
                var hostgroup_name = $("#hostgroup").val()
                var data = $("#data").val()
                var binlog = $("#binlog").val()
                var relaylog = $("#relaylog").val()
                var redolog = $("#redolog").val()
                oTable_ldevlist.settings()[0].ajax.data['hostgroup'] = hostgroup_name;
                oTable_ldevlist.settings()[0].ajax.data['data'] = data;
                oTable_ldevlist.settings()[0].ajax.data['binlog'] = binlog;
                oTable_ldevlist.settings()[0].ajax.data['relaylog'] = relaylog;
                oTable_ldevlist.settings()[0].ajax.data['redolog'] = redolog;
                oTable_ldevlist.ajax.url('/allocation/').load();
            });

            $("#save_storagelist_submit").click(function(){
                var storage_type =  String($("#storage_type_select option:selected").attr("name"))
                var storage_name = $("#storage_name").val()
                var storage_serial = $("#storage_serial").val()
                var storage_option = $("#storage_option").val()
                var storage_postion = $("#storage_postion").val()
                if (storage_name!="" && storage_type!="" && storage_serial!="" ){
                    $.ajax({
                        type:"POST",
                        url:"/savestoragelist/",
                        data:{
                            "storage_type" : storage_type,
                            "storage_name":storage_name,
                            "storage_serial":storage_serial,
                            "storage_option":storage_option,
                            "storage_postion":storage_postion
                        },
                        traditional: true,
                        success:function(result){
                            if (result == "success"){
                                alert("添加成功")
                                location.reload()
                            }else{
                                alert("添加失败，请确认存储名/序列号没有重复添加！")
                            }
                        }
                    })
                }else {
                    alert("必填项不能为空")
                }

            });

            $("#save_storagelist_cancel").click(function(){
                $("#storage_name").val("")
                $("#storage_serial").val("")
                $("#storage_option").val("")
                $("#storage_postion").val("")
            });
        }

    };

}();

var chart_storage = null;
var chart_ldev = null;
var chart_hostgroup = null;

jQuery(document).ready(function() {    
    chart_storage = Highcharts.chart('chart_1', {
            // Highcharts 配置
                chart: {
                    type: 'pie'
                },
                title: {
                    text: '存储空间使用情况'
                },
                subtitle: {
                    text: ''  
                },
                tooltip: {
                    headerFormat: '',
                    pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {point.name}</b><br/>' +
                    '<b>{point.y} GB</b><br/>'
                },
                 colors: [ '#2b908f',  '#f45b5b','#8085e9', '#f15c80', '#e4d354', '#8085e8', '#8d4653', '#91e8e1'],
                plotOptions: {
                    pie:{
                        showInLegend: true,
                        dataLabels:{
                            enabled:true,
                            formatter: function() {
                        //this 为当前的点（扇区）对象，可以通过  console.log(this) 来查看详细信息
                              return '<span style="color: ' + this.point.color + '"> ' + this.y +' GB</span>';
                           }
                        }
                    }
                },
                series:[{
                    data:[]
                }]
    });

    chart_ldev = Highcharts.chart('chart_2', {
            // Highcharts 配置
                chart: {
                    type: 'bar'
                },
                title: {
                    text: 'LDEV使用情况'
                },
                xAxis: {
                    categories: []
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'LDEV使用情况'
                    }
                },
                legend: {
                    reversed: false
                },
                colors: [ '#f45b5b','#2b908f',  '#8085e9', '#f15c80', '#e4d354', '#8085e8', '#8d4653', '#91e8e1'],
                plotOptions: {
                    series: {
                        stacking: 'normal'
                    },
                    bar:{
                        dataLabels:{
                            enabled:true
                        }
                    }
                },
                series: []
    });

    chart_hostgroup = Highcharts.chart('chart_1_1', {
            // Highcharts 配置
                 chart: {
                    type: 'column'
                },
                title: {
                    text: '主机上LDEV使用情况'
                },
                xAxis: {
                    categories: [],
                    crosshair: true
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: '使用个数'
                    }
                },

                tooltip: {
                    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f}个</b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
                },
                plotOptions: {
                    column: {
                        borderWidth: 0,
                        dataLabels:{
                            enabled:true
                        }
                    }
                },
                colors: ['#273446', '#68808E', '#D29B8E', '#75989F'],
                series: []
    });

})

var updatechartstorage = function (arg){
    storage_name = arg
    $.ajax({
        type:"POST",
        url:"/updatechartstorage/",
        data:{"storage_name":storage_name},
        traditional: true,
        dataType:"json",
        success:function(result){
            while(chart_storage.series.length > 0) {
                    chart_storage.series[0].remove(false);
            }
            chart_storage.redraw();
            chart_storage.addSeries({},false);
            for (var i = 0; i < result.length; i++) {
                chart_storage.series[0].addPoint({name: result[i].name,y: result[i].y}, true);
            }
            chart_storage.redraw();
        }
    })    
}

var updatechartldev = function (arg){
    storage_name=arg 
    $.ajax({
        type:"POST",
        url:"/updatechartldev/",
        data:{"storage_name":storage_name},
        traditional: true,
        dataType:"json",
        success:function(result){
            while(chart_ldev.series.length > 0) {
                    chart_ldev.series[0].remove(false);
            }
            chart_ldev.redraw();
            chart_ldev.xAxis[0].setCategories(result.xaxis)
            chart_ldev.addSeries({name:"已使用",data : result.data[0]},false);
            chart_ldev.addSeries({name:"未使用",data : result.data[1]},false);
            chart_ldev.redraw();
        }
    }) 
}

var updatecharthostgroup = function(arg){
    storage_name=arg
    $.ajax({
        type:"POST",
        url:"/updatecharthostgroup/",
        data:{"storage_name":storage_name},
        traditional: true,
        dataType:"json",
        success:function(result){
            while(chart_hostgroup.series.length > 0) {
                    chart_hostgroup.series[0].remove(false);
            }
            chart_hostgroup.redraw()
            chart_hostgroup.xAxis[0].setCategories(result.xaxis)
            for (var i=0 ; i< result.name.length; i++){
                chart_hostgroup.addSeries({name : result.name[i],data : result.data[i]},false);
            }
            chart_hostgroup.redraw();
        }
    }) 
}


