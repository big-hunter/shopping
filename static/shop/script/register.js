
$(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        })
    $("#register").bind("click", function(){

        var username = $('[data-model=username]').val()
        var password1 = $('[data-model=password1]').val()
        var password2 = $('[data-model=password2]').val()
        if (username =="" || username == undefined
          || password1 == "" ||  password1== undefined
          || password2 == "" ||  password2 == undefined){
            alert("请完善信息")
            return
          }
        if (password1 != password2){
            alert("两次密码不同")
            return
        }
        var data = {
            "username" : username,
            "password" : password1
        }
        $.ajax({
            type:"POST", // 请求类型 GET/POST
            url:"/register/", // 请求路径
            dataType:"json",
            data:JSON.stringify(data),
            success : function(data){
                console.log(data)
                window.location.href = "/login"
            },
            error: function(){
                alert("注册失败")
            }
	    })
    })
})

