// ------------------------------AJAX请求----------------------------------

$('#btn').chick(function () {
    $.ajax({
        url: '../../../NET/User/Query/FuzzyQuery.ashx?method=eotDL',//规定发送请求的 URL。默认是当前页面。
        data: { id: 'id', type: 'type' },//请求的参数
        headers: {      //设置请求头
            Accept: "application/json; charset=utf-8",
            token: "" + token  //这是获取的token
        },
        cache: false,//缓存，要求为Boolean类型的参数，默认为true（当dataType为script时，默认为false），设置为false将不会从浏览器缓存中加载请求信息。
        type: 'POST',//默认GET
        timeout: 2000,//超时 2秒后提示错误
        dataType: 'json',// json写了jquery会帮我们转换成数组或者对象 他已经用JSON.parse弄好了  预期的服务器响应的数据类型。
        contentType: "application/json",  //推荐写这个   发送数据到服务器时所使用的内容类型。默认是："application/x-www-form-urlencoded"。
        async: true,//默认异步

        //发送前
        beforeSend: function (request) {      //使用beforeSend添加请求头
            request.setRequestHeader("token", token);
            request.setRequestHeader("Content-Type", "application/json");

            // 发送之前就会进入这个函数
            // return false 这个ajax就停止了不会发 如果没有return false 就会继续
        },

        //请求完成（在请求成功或失败之后均调用，即在 success 和 error 函数之后。）
        complete: function (da) {
            $.messager.progress('close');
            $.messager.show({ title: '提示', msg: '下载完成！', timeout: 3000, showType: 'slide' });
        },

        // 成功拿到结果放到这个函数 data就是拿到的结果
        success: function (data, status) {

        },

        //失败，超时
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            if (textStatus === 'timeout') {
                alert('請求超時');
                setTimeout(function () {
                    alert('重新请求');
                }, 2000);
            }
        }

    });
});

// ----------------------------------------ajax data属性传值的方式总结---------------------------------------
// ①：属性加引号
// data: {"channelOrgCode": channelOrgCode }
// ②：属性也可以不加引号
data: { channelOrgCode: channelOrgCode }
// ③：拼接数据（拼接数据就不用像上面包在{}里面了）
data: "page=" + page + "&size=" + size + "&startDate=" + startDate + "&endDate=" + endDate
// ④：组装数据，然后赋值给一个变量，在用JSON.stringify(）把js对象转化为json字符串
var pList = [{ id: productId, ptType: ptType, num: num }];
$.ajax({
    url: "tdOrderController.do?addOrderItem",
    data: {
        pList: JSON.stringify(pList)
    },
    type: "post",
    dataType: "json",
    success: function (d) {
        if (!d.success) {
            mui.toast(d.msg);
            return false;
        } else {
            carNum();
        }
    }
});
// ⑤：也可以把data赋值给一个变量，在用JSON.parse()将json字符串转化为一个js对象
var dataTemp = {
    year: year,
    month: month,
    chooseNum: 1
};

$.ajax({
    url: "tdMonthlyPlanCTConfirmController.do?approveMonthlyPlan",
    type: 'post',
    data: dataTemp,
    dataType: "json",
    success: function (data) {
        var d = JSON.parse(data);
        if (d.success) {
            mui.toast(d.msg);
            centerSearch();
        } else {
            mui.toast(d.msg);
            return;
        }
    },
    error: function () {
        tip("客户端请求错误", 'error');
        return false;
    }
});





// -------------------------jQuery 语法------------------------

// $(this).hide() - 隐藏当前元素
// $("p").hide() - 隐藏所有 <p> 元素
// $("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素
// $("#test").hide() - 隐藏所有 id="test" 的元素

// 文档就绪事件
$(document).ready(function () {
    // 开始写 jQuery 代码...
});

// -------------------------选择器------------------------------
// 元素选择器
// $("p")
// #id 选择器
// $("#test")
// .class 选择器
// $(".test")

// 选取所有元素
// $("*")
// 选取当前 HTML 元素
// $(this)	
// 选取 class 为 intro 的 <p> 元素
// $("p.intro")
// 选取第一个 <p> 元素
// $("p:first")
// 选取第一个 <ul> 元素的第一个 <li> 元素
// $("ul li:first")
// 选取每个 <ul> 元素的第一个 <li> 元素
// $("ul li:first-child")
// 选取带有 href 属性的元素
// $("[href]")
// 选取所有 target 属性值等于 "_blank" 的 <a> 元素
// $("a[target='_blank']")
// 选取所有 target 属性值不等于 "_blank" 的 <a> 元素
// $("a[target!='_blank']")
// 选取所有 type="button" 的 <input> 元素 和 <button> 元素
// $(":button")
// 选取偶数位置的 <tr> 元素
// $("tr:even")
// 选取奇数位置的 <tr> 元素
// $("tr:odd")



// -------------------------------------常用的 jQuery 事件方法-------------------------------------
// click() 方法是当按钮点击事件被触发时会调用一个函数。
// click()
// 当双击元素时，会发生 dblclick 事件。
// dblclick()
// 当鼠标指针穿过元素时，会发生 mouseenter 事件。
// mouseenter()
// 当鼠标指针离开元素时，会发生 mouseleave 事件。
// mouseleave()
// 当鼠标指针移动到元素上方，并按下鼠标按键时，会发生 mousedown 事件。
// mousedown()
// 当在元素上松开鼠标按钮时，会发生 mouseup 事件。
// mouseup()
// hover()方法用于模拟光标悬停事件。
// hover()
// 当元素获得焦点时，发生 focus 事件。
// focus()
// 当元素失去焦点时，发生 blur 事件。
// blur()
// 键盘事件 按键事件
// keydown() - 键按下的过程
// keypress() - 键被按下
// keyup() - 键被松开
// keypress 事件不会触发所有的键（比如 ALT、CTRL、SHIFT、ESC）。请使用 keydown() 方法来检查这些键。
$("input").keypress(function (e) {
    if (e.which == 13) { //当回车键被按下
        console.log(e)
    };
});
// 当元素的值改变时发生 change 事件（仅适用于表单字段）。
// change() 
$("input").change(function () {
    console.log("文本已被修改");
});
// 注意：当用于 select 元素时，change 事件会在选择某个选项时发生。当用于 text field 或 text area 时，change 事件会在元素失去焦点时发生。


// ------------------------------------------jQuery 效果- 隐藏和显示--------------------------------
// jQuery hide() 和 show()
// 语法:
// $(selector).hide(speed,callback);
// $(selector).show(speed,callback);
// 实例
$(document).ready(function () {
    $(".hidebtn").click(function () {
        $("div").hide(1000, "linear", function () {  //第二个参数是一个字符串，表示过渡使用哪种缓动函数。（译者注：jQuery自身提供"linear" 和 "swing"，其他可以使用相关的插件）。
            alert("Hide() 方法已完成!");
        });
    });
});
// 通过 jQuery，您可以使用 toggle() 方法来切换 hide() 和 show() 方法。
// jQuery toggle()
// 语法:
// $(selector).toggle(speed,callback);
$("button").click(function () {
    $("p").toggle();
});

// -----------------------------------------jQuery - 链(Chaining)------------------------------------
// 下面的例子把 css()、slideUp() 和 slideDown() 链接在一起。"p1" 元素首先会变为红色，然后向上滑动，再然后向下滑动：
// 实例
$("#p1").css("color", "red").slideUp(2000).slideDown(2000);



// ----------------------------------------jQuery - 获取内容和属性----------------------------------------
// 获得内容 - text()、html() 以及 val()
// text() - 设置或返回所选元素的文本内容
// html() - 设置或返回所选元素的内容（包括 HTML 标记）
// val() - 设置或返回表单字段的值
// 下面的例子演示如何通过 jQuery text() 和 html() 方法来获得内容
$("#btn1").click(function () {
    alert("Text: " + $("#test").text());
});
$("#btn2").click(function () {
    alert("HTML: " + $("#test").html());
});

// 获取属性 - attr()
// 下面的例子演示如何获得链接中 href 属性的值：
// 实例
$("button").click(function () {
    alert($("#runoob").attr("href"));
});

// -------------------------------------------jQuery - 设置内容和属性--------------------------------
// 设置内容 - text()、html() 以及 val()
// text() - 设置或返回所选元素的文本内容
// html() - 设置或返回所选元素的内容（包括 HTML 标记）
// val() - 设置或返回表单字段的值
// 实例
$("#btn1").click(function () {
    $("#test1").text("Hello world!");
});
$("#btn2").click(function () {
    $("#test2").html("<b>Hello world!</b>");
});
$("#btn3").click(function () {
    $("#test3").val("RUNOOB");
});
// text()、html() 以及 val() 的回调函数
// 上面的三个 jQuery 方法：text()、html() 以及 val()，同样拥有回调函数。回调函数有两个参数：被选元素列表中当前元素的下标，以及原始（旧的）值。然后以函数新值返回您希望使用的字符串。
// 下面的例子演示带有回调函数的 text() 和 html()：
// 实例
$("#btn1").click(function () {
    $("#test1").text(function (i, origText) {
        return "旧文本: " + origText + " 新文本: Hello world! (index: " + i + ")";
    });
});
$("#btn2").click(function () {
    $("#test2").html(function (i, origText) {
        return "旧 html: " + origText + " 新 html: Hello <b>world!</b> (index: " + i + ")";
    });
});

// 设置属性 - attr()
// jQuery attr() 方法也用于设置/改变属性值。
// 下面的例子演示如何改变（设置）链接中 href 属性的值：
// 实例
$("button").click(function () {
    $("#runoob").attr("href", "http://www.runoob.com/jquery");
});
// attr() 方法也允许您同时设置多个属性。
// 下面的例子演示如何同时设置 href 和 title 属性：
// 实例
$("button").click(function () {
    $("#runoob").attr({
        "href": "http://www.runoob.com/jquery",
        "title": "jQuery 教程"
    });
});
// attr() 的回调函数
// jQuery 方法 attr()，也提供回调函数。回调函数有两个参数：被选元素列表中当前元素的下标，以及原始（旧的）值。然后以函数新值返回您希望使用的字符串。
// 下面的例子演示带有回调函数的 attr() 方法：
// 实例
$("button").click(function () {
    $("#runoob").attr("href", function (i, origValue) {
        return origValue + "/jquery";
    });
});

// -----------------------------------jQuery - 添加元素---------------------------------------
// 添加新的 HTML 内容
// 我们将学习用于添加新内容的四个 jQuery 方法：
// append() - 在被选元素的结尾插入内容
// prepend() - 在被选元素的开头插入内容
// after() - 在被选元素之后插入内容
// before() - 在被选元素之前插入内容
// jQuery append() 方法
// jQuery append() 方法在被选元素的结尾插入内容（仍然该元素的内部）。
// 实例
$("p").append("追加文本");
// jQuery prepend() 方法
// jQuery prepend() 方法在被选元素的开头插入内容。
// 实例
$("p").prepend("在开头追加文本");
// 通过 append() 和 prepend() 方法添加若干新元素
// 实例
function appendText() {
    var txt1 = "<p>文本。</p>";              // 使用 HTML 标签创建文本
    var txt2 = $("<p></p>").text("文本。");  // 使用 jQuery 创建文本
    var txt3 = document.createElement("p");
    txt3.innerHTML = "文本。";               // 使用 DOM 创建文本 text with DOM
    $("body").append(txt1, txt2, txt3);        // 追加新元素
}
// jQuery after() 和 before() 方法
// jQuery after() 方法在被选元素之后插入内容。
// jQuery before() 方法在被选元素之前插入内容。
// 实例
$("img").after("在后面添加文本");
$("img").before("在前面添加文本");
// 通过 after() 和 before() 方法添加若干新元素
// 实例
function afterText() {
    var txt1 = "<b>I </b>";                    // 使用 HTML 创建元素
    var txt2 = $("<i></i>").text("love ");     // 使用 jQuery 创建元素
    var txt3 = document.createElement("big");  // 使用 DOM 创建元素
    txt3.innerHTML = "jQuery!";
    $("img").after(txt1, txt2, txt3);          // 在图片后添加文本
}
// 总结：
// append/prepend 是在选择元素内部嵌入。
// after/before 是在元素外面追加。
// --------------------------------------------jQuery - 删除元素--------------------------------
// 删除元素/内容
// 如需删除元素和内容，一般可使用以下两个 jQuery 方法：
// remove() - 删除被选元素（及其子元素）
// empty() - 从被选元素中删除子元素
// jQuery remove() 方法
// jQuery remove() 方法删除被选元素及其子元素。
// 实例
$("#div1").remove();
// jQuery empty() 方法
// jQuery empty() 方法删除被选元素的子元素。
// 实例
$("#div1").empty();
// 过滤被删除的元素
// jQuery remove() 方法也可接受一个参数，允许您对被删元素进行过滤。
// 该参数可以是任何 jQuery 选择器的语法。
// 下面的例子删除 class="italic" 的所有 <p> 元素：
// 实例
$("p").remove(".italic");

// --------------------------------------------jQuery - 获取并设置 CSS 类------------------------------------
// jQuery 操作 CSS
// jQuery 拥有若干进行 CSS 操作的方法。我们将学习下面这些：
// addClass() - 向被选元素添加一个或多个类
// removeClass() - 从被选元素删除一个或多个类
// toggleClass() - 对被选元素进行添加/删除类的切换操作
// css() - 设置或返回样式属性
// jQuery addClass() 方法
// 下面的例子展示如何向不同的元素添加 class 属性。当然，在添加类时，您也可以选取多个元素：
// 实例
$("button").click(function () {
    $("h1,h2,p").addClass("blue");
    $("div").addClass("important");
});
// 您也可以在 addClass() 方法中规定多个类：
// 实例
$("button").click(function () {
    $("body div:first").addClass("important blue");
});
// jQuery removeClass() 方法
// 下面的例子演示如何在不同的元素中删除指定的 class 属性：
// 实例
$("button").click(function () {
    $("h1,h2,p").removeClass("blue");
});
// jQuery toggleClass() 方法
// 下面的例子将展示如何使用 jQuery toggleClass() 方法。该方法对被选元素进行添加/删除类的切换操作： 类似 hide show
// 实例
$("button").click(function () {
    $("h1,h2,p").toggleClass("blue");
});

// -----------------------------------------jQuery css() 方法-------------------------------
// jQuery css() 方法
// css() 方法设置或返回被选元素的一个或多个样式属性。
// 返回 CSS 属性
// 如需返回指定的 CSS 属性的值，请使用如下语法：
css("propertyname");
// 下面的例子将返回首个匹配元素的 background-color 值：
// 实例
$("p").css("background-color");
// 设置 CSS 属性
// 如需设置指定的 CSS 属性，请使用如下语法：
// css("propertyname","value");
// 下面的例子将为所有匹配元素设置 background-color 值：
// 实例
$("p").css("background-color", "yellow");
// 设置多个 CSS 属性
// 如需设置多个 CSS 属性，请使用如下语法：
// css({"propertyname":"value","propertyname":"value",...});
// 下面的例子将为所有匹配元素设置 background-color 和 font-size：
// 实例
$("p").css({ "background-color": "yellow", "font-size": "200%" });

// -----------------------------------------jQuery 尺寸-------------------------------
// jQuery 尺寸方法
// jQuery 提供多个处理尺寸的重要方法：
// width()
// height()
// innerWidth()
// innerHeight()
// outerWidth()
// outerHeight()
// jQuery width() 和 height() 方法
// width() 方法设置或返回元素的宽度（不包括内边距、边框或外边距）。
// height() 方法设置或返回元素的高度（不包括内边距、边框或外边距）。
// 下面的例子返回指定的 <div> 元素的宽度和高度：
// 实例
$("button").click(function () {
    var txt = "";
    txt += "div 的宽度是: " + $("#div1").width() + "</br>";
    txt += "div 的高度是: " + $("#div1").height();
    $("#div1").html(txt);
});
// jQuery innerWidth() 和 innerHeight() 方法
// innerWidth() 方法返回元素的宽度（包括内边距）。
// innerHeight() 方法返回元素的高度（包括内边距）。
// 下面的例子返回指定的 <div> 元素的 inner-width/height：
// 实例
$("button").click(function () {
    var txt = "";
    txt += "div 宽度，包含内边距: " + $("#div1").innerWidth() + "</br>";
    txt += "div 高度，包含内边距: " + $("#div1").innerHeight();
    $("#div1").html(txt);
});
// jQuery outerWidth() 和 outerHeight() 方法
// outerWidth() 方法返回元素的宽度（包括内边距和边框）。
// outerHeight() 方法返回元素的高度（包括内边距和边框）。
// 下面的例子返回指定的 <div> 元素的 outer-width/height：
// 实例
$("button").click(function () {
    var txt = "";
    txt += "div 宽度，包含内边距和边框: " + $("#div1").outerWidth() + "</br>";
    txt += "div 高度，包含内边距和边框: " + $("#div1").outerHeight();
    $("#div1").html(txt);
});

// ----------------------------------jQuery 遍历 - 祖先-----------------------------------
// 向上遍历 DOM 树
// 这些 jQuery 方法很有用，它们用于向上遍历 DOM 树：
// parent()
// parents()
// parentsUntil()
// jQuery parent() 方法
// parent() 方法返回被选元素的直接父元素。
// 该方法只会向上一级对 DOM 树进行遍历。
// 下面的例子返回每个 <span> 元素的直接父元素：
// 实例
$(document).ready(function () {
    $("span").parent();
});
// jQuery parents() 方法
// parents() 方法返回被选元素的所有祖先元素，它一路向上直到文档的根元素 (<html>)。
// 下面的例子返回所有 <span> 元素的所有祖先：
// 实例
$(document).ready(function () {
    $("span").parents();
});
{/* 您也可以使用可选参数来过滤对祖先元素的搜索。
下面的例子返回所有 <span> 元素的所有祖先，并且它是 <ul> 元素：
实例 */}
$(document).ready(function () {
    $("span").parents("ul");
});
{/* jQuery parentsUntil() 方法
parentsUntil() 方法返回介于两个给定元素之间的所有祖先元素。
下面的例子返回介于 <span> 与 <div> 元素之间的所有祖先元素：
实例 */}
$(document).ready(function () {
    $("span").parentsUntil("div");
});

// --------------------------------jQuery 遍历 - 后代-----------------------------
// 向下遍历 DOM 树
// 下面是两个用于向下遍历 DOM 树的 jQuery 方法：
// children()
// find()
// jQuery children() 方法
// children() 方法返回被选元素的所有直接子元素。
// 该方法只会向下一级对 DOM 树进行遍历。
// 下面的例子返回每个 <div> 元素的所有直接子元素：
// 实例
$(document).ready(function () {
    $("div").children();
});
// 您也可以使用可选参数来过滤对子元素的搜索。
// 下面的例子返回类名为 "1" 的所有 <p> 元素，并且它们是 <div> 的直接子元素：
// 实例
$(document).ready(function () {
    $("div").children("p.1");
});
// jQuery find() 方法
// find() 方法返回被选元素的后代元素，一路向下直到最后一个后代。
// 下面的例子返回属于 <div> 后代的所有 <span> 元素：
// 实例
$(document).ready(function () {
    $("div").find("span");
});
// 下面的例子返回 <div> 的所有后代：
// 实例
$(document).ready(function () {
    $("div").find("*");
});
// -------------------------------------jQuery 遍历- 过滤---------------------------------
// 缩小搜索元素的范围
// 三个最基本的过滤方法是：first(), last() 和 eq()，它们允许您基于其在一组元素中的位置来选择一个特定的元素。
// 其他过滤方法，比如 filter() 和 not() 允许您选取匹配或不匹配某项指定标准的元素。
// jQuery first() 方法
// first() 方法返回被选元素的首个元素。
// 下面的例子选取首个 <div> 元素内部的第一个 <p> 元素：
// 实例
$(document).ready(function () {
    $("div p").first();
});
// jQuery last() 方法
// last() 方法返回被选元素的最后一个元素。
// 下面的例子选择最后一个 <div> 元素中的最后一个 <p> 元素：
// 实例
$(document).ready(function () {
    $("div p").last();
});
// jQuery eq() 方法
// eq() 方法返回被选元素中带有指定索引号的元素。
// 索引号从 0 开始，因此首个元素的索引号是 0 而不是 1。下面的例子选取第二个 <p> 元素（索引号 1）：
// 实例
$(document).ready(function () {
    $("p").eq(1);
});
// jQuery filter() 方法
// filter() 方法允许您规定一个标准。不匹配这个标准的元素会被从集合中删除，匹配的元素会被返回。
// 下面的例子返回带有类名 "url" 的所有 <p> 元素：
// 实例
$(document).ready(function () {
    $("p").filter(".url");
});
// jQuery not() 方法
// not() 方法返回不匹配标准的所有元素。
// 提示：not() 方法与 filter() 相反。
// 下面的例子返回不带有类名 "url" 的所有 <p> 元素：
// 实例
$(document).ready(function () {
    $("p").not(".url");
});

// ---------------------------------jQuery - AJAX ------------------------------
// 什么是 AJAX？
// AJAX = 异步 JavaScript 和 XML（Asynchronous JavaScript and XML）。
// 简短地说，在不重载整个网页的情况下，AJAX 通过后台加载数据，并在网页上进行显示。
// jQuery - AJAX load() 方法
// jQuery load() 方法
// jQuery load() 方法是简单但强大的 AJAX 方法。
// load() 方法从服务器加载数据，并把返回的数据放入被选元素中。
// 语法:
// $(selector).load(URL,data,callback);
// 必需的 URL 参数规定您希望加载的 URL。
// 可选的 data 参数规定与请求一同发送的查询字符串键/值对集合。
// 可选的 callback 参数是 load() 方法完成后所执行的函数名称。
// 这是示例文件（"demo_test.txt"）的内容：
// <h2>jQuery AJAX 是个非常棒的功能！</h2>
// <p id="p1">这是段落的一些文本。</p>
// 下面的例子会把文件 "demo_test.txt" 的内容加载到指定的 <div> 元素中：
// 实例
$("#div1").load("demo_test.txt");
// 也可以把 jQuery 选择器添加到 URL 参数。
// 下面的例子把 "demo_test.txt" 文件中 id="p1" 的元素的内容，加载到指定的 <div> 元素中：
// 实例
$("#div1").load("demo_test.txt #p1");
// 可选的 callback 参数规定当 load() 方法完成后所要允许的回调函数。回调函数可以设置不同的参数：
// responseTxt - 包含调用成功时的结果内容
// statusTXT - 包含调用的状态
// xhr - 包含 XMLHttpRequest 对象
// 下面的例子会在 load() 方法完成后显示一个提示框。如果 load() 方法已成功，则显示"外部内容加载成功！"，而如果失败，则显示错误消息：
// 实例
$("button").click(function () {
    $("#div1").load("demo_test.txt", function (responseTxt, statusTxt, xhr) {
        if (statusTxt == "success")
            alert("外部内容加载成功!");
        if (statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
});
// jQuery - AJAX get() 和 post() 方法
// jQuery $.get() 方法
// $.get() 方法通过 HTTP GET 请求从服务器上请求数据。
// 语法：
// $.get(URL,callback);
// 必需的 URL 参数规定您希望请求的 URL。
// 可选的 callback 参数是请求成功后所执行的函数名。
// 下面的例子使用 $.get() 方法从服务器上的一个文件中取回数据：
// 实例
$("button").click(function () {
    $.get("demo_test.php", function (data, status) {
        alert("数据: " + data + "\n状态: " + status);
    });
});
// jQuery $.post() 方法
// $.post() 方法通过 HTTP POST 请求向服务器提交数据。
// 语法:
// $.post(URL,data,callback);
// 必需的 URL 参数规定您希望请求的 URL。
// 可选的 data 参数规定连同请求发送的数据。
// 可选的 callback 参数是请求成功后所执行的函数名。
// 下面的例子使用 $.post() 连同请求一起发送数据：
// 实例
$("button").click(function () {
    $.post("/try/ajax/demo_test_post.php",
        {
            name: "菜鸟教程",
            url: "http://www.runoob.com"
        },
        function (data, status) {
            alert("数据: \n" + data + "\n状态: " + status);
        });
});






























