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


    $("#J_btnAddCart").bind("click",function(){
        id = $("#productId").val()
        num = 1;
        $.get("/cart/add",
        {"id":id,"num":num},
        function(data){
          var obj = $.parseJSON(data)
          if(obj.rsp== "1"){
            alert('添加成功！')
           }else if(obj.rsp == 3){
             alert('请先登陆')
             window.location.href ="/login"
            }
        })
    })

    $("#buy").bind("click",function(){
        var id = $("#productId").val()
        $.get("/myorder",
        {"id":id},
        function(data){
          var obj = $.parseJSON(data)
          if(obj.rsp== "1"){
            alert('添加成功！')
            window.location.href ="/cart/delall"
           }else if(obj.rsp == 2){
                alert('请添加收货地址')
                window.location.href ="/addres/list"
           }
           else if(obj.rsp == 3){
             alert("商品订单生成失败！")
             window.location.href ="/details?id="+id
            }
        })
    })
})