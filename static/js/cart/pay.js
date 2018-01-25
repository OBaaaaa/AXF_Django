$(function () {


    $('.pay').click(function () {

        var current_node = $(this);
        var order_id = current_node.attr('order_id');
        console.log(order_id)
        $.getJSON('/app/pay/',{'order_id':order_id},function (data) {
            if (data['status']=='200'){
                window.open('/app/mine/',target = '_self')

            }
        })


    })
})