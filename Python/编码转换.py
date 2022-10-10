from urllib import parse
import json

teststr = 'gffdsgfdzhong中文4545gfds'

#字符串转换成URL编码
testurl = parse.quote(teststr)
#url编码解码成字符串
teststr1 = parse.unquote(testurl)

# json是一种有固定格式的字符串，即json隶属于字符串
python_dict = {"code": 0, "msg": "服务器错误"}
#dict对象转换成json字符串
jsonData = json.dumps(python_dict)
#dict对象转换成json字符串,添加如下参数才能转换日期时间型
jsonData = json.dumps(python_dict, default=str, ensure_ascii=False)
#json字符串转换成json对象
python_dict = json.loads(jsonData)
