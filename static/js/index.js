jQuery(document).ready(function($){
    $('.nav__item').click(function () {     // 导航
        $(this).addClass('on').siblings().removeClass('on');
    })
    
    Echo.init({     //图片延迟加载
        offset: 500,
        throttle: 0
    });
    
    $('.flexslider1').flexslider({      // 轮播
        animation: "fade",
        slideshow: false,
        controlNav: false,
        directionNav: false 
        
    });
    $('.flexslider2').flexslider({      // 轮播
        animation: "slide",
        animationLoop: true,
        itemWidth: 185,
        controlNav: false,
        pauseOnHover: true,
        maxItems: 6
    });
      
    $(".parallax").parallax({       // 视差滚动
        'speed': 50
    });
    
    // 动态打字效果
    var inputing = new typer('inputing');
    inputing.end().type(200).type('这是个啥子网站？').end().type(2000).del()
    inputing.type('这是个very神奇的页面，').del(3).type(300).type('网站。').end().type(2500)
    inputing.del().type('哪里神奇了？').end().type(2570)
    inputing.del().type('我说神奇就神奇！！！').end().type(1830).del().repeat()
    
    var wow = new WOW({     // 添加动效
        boxClass:     'wow',
        animateClass: 'animated',
        offset:       0,
        mobile:       true,
        live:         true,
        callback:     function(box) {
        },
        scrollContainer: null
    });
    wow.init(); 
    
    $('#form').validator({      // 表单验证
        fields: {
            'url': 'url',
            'name': 'required',
            'tel': 'required;mobile',
            'qq': 'required;qq'
        },
        theme: 'simple_bottom',
        msgStyle: "position: relative; top: -34px; left:40px;",
        invalid: function () {
            console.log('valid fail');
        },
        valid: function (e) {
            var url = $('input[name="url"]').val();
            var name = $('input[name="name"]').val();
            var mobile = $('input[name="mobile"]').val();
            var qq = $('input[name="qq"]').val();
            var wangwang = $('input[name="wangwang"]').val();
            console.log(url + ', '+ name + ', ' + mobile + ', ' + qq + ', ' + wangwang + ', ');
            $.ajax({
                url: '/',
                dataType: 'json',
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    url: url,
                    name: name,
                    tel: mobile,
                    qq: qq,
                    wangwang: wangwang
                },
                success: function (ret) {
                    if (ret.code == 0) {
                        alert('提交成功');
                    } else {
                        console.log(ret);
                        alert(ret.msg);
                    }
                },
                error: function () {
                    alert('网络错误')
                }
            })
        }
    });
});