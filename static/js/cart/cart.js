$(function () {
    $('.subShopping').click(function () {
        var current_node = $(this);
        var goods_id = current_node.attr('goods_id');
        $.getJSON('/app/subshopping/', {'goods_id': goods_id}, function (data) {
            console.log(data);
            if (data['status'] == '200') {
                current_node.next('span').html(data['goods_num']);
            } else if (data['status'] == '400') {
                current_node.parents('li').remove();
            }
        })
    })

    $('.addShopping').click(function () {
        var current_node = $(this);
        var goods_id = current_node.attr('goods_id');
        $.getJSON('/app/addshopping/', {'goods_id': goods_id}, function (data) {
            console.log(data);
            if (data['status'] == '200') {
                current_node.prev('span').html(data['goods_num']);
            } else if (data['status'] == '400') {
                current_node.parents('li').remove();
            }


        })
    })


    $('.ischose').click(function () {
        var current_node = $(this);
        var li_node = current_node.parents('li');
        var goods_id = li_node.attr('goods_id');
        $.getJSON('/app/changecheck/', {'goods_id': goods_id}, function (data) {
            console.log(data)
            if (data['status'] == '200') {
                current_node.find('span').toggle()
            }
        })


    })

    $('#ok').click(function () {
        var menu_list = $('.menuList');

        var good_id_list = [];

        for (var i = 0; i < menu_list.length; i++) {
            var status = menu_list.eq(i).find('.ischose span').css('display');


            if (status == 'block') {
                good_id_list.push(menu_list.eq(i).attr('goods_id'));
            }
        }


        if (good_id_list.length == 0) {

            alert('NONONO')

        } else {


            $.getJSON('/app/makeorder/', {'good_id_list': good_id_list.join('#')}, function (data) {

                console.log(data)
                if (data['status'] == '200') {
                    window.open('/app/getorder/?order_id='+data['order_id'],target='_self')
                }
            })
        }


    })


});