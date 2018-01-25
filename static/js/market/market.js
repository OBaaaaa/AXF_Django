$(function () {
    $("#all_type").click(function () {
        $("#all_type_detail").css('display','block');
    });
    $("#all_type_detail").click(function () {
        $(this).css('display','none');
    });

    $('#order_rule').click(function () {
        $('#order_rule_detail').css('display','block');
    });

    $('#order_rule_detail').click(function () {
        $(this).css('display','none');
    });




    $('.add_goods').click(function () {
        var current_node = $(this);
        var goods_id = current_node.attr('goods_id');

        $.getJSON('/app/addgoods/',{'goods_id':goods_id},function (data) {
            console.log(data);
            if (data['status'] == '200'){
                console.log(111)
                if (current_node.has('span')){

                }else {

                }
                var span = current_node.prev('span');
                span.html(data['goods_num'])
            }else if(data['status']=='901'){
                window.open('/app/login/',target = '_self')
            }

        })
    })

        $('.sub_goods').click(function () {
        var current_node = $(this)
        var goods_id = current_node.attr('goods_id');
        $.getJSON('/app/subgoods/',{'goods_id':goods_id},function (data) {
            console.log(data);
            if (data['status'] == '200'){
                console.log(222)
                var span = current_node.next('span');
                span.html(data['goods_num'])
            }else if(data['status']=='901'){
                window.open('/app/login/',target = '_self')
            }

        })
    })

})