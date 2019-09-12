/**
main function to initiate template pages by self
**/
/*document.write("<script language=javascript src='../h-ui.admin/js/H-ui.admin.js'></script>")*/
var storage_serial = $('#min_title_list',parent.document).children('li.active').text();

/* 获取某台存储上的LDEV信息 */
function initStorageLdevDataTable(){
    var ldevInfoTable = $('#ldevInfoDataTable').dataTable({
        "destroy": true,
        "iDisplayLength": 10,
        "sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
        "ajax" : {
            "url" : "/getldevlist/",
            "type" : "POST",
            "data" : {
                "param" : storage_serial
            },
            "dataType" : "json"
        },
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
}

$('a#gettopology').on( 'click',function () {
    creatIframeByButton('topology',storage_serial)
});

/* 获取某台存储上总体使用率 饼图*/
function updatePercentOfused_pie(chart_storage){
    $.ajax({
        type:"POST",
        url:"/updatePercentOfused_pie/",
        data:{"storage_serial":storage_serial},
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
};

/* 获取存储总体使用率 bart图*/
function updateInfoOfused_bar(chart_ldev){
    $.ajax({
        type:"POST",
        url:"/updateInfoOfused_bar/",
        data:{"storage_serial":storage_serial},
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
};

/* 获取存储上hostgroup使用ldev情况 column图*/
function updateInfoOfLdev_column(chart_hostgroup){
    $.ajax({
        type:"POST",
        url:"/updateInfoOfLdev_column/",
        data:{"storage_serial":storage_serial},
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
};

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











