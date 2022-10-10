request.POST / request.body区别


# 有时候前端提交数据了，但是 request.POST 却取不到数据
# 这种情况下，可以从尝试 request.body 中读取数据
# json_result = json.loads(request.body)


当request.POST没有值 需要考虑下面两个要求
1.如果请求头中的: Content-Type: application/x-www-form-urlencoded request.POST中才会有值（才会去request.body中解析数据）
2.若1有，也不一定有值 必须有数据格式要求： name=alex&age=18&gender=男


如:
    a. form表单提交 默认就会满足上诉的1和2
        <form method...>
            input
        </form>
 
    b. ajax提交
        $.ajax({
            url:...
            type:POST,
            data:{
                name:alex,
                age=18,
            }     #默认也会满足上诉1和2  请求头默认为上述情况 内部数据格式会转为上述情况
        })
 
       自定义ajax 情况一
       $.ajax({
            url:...
            type:POST,
            headers:{'Content-Type':"application/json"}  #不同的请求头 导致request.POST获取不了数据 而request.body依旧存在数据
            data:{name:alex, age = 18}   #内部自动转换 name=alex&age=18
 
       }) #即body有值 POST无值
 
       自定义ajax 情况二
       $.ajax({
            url:...
            type:POST,
            headers:{'Content-Type':"application/json"}  #不同的请求头 导致request.POST获取不了数据 而request.body依旧存在数据
            data:JSON.stringfy{name:alex, age = 18} #{name:alex,age:18}
 
       })  #body有值 POST无值
       #从 request.body里获取数据 然后再通过json.loads(request.body)