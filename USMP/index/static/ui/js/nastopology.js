/**
main function to initiate template pages by self
**/
var storage_serial = $('#min_title_list',parent.document).children('li.active').text();
function mute(node) {
    if (!~node.getAttribute('class').search(/muted/))
        node.setAttributeNS(null, 'class', node.getAttribute('class') + ' muted');
}
function unmute(node) {
    node.setAttributeNS(null, 'class', node.getAttribute('class').replace(/(\s|^)muted(\s|$)/g, '$2'));
}

/* 获取某台存储拓扑图 */
function get_topology(){
    $.ajax({
        type:"POST",
        url:"/gettopologydata/",
        data: {
            "storage" : storage_serial
        },
        traditional:true,
        dataType:"json",
        success:function(result){
            s = new sigma({
                graph: result,
                settings: {
                    enableHovering: false
                }
            });
            s.addRenderer({
                id: 'main',
                type: 'svg',
                container: document.getElementById('graph-container'),
                freeStyle: true
            });
            s.refresh();
            $('.sigma-node').click(function() {
                // Muting
                $('.sigma-node, .sigma-edge').each(function() {
                    mute(this);
                    });
                // Unmuting neighbors
                var neighbors = s.graph.neighborhood($(this).attr('data-node-id'));
                neighbors.nodes.forEach(function(node) {
                    unmute($('[data-node-id="' + node.id + '"]')[0]);
                    var neighbors_2 = s.graph.neighborhood(node.id)
                    neighbors_2.nodes.forEach(function(node2){
                        unmute($('[data-node-id="' + node2.id + '"]')[0]);
                        })
                    neighbors_2.edges.forEach(function(edge2){
                        unmute($('[data-edge-id="' + edge2.id + '"]')[0]);
                        })
                });
                neighbors.edges.forEach(function(edge) {
                    unmute($('[data-edge-id="' + edge.id + '"]')[0]);
                    });
                });
            s.bind('clickStage', function() {
                $('.sigma-node, .sigma-edge').each(function() {
                    unmute(this);
                });
            });
        }
    })
}