/**
main function to initiate template pages by self
**/

var cluster = $('#min_title_list',parent.document).children('li.active').text();

/* 获取volume 详细信息 */
function getVolumeFullInfo (){
    $('#NasInfoDataTable').DataTable({
        "ajax" : {
            "url" : "/getvolumefullinfo/",
            "type" : "POST",
            "data" : {
                "param" : cluster
            },
            "dataType" : "json"
        },
        "columns" : [
            {"data" : "cluster"},
            {"data" : "node"},
            {"data" : "vserver"},
            {"data" : "aggregate"},
            {"data" : "volume"},
            {"data" : "vol_size"},
            {"data" : "vol_usedsize"},
            {"data" : "vol_availsize"}
            ]
    });
};

/* 获取volume使用率 column图 */
function getUsedPercentOfVolume(chart_usedPercentOfVolume){
    $.ajax({
        type:"POST",
        url:"/getUsedPercentOfVolume/",
        data:{"cluster_name":cluster},
        traditional: true,
        dataType:"json",
        success:function(result){
            if (result != "failed") {
                chart_usedPercentOfVolume.xAxis[0].setCategories(result.xaxis);
                chart_usedPercentOfVolume.addSeries({name : "使用率（%）",data : result.percent},false);
                chart_usedPercentOfVolume.addSeries({name : "总体容量(GB)",data : result.size},false).hide();
                chart_usedPercentOfVolume.addSeries({name : "已用容量(GB)",data : result.used},false).hide();
                chart_usedPercentOfVolume.redraw();
            }else {
                alert('获取信息失败');
            }

        }
    })
};

/* 获取aggr使用率 column图 */
function getUsedPercentOfAggr(chart_usedPercentOfAggr){
    $.ajax({
        type:"POST",
        url:"/getUsedPercentOfAggr/",
        data:{"cluster_name":cluster},
        traditional: true,
        dataType:"json",
        success:function(result){
            if (result != "failed") {
                chart_usedPercentOfAggr.xAxis[0].setCategories(result.xaxis);
                chart_usedPercentOfAggr.addSeries({name : "使用率（%）",data : result.percent},false);
                chart_usedPercentOfAggr.addSeries({name : "总体容量(GB)",data : result.size},false).hide();
                chart_usedPercentOfAggr.addSeries({name : "已用容量(GB)",data : result.used},false).hide();
                chart_usedPercentOfAggr.redraw();
            }else {
                alert('获取信息失败');
            }

        }
    })
};

/* 获取集群概要信息 */
function getNasClusterInfo(){
    $.ajax({
        type:"POST",
        url:"/getnasclusterinfo/",
        data:{"cluster_name":cluster},
        traditional: true,
        dataType:"json",
        success:function(result){
            $("#node_list").text(result.node_list);
            $("#aggr_list").text(result.aggr_list);
            $("#svm_list").text(result.svm_list);
            $("#vol_count").text(result.vol_count);
        }
    })
};

function getNasTopology(){
    $('#clusterInfoDataTable tbody').on( 'click', 'a#checktopology', function () {
        alert("功能尚未开放")
        //creatIframeByButton('getnastopology',cluster);
    });
}

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