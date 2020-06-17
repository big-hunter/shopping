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
            window.location.href ="/cart/details"
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
    var full_img = $("#full").attr("src") //04
    var path_arr = full_img.split("/")
    var last_str = path_arr[path_arr.length -1]

    //03 back
    var back_path  = last_str.replace("4_full","3_back")
    var back_related = full_img.replace(last_str, back_path)
    console.log(back_related)
    $("#back").attr("src",back_related)

    //02 side
    var side_path  = last_str.replace("4_full","2_side")
    var side_related = full_img.replace(last_str, side_path)
    console.log(side_related)
    $("#side").attr("src",side_related)

    var additional_path  = last_str.replace("4_full","7_additional")
    var additional_related = full_img.replace(last_str, additional_path)
    console.log(additional_related)
    $("#additonal").attr("src",additional_related)//07 additonal.jpg

    function getQueryVariable(variable)
    {
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
    }
    var goodid = getQueryVariable("id")
    $.ajax({
        type:"GET",
        url:"/good/rec/?goodid="+goodid, // 请求路径
        dataType:"json",
        success : function(data){
            console.log(data)
            if (data.length <4){
                  for(var i = 0; i < data.length ; i++){
                    console.log("#rec_img"+String(i))
                    $("#rec_img"+String(i)).attr('src' ,data[i].pic)
                    $(".good_item"+String(i)).attr('href' ,"/details/?id="+data[i].id)
                  }
            }else{
                  for(var i = 0; i <4 ; i++){
                    $("#rec_img"+String(i)).attr('src' ,data[i].pic)
                    $(".good_item"+String(i)).attr('href' ,"/details/?id="+data[i].id)
                  }
            }

        },
        error: function(){
              console.log("rec error")
        }
    })


})