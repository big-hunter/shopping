/*my own shop 折扣店 sep.27*/
$(function(){(
  /*-----------幻灯片start------------*/
   function(){
		var curr = 0;
		$("#jsNav .trigger").each(function(i){
			$(this).click(function(){
				curr = i;
				$("#js img").eq(i).fadeIn("slow").siblings("img").hide();
				$(this).siblings(".trigger").removeClass("imgSelected").end().addClass("imgSelected");
				return false;
			});
		});
		
		var pg = function(flag){
			if (flag) {
				if (curr == 0) {
					todo = 4;
				} else {
					todo = (curr - 1) % 5;
				}
			} else {
				todo = (curr + 1) % 5;
			}
			$("#jsNav .trigger").eq(todo).click();
		};
		
		//ǰ
		$("#prev").click(function(){
			pg(true);
			return false;
		});
		
		//
		$("#next").click(function(){
			pg(false);
			return false;
		});
		
		//Զ
		var timer = setInterval(function(){
			todo = (curr + 1) % 5;
			$("#jsNav .trigger").eq(todo).click();
		},2000);
		
		$("#js,#prev,#next").hover(function(){
				clearInterval(timer);
			},
			function(){
				timer = setInterval(function(){
					todo = (curr + 1) % 5;
					$("#jsNav .trigger").eq(todo).click();
				},2000);			
			}
		);
	})();
	
	 /*-----------幻灯片end------------*/
	 
	 
	 	
	 /*-----------首页变色start-----------*/
	 $(".look").hover(function(){
	 $(this).addClass("changecolor");
	 },
	 function(){
	 $(this).removeClass("changecolor");
	 });
	 
});
 /*-----------首页变色end-----------*/
  /*-----------注册界面提醒-----------*/
$(function(){
    $(".spsearch span").hide();
$("input.spnormal").focus(function(){

    $(this).next().show();
});
$(".spnormal").blur(function(){
    console.log("k");
    $(this).next().hide();
});
});

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


$(document).ready(function(){
  var username = getCookie("username")
   if(username){
       $("[data-model='login']").text(username)
       $("[data-model='login']").attr("href","#")
   }
   // data-click="{{good.id}}"
   $("[data-click]").bind("click",function(){
        var _this = this
        $.ajax({
            type:"GET",
            url:"/good/click/", // 请求路径
            //async:false,
            data:{"good_id": String( _this.name) },
            success : function(data){
               if(data.rsp == '1'){
                  console.log("anonymous")
               }else{
                  console.log("clicked")
               }
            },
            error: function(){
                console.log("console error")
            }
        })

   })


    $("#highTolow").bind("click",function(){
        var type = getQueryVariable("type")
        var  page = getQueryVariable("page")
        if (page != undefined || page !=""){
            window.location.href = "/goodslist/?type="+type+"&&page="+page+"&&price=1"
        } else{
            window.location.href = "/goodslist/?type="+type+"&&price=1"
        }
    });
    $("#discount").bind("click",function(){
        var type = getQueryVariable("type")
       var  page = getQueryVariable("page")
         if(page != undefined || page !=""){
             window.location.href = "/goodslist/?type="+type+"&&page="+page+"&&discount="+discount
        }
        else{
            window.location.href = "/goodslist/?type="+type+"&&price=1"
        }
    });

    $("#popar").bind("click",function(){
        var type = getQueryVariable("type")
         var  page = getQueryVariable("page")
        if (page != undefined || page !=""){
            window.location.href = "/goodslist/?type="+type+"&&page="+page+"&&popar=1"
        } else{
           window.location.href = "/goodslist/?type="+type+"&&popar=1"
        }
    });
})

/*-----------注册界面提醒end-----------*/
