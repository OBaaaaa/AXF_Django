$(function () {
    $('#u_username').change(function () {
        var username = $(this).val();

        $.getJSON('/app/usernamecheck/',{'username':username},function (data) {
            var status = data['status'];

            if (status == '200'){
                $('#u_info').html(data['msg']);
                $('#u_info').addClass('user_check_success').removeClass('user_check_fail');
            }else {
                $('#u_info').html(data['msg']);
                $('#u_info').removeClass('user_check_success').addClass('user_check_fail');
            }
        })

    })


    $('#u_confirm_password').change(function () {
        var confirm_password = $(this).val();
        var password = $('#u_password').val();
        if (password==confirm_password){
            $('#cp_info').html('两次密码一致');
            $('#cp_info').css('color','green')
        }else {
            $('#cp_info').html('密码不一致');
            $('#cp_info').css('color','red')
        }
    })
    


})
function pwd_md5() {

        var password = $('#u_password').val();
        console.log(password);
        var new_password = md5(password);
        console.log(new_password);
        $('#u_password').val(new_password);
    }