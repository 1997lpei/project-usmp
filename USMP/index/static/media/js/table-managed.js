var TableManaged = function () {

    return {

        //main function to initiate the module
        init: function () {
            
            if (!jQuery().dataTable) {
                return;
            }
            // begin first table
            $('#examplelyc').DataTable( {
                "processing": true,
                "serverSide": true,
                "ajax": {
                    //"url" : "../../../static/arrays.txt"
                    "url" : "/getdata/",
                    "type" : "POST",
                   // "dataType" : "json",
                    //"success" : function(data){
                    //    alert(data[0].first_name)
                    //}
                },
                "columns": [
                { "data": "first_name" },
                { "data": "last_name" },
                { "data": "position" },
                { "data": "office" },
                { "data": "start_date" },
                { "data": "salary" }
                ]
            } );

        }
    };

}();