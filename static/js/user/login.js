function pwd_md5() {

        var password = $('#u_password').val();
        console.log(password);
        var new_password = md5(password);
        console.log(new_password);
        $('#u_password').val(new_password);
    }