/**
main function to initiate template pages by self
**/
/*document.write("<script language=javascript src='../h-ui.admin/js/H-ui.admin.js'></script>")*/
var storage_name = $('#min_title_list',parent.document).children('li.active').text();

/* 更新左侧导航栏 */
function initSiderbarMenu () {
    $.ajax({
        type:"POST",
        url:"/initindexbar/",
        data:{"flag":true},
        dataType:"json",
        success:function(result){
            for (var i = 0 ;i<result.hds_storage_list.length ; i++){
                $('#hds_storage_sidebar').append("<li><a data-href=\"gotostorageinfopage/?storage=" + result.hds_storage_list[i] + "\" data-title=\"" + result.hds_storage_list[i]+"\" href=\"javascript:void(0)\">"+result.hds_storage_list[i]+"</a></li>");
            }
            for (var i = 0 ;i<result.nas_cluster_list.length ; i++){
                $('#netapp_nas_sidebar').append("<li><a data-href=\"gotonasclusterinfopage/?cluster=" + result.nas_cluster_list[i] + "\" data-title=\"" + result.nas_cluster_list[i]+"\" href=\"javascript:void(0)\">"+result.nas_cluster_list[i]+"</a></li>");
            }
        }
    });
};

/* 获取welcome页面数据 */
/**
function initWelcomeDataTable (){
    var welcome_table = $('#welcomeDataTable').DataTable({
        "ajax" : {
            "url" : "/getallstorageinfo/",
            "type" : "POST",
            "data" : {
                "param" : "all"
            },
            "dataType" : "json"
        },
        "columnDefs" : [{
            "targets" : -1,
            "data" : null,
            "render" : function(data,type,row) {
                var html = "<a id='checktopology'>查看拓扑</a>";
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
            ]
    });

    $('#indexDataTable tbody').on( 'click', 'a#checktopology', function () {
        var data = welcome_table.row($(this).parents('tr')).data();
        creatIframeByButton('topology',data['serial']);
    });
};
**/
/*创建iframe*/
function creatIframeByButton(href,titleName){
	var topWindow=$(window.parent.document),
		show_nav=topWindow.find('#min_title_list'),
		iframe_box=topWindow.find('#iframe_box'),
		iframeBox=iframe_box.find('.show_iframe'),
		$tabNav = topWindow.find(".acrossTab"),
		$tabNavWp = topWindow.find(".Hui-tabNav-wp"),
		$tabNavmore =topWindow.find(".Hui-tabNav-more");
	var taballwidth=0;
	show_nav.find('li').removeClass("active");
	show_nav.append('<li class="active"><span data-href="'+href+'">'+titleName+'</span><i></i><em></em></li>');
	var $tabNavitem = topWindow.find(".acrossTab li");
	if (!$tabNav[0]){return}
	$tabNavitem.each(function(index, element) {
        taballwidth+=Number(parseFloat($(this).width()+60))
    });
	$tabNav.width(taballwidth+25);
	var w = $tabNavWp.width();
	if(taballwidth+25>w){
		$tabNavmore.show()}
	else{
		$tabNavmore.hide();
		$tabNav.css({left:0})
	}
	iframeBox.hide();
	iframe_box.append('<div class="show_iframe"><div class="loading"></div><iframe frameborder="0" src='+href+'></iframe></div>');
	var showBox=iframe_box.find('.show_iframe:visible');
	showBox.find('iframe').load(function(){
		showBox.find('.loading').hide();
	});
}

/* NAS配置上传/刷新数据库/创建配置EXCEL */
function nas_db_update(){
    $("#button_conform").click(function(){
        $("#spinner_section").css("display","block");
        $.ajax({
            type:"POST",
            url:"/updatenasdb/",
            data:{},
            traditional: true,
            dataType:"json",
            success:function(result){
                $("#spinner_section").css("display","none");
                if (result == "success") {
                    $("#div_input p").remove();
                    $("#div_input").append("<p>" + "刷新成功" + "</p>");
                }else if(result == "DeadLockHappened"){
                    $("#div_input").append("<p>" + "发生死锁" + "</p>");
                }else{
                    $("#div_input").append("<p>" + "刷新失败" + "</p>");
                }
            }
        })
    });

    $("#button_cancel").click(function(){
        layer_close();
    });
};

/* 存储配置上传/刷新数据库/创建配置EXCEL */
function storage_conf_update(){
    files_array = new Array("");
    $("#span_selectFile").on("change","input[type='file']",function(){
        var selectedfiles = $("#selectFile")[0].files;
        $("#div_selectFile p").remove();
        for (var i = selectedfiles.length - 1; i >= 0; i--) {
            $("#div_selectFile").append("<p>" + selectedfiles[i].name + "</p>")
            files_array[i] = selectedfiles[i].name
        }
        $("#spinner_section").css("display","block");
        var form = new FormData($("#form-storage-conf-update")[0])
        $.ajax({
            url:"",
            type:'post',
            data:form,
            processData:false,
            contentType:false,
            success:function () {
                $("#spinner_section").css("display","none");
                $("#uploadfile").val("");
                $("#div_selectFile").append("<p>" + "上传成功，请点击导入数据库/创建EXCEL文件" + "</p>")
            }
        })
    });

    $("#button_update").click(function(){
        $("#spinner_section").css("display","block");
        $.ajax({
            type:"POST",
            url:"/updatestoragedb/",
            data:{"selectedfiles":JSON.stringify(files_array)},
            traditional: true,
            dataType:"json",
            success:function(result){
                $("#spinner_section").css("display","none");
                if (result == "success") {
                    $("#uploadfile").val("");
                    $("#div_selectFile p").remove();
                    $("#div_selectFile").append("<p>" + "刷新数据库成功" + "</p>")
                }else {
                    $("#div_selectFile").append("<p>" + "刷新数据库失败" + "</p>")
                }
            }
        })
    });

    $("#button_create").click(function(){
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
                    $("#uploadfile").val("");
                    $("#div_selectFile p").remove();
                    $("#div_selectFile").append("<p>" + "创建EXCEL成功" + "</p>")
                }else {
                    $("#div_selectFile").append("<p>" + "创建EXCEL失败" + "</p>")
                }
            }
        })
    });
};









