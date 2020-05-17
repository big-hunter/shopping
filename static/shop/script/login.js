/*my own shop 折扣店 sep.27*/
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
    $("#login").bind("click", function(){
        var username = $('[data-model=username]').val()
        var password = $('[data-model=password]').val()
        if (username =="" || username == undefined){
            alert("输入密码")
            return
          }
        var data = {
            "username" : username,
            "password" : password
        }
        $.ajax({
            type:"POST", // 请求类型 GET/POST
            url:"/login/", // 请求路径
            dataType:"json",
            data:JSON.stringify(data),
            success : function(data){
                console.log(data)
                window.location.href = "/"
            },
            error: function(){
                alert("登陆失败")
            }
	    })
    })
})

