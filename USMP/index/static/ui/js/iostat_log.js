/**
Core script to handle the entire layout and base functions
**/
var option = {
    tooltip: {
        trigger: 'axis',
        position: function (pt) {
            return [pt[0], '10%'];
        }
    },
    title:{
        left:'center'
    },
    toolbox: {
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%']
    },
    dataZoom: [{
        type: 'inside',
        start: 0,
        end: 10
    },{
        start: 0,
        end: 10,
        handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
        handleSize: '80%',
        handleStyle: {
            color: '#fff',
            shadowBlur: 3,
            shadowColor: 'rgba(0, 0, 0, 0.6)',
            shadowOffsetX: 2,
            shadowOffsetY: 2
        }
    }],
    series: []
}
var iostatlog
var myChart ;

var iostat_log = function(){
	return {
		init : function() {
		    files_array = new Array("");
		    myChart = echarts.init(document.getElementById('chart_iostat'));
			$("#span_selectFile").on("change","#iostat_selectFile",function(){
                var selectedfiles = $("#iostat_selectFile")[0].files;
                $("#div_selectFile p").remove();
                for (var i = selectedfiles.length - 1; i >= 0; i--) {
                    files_array[i] = selectedfiles[i].name
                }
                myChart.showLoading();
                var form = new FormData($("#form-iostatlog-update")[0]);
                $.ajax({
                    url:'/upload/',
                    type:'post',
                    data:form,
                    processData:false,
                    contentType:false,
                    success:function (result) {
                        $.ajax({
                            type:"POST",
                            url:"/getiostatoption/",
                            data:{
                                "filename" : selectedfiles[0].name
                            },
                            traditional:true,
                            dataType:"json",
                            success:function(result){
                                if (result != "failed") {
                                    myChart.hideLoading();
                                    $("option").remove();
                                    for (var i = result.disk.length - 1; i >= 0; i--) {
                                        $("#disk_select").append("<option>" + result.disk[i] + "</option>")
                                    }
                                    for (var i = result.option.length - 1; i >= 0; i--) {
                                        $("#option_select").append("<option>" + result.option[i] + "</option>")
                                    }
                                }else{
                                    alert("获取参数失败！")
                                    myChart.hideLoading();
                                    $("option").remove();
                                }

                            }
                        })
                    }
                })
            });

			/* 显示IOSTAT图 */
            $("#iostat_button").click(function(){
                myChart.showLoading();
                option.series=[];
                var selectedValues=[];
                $("#disk_select :selected").each(function () {
                    selectedValues.push($(this).val())
                });
                var disk_option = String($("#option_select option:selected").val())
                $.ajax({
                        type:"POST",
                        url:"/getiostatlog/",
                        data:{
                            "disks" : selectedValues,
                            "option" : disk_option
                        },
                        traditional: true,
                        dataType:"json",
                        success:function(result){
                            myChart.hideLoading();
                            option.xAxis.data = result.date;
                            option.title.text = disk_option;
                            for (var i=0 ;i<selectedValues.length;i++){
                                var item = {
                                    type:'line',
                                    smooth:true,
                                    symbol: 'none',
                                    sampling: 'average',
                                    name : selectedValues[i],
                                    data : result[selectedValues[i]]
                                };
                                option.series.push(item)
                            }
                            myChart.setOption(option,true)
                        }
                })

            });

		} //init
	}; //return 

}(); //iostat_log




