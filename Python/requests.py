链接：https://blog.csdn.net/bbwangj/article/details/86531142

一、requests模块介绍
Requests 是使用 Apache2 Licensed 许可证的 基于Python开发的HTTP 库，其在Python内置模块的基础上进行了高度的封装，从而使得Pythoner进行网络请求时，变得美好了许多，使用Requests可以轻而易举的完成浏览器可有的任何操作。requests可以模拟浏览器的请求，比起之前用到的urllib，requests模块的api更加便捷（其本质就是封装了urllib3），

特点：requests库发送请求将网页内容下载下来以后，并不会执行js代码，这需要我们自己分析目标站点然后发起新的request请求

1、安装requests模块

pip3 install requests
2、requests模块支持的请求方式

常用的就是requests.get()和requests.post()，建议在正式学习requests前，先熟悉下HTTP协议；http://www.cnblogs.com/linhaifeng/p/6266327.html

>>> import requests
>>> r = requests.get('https://api.github.com/events')   
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')
二、requests发送GET请求
 1、基本get请求

1 import requests
2 response=requests.get('http://dig.chouti.com/')
3 print(response.text)
response查看response编码

respose.encoding：查看返回网页数据默认编码

import requests
 
url='https://www.baidu.com/'
respose=requests.get(
             url=url,
             headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
             })
 
print(respose.encoding)#查看网页编码
respose.encoding='utf-8' #设置网页编码
print(respose.status_code)
with open('a.html','w',encoding='utf-8') as f:
    f.write(respose.text)
2、带参数的GET请求

 url编码

#带参数的url,+url编码
from urllib.parse import urlencode
import requests
k=input('输入关键字：  ').strip()
res=urlencode({'wd':k},encoding='utf-8')  #url编码
respose=requests.get('https://www.baidu.com/s?%s'% res,
                     headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
                     },
                     # params={'wd':k}
 
 
                     )
with open('a.html','w',encoding='utf-8') as f:
    f.write(respose.text)
headers设置请求头

respose=requests.get('https://www.baidu.com/s?%s'% res,
                     headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
                     },
params 请求参数设置（自动处理URL后参数编码）

k=input('输入关键字：  ').strip()
# res=urlencode({'wd':k},encoding='utf-8')  #url编码
respose=requests.get('https://www.baidu.com/s?',
                     headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
                     },
                     params={'wd':k}
 
 
                     )
with open('a.html','w',encoding='utf-8') as f:
    f.write(respose.text)
Cookies 请求携带cookie信息

respose=requests.get('https://www.baidu.com/s?',
                     headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
                     },
                     params={'wd':k},
                     Cookies={'user_session':'wGMHFJKgDcmRIVvcA14_Wrt_3xaUyJNsBnPbYzEL6L0bHcfc'},
 
                     )
allow_redirects=False   禁止根据resposes的响应头的location做页面跳转，默认是true跳转；

设置为flase可以停留在本次请求（request），获取本次响应（responses）响应头，让跳转的loction地址；否则跳转了获取得就是跳转之后页面的响应内容了！

r3=session.get('https://passport.lagou.com/grantServiceTicket/grant.html',
               headers={
                   'Referer':'//passport.lagou.com/login/login.html',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                   'Host':'passport.lagou.com',
                    },
               allow_redirects = False  # 禁止授权完成之后，禁止做页面跳转
               ,
 
               )
小结：



三、requests发送POST请求
1、get请求和post请求的区别

GET请求：HTPP默认的请求方式是GET；

GETt请求的特点：

  *没有请求体，携带数据保存在URL后面

  *GET请求携带的参数必须在1k之内

  *GET请求的携带的数据由于封装在URL后面，所以会暴露在浏览器地址栏中

POST请求：用户先server端提交上传数据一般会使用POST请求

POST请求的特点：

 *有请求体，数据保存在请求体中

 *上传提交的数据无上限

 *请求体中如果存在中文，会使用URL编码！

小结：

requests.post()用法与requests.get()完全一致，特殊的是requests.post()有一个data参数，用来存放请求体数据，也就是POST请求的请求体；

 2、发送post请求，模拟浏览器的登录github

import requests
import re
 
#访问登录页面
r1=requests.get('https://github.com/login/',
                     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
 
                     )
 
authenticity_token=re.findall(r'name="authenticity_token".*?value="(.*?)"',r1.text,re.S)[0]
# print(r1.cookies.items()) #获取元祖类型的cookies信息
# print(r1.cookies.get_dict())#获取字典类型的cokies信息
cookies=r1.cookies.get_dict()
 
 
#访问登录页面
r2=requests.post('https://github.com/session',
    data={
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':authenticity_token,
    'login':'13220198866@163.com',
    'password':'123.com'},
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
    cookies=cookies)
 
 
#访问设置个人主页
cookies2=r2.cookies.get_dict() #获取登录页面返回的cokies信息
r3=requests.get('https://github.com/settings/emails',cookies=cookies2)
 
print('13220198866@163.com' in r3.text  )
3、使用request.post() 之 content-type

requests.post(url='xxxxxxxx',
              data={'xxx':'yyy'}) #没有指定请求头,#默认的请求头:application/x-www-form-urlencoed
 
#如果需要向server端传说json数据，必须设置 content-ype:application/json,并且用data传值, 否则服务端取不到值
requests.post(url='',
              data={'':1,},
              headers={
                  'content-type':'application/json'
              })
四 、requests模块的响应Response
当我们使用requets模块，发送了正确GET/POST请求之后，服务端势必会给我们一个response（响应内容）

1、response属性

respose=requests.get('http://www.cnblogs.com/sss4/')
print(respose.text)  #显示文本内容
print(respose.content) #显示二进制内容（比如爬 图片 或视频需要）
print(respose.status_code) #返回的状态码
print(respose.headers) #获取响应头
print(respose.cookies) #获取服务端响应的cokies信息
print(respose.cookies.get_dict()) #获取字典形式的cokies信息
print(respose.cookies.items()) #获取列表类型的cookis信息
print(respose.url) #获取请求的URLhttp://www.cnblogs.com/sss4/
print(respose.history)#获取跳转前的url
print(respose.json()) #获取json数据
respose.encoding='gbk'#设置 requests模块的编码
五、requests模块的高级用法
1、SSL Cert Verification（验证证书）

大家平时访问某网站的时候，URL是以https开头的，这是为什么呢？
https是http+ssl协议：基于证书校验的http协议

世界上有一个专门负责为浏览器颁发证书的CA机构

某些网站会去CA中心买1个数字证书，这样浏览器每次去访问该网站都会去访问权威CA机构，获取该证书携带该证书过去访问该网站；

还有一类网站不愿去花钱去CA购买权威的证书，自己搭建了一个颁发证书的CA，这些CA中心是不被浏览器认可的，所以每次访问这些网站的时候，浏览器会去私有证书颁发机构获取证书，浏览器会提示用户这是一个不安全的链接，让用户选择处理；
我们在做爬虫的时候如何绕过证书验证环节呢？

情况1：不再证书验证

不做证书验证的情况，在某些情况下是行不通的的；

除非某些网站购买的是权威的CA证书，已经和浏览器和操作系统做了合作下载浏览器时把证书自带下载好了；（提升了用户体验，也提升了安全性。）

另外一种情况是 虽然该网站做了证书验证，但是不使用https协议也能正常登录；（用户体验为上）
verify=False 代表不做证书验证

#证书验证(大部分网站都是https)
import requests
respone=requests.get('https://www.12306.cn') #如果是ssl请求,首先检查证书是否合法,不合法则报错,程序终端
去掉报错,并且去掉警报信息

import requests
from requests.packages import urllib3
urllib3.disable_warnings() #关闭警告
respone=requests.get('https://www.12306.cn',verify=False)
print(respone.status_code)
情况2：必须做用户证书验证的网站

但是一些网站必须硬性要求浏览器携带证书，比如12306这种刚需网站，如何破？（安全至上）

import requests
respone=requests.get('https://www.12306.cn',
                     cert=('/path/server.crt',
                           '/path/key'))
print(respone.status_code)
 2、使用爬虫代理

如果你使用爬某网站的频率过高，IP会被该网站封掉，如何破？找一个代理使用别人的IP地址去访问

#官网链接: http://docs.python-requests.org/en/master/user/advanced/#proxies
 
#代理设置:先发送请求给代理,然后由代理帮忙发送(封ip是常见的事情)
import requests
proxies={
    'http':'http://egon:123@localhost:9743',#带用户名密码的代理,@符号前是用户名与密码
    'http':'http://localhost:9743',
    'https':'https://localhost:9743',
}
respone=requests.get('https://www.12306.cn',
                     proxies=proxies)
 
print(respone.status_code)
 
 
 
#支持socks代理,安装:pip install requests[socks]
import requests
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
respone=requests.get('https://www.12306.cn',
                     proxies=proxies)
 
print(respone.status_code)
3、超时设置

import requests
 
 
result=requests.get('https://www.baidu.com/',timeout=0.0001 )  #timeout=0.0001 代表 请求+接收服务端数据的总时间；
 
#如果想明确控制  连接 和 等待接收服务端数据的时间timeout=(1,2))
result2=requests.get('https://www.baidu.com/',timeout=(1,2)) #timeout=(0.1,0.2)#0.1代表链接超时时间  0.2代表接收数据的超时时间
4、 认证设置

爬取公司内网需要输入用户名和密码的 内网 例如：监控系统、乐视人（线上报销）

#官网链接：http://docs.python-requests.org/en/master/user/authentication/
 
#认证设置:登陆网站是,弹出一个框,要求你输入用户名密码（与alter很类似），此时是无法获取html的
# 但本质原理是拼接成请求头发送
#         r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
# 一般的网站都不用默认的加密方式，都是自己写
# 那么我们就需要按照网站的加密方式，自己写一个类似于_basic_auth_str的方法
# 得到加密字符串后添加到请求头
#         r.headers['Authorization'] =func('.....')
 
#看一看默认的加密方式吧，通常网站都不会用默认的加密设置
import requests
from requests.auth import HTTPBasicAuth
r=requests.get('xxx',auth=HTTPBasicAuth('user','password'))
print(r.status_code)
 
#HTTPBasicAuth可以简写为如下格式
import requests
r=requests.get('xxx',auth=('user','password'))
print(r.status_code)
5、requests模块自带异常处理

#异常处理
import requests
from requests.exceptions import * #可以查看requests.exceptions获取异常类型
 
try:
    r=requests.get('http://www.baidu.com',timeout=0.00001)
except ReadTimeout:
    print('===:')
# except ConnectionError: #网络不通
#     print('-----')
# except Timeout:
#     print('aaaaa')
 
except RequestException:
    print('Error')
6、使用requests模块上传文件

import requests
files={'file':open('a.jpg','rb')}
respone=requests.post('http://httpbin.org/post',files=files)
print(respone.status_code)
 

六、requests.session()方法
每次写爬虫都要在响应头中获取cokies信息，然后在把获取的cokies信息加在请求头，太繁琐了；

如果有了 requests.session()对象，就可以自动处理cokies问题了；

session= requests.session()  #相当于设置了 一个会话相关的容器，把所有会话相关的cookie都存放起来（自动保存cookie问题）
r1=session.get('https://github.com/login/',
                     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'},
 
                     )
 
authenticity_token=re.findall(r'name="authenticity_token".*?value="(.*?)"',r1.text,re.S)[0]
 

其他请求

requests.get(url, params=None, **kwargs)

requests.post(url, data=None, json=None, **kwargs)

requests.put(url, data=None, **kwargs)

requests.head(url, **kwargs)

requests.delete(url, **kwargs)

requests.patch(url, data=None, **kwargs)

requests.options(url, **kwargs)

 

# 以上方法均是在此方法的基础上构建

requests.request(method, url, **kwargs)

requests模块已经将常用的Http请求方法为用户封装完成，用户直接调用其提供的相应方法即可，其中方法的所有参数有：

def request(method, url, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.
 
    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': ('filename', fileobj)}``) for multipart encoding upload.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How long to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) whether the SSL cert will be verified. A CA_BUNDLE path can also be provided. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
 
    Usage::
 
      >>> import requests
      >>> req = requests.request('GET', 'http://httpbin.org/get')
      <Response [200]>
    """
 
    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)
更多requests模块相关的文档见：http://cn.python-requests.org/zh_CN/latest/

案例：自动登陆抽屉并点赞

### 1、首先登陆任何页面，获取cookie

 

i1 = requests.get(url= "http://dig.chouti.com/help/service")

 

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权

i2 = requests.post(

    url= "http://dig.chouti.com/login",

    data= {

        'phone': "86手机号",

        'password': "密码",

        'oneMonth': ""

    },

    cookies = i1.cookies.get_dict()

)

 

### 3、点赞（只需要携带已经被授权的gpsd即可）

gpsd = i1.cookies.get_dict()['gpsd']

i3 = requests.post(

    url="http://dig.chouti.com/link/vote?linksId=8589523",

    cookies={'gpsd': gpsd}

)

print(i3.text)

案例：“破解”微信公众号
“破解”微信公众号其实就是使用Python代码自动实现【登陆公众号】->【获取观众用户】-> 【向关注用户发送消息】。

注：只能向48小时内有互动的粉丝主动推送消息

1、自动登陆



分析对于Web登陆页面，用户登陆验证时仅做了如下操作：

登陆的URL：https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN
POST的数据为：
    {
         'username': 用户名,
         'pwd': 密码的MD5值,
         'imgcode': "", 
         'f': 'json'
    }
注：imgcode是需要提供的验证码，默认无需验证码，只有在多次登陆未成功时，才需要用户提供验证码才能登陆

POST的请求头的Referer值，微信后台用次来检查是谁发送来的请求
请求发送并登陆成功后，获取用户响应的cookie，以后操作其他页面时需要携带此cookie 
请求发送并登陆成功后，获取用户相应的内容中的token
# -*- coding:utf-8 -*- 
import requests
import time
import hashlib
 
 
def _password(pwd):
    ha = hashlib.md5()
    ha.update(pwd)
    return ha.hexdigest()
 
def login():
    
    login_dict = {
        'username': "用户名",
        'pwd': _password("密码"),
        'imgcode': "",
        'f': 'json'
    }
 
    login_res = requests.post(
        url= "https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN",
        data=login_dict,
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'})
 
    # 登陆成功之后获取服务器响应的cookie
    resp_cookies_dict = login_res.cookies.get_dict()
    # 登陆成功后，获取服务器响应的内容
    resp_text = login_res.text
    # 登陆成功后，获取token
    token = re.findall(".*token=(\d+)", resp_text)[0]
 
    print resp_text
    print token
    print resp_cookies_dict
 
login()
登陆成功获取的相应内容如下：

响应内容：

{"base_resp":{"ret":0,"err_msg":"ok"},"redirect_url":"\/cgi-bin\/home?t=home\/index&lang=zh_CN&token=537908795"}

 

响应cookie：

{'data_bizuin': '3016804678', 'bizuin': '3016804678', 'data_ticket': 'CaoX+QA0ZA9LRZ4YM3zZkvedyCY8mZi0XlLonPwvBGkX0/jY/FZgmGTq6xGuQk4H', 'slave_user': 'gh_5abeaed48d10', 'slave_sid': 'elNLbU1TZHRPWDNXSWdNc2FjckUxalM0Y000amtTamlJOUliSnRnWGRCdjFseV9uQkl5cUpHYkxqaGJNcERtYnM2WjdFT1pQckNwMFNfUW5fUzVZZnFlWGpSRFlVRF9obThtZlBwYnRIVGt6cnNGbUJsNTNIdTlIc2JJU29QM2FPaHZjcTcya0F6UWRhQkhO'}

2、访问其他页面获取用户信息



分析用户管理页面，通过Pyhton代码以Get方式访问此页面，分析响应到的 HTML 代码，从中获取用户信息：

获取用户的URL：https://mp.weixin.qq.com/cgi-bin/user_tag?action=get_all_data&lang=zh_CN&token=登陆时获取的token
发送GET请求时，需要携带登陆成功后获取的cookie
1

{'data_bizuin': '3016804678', 'bizuin': '3016804678', 'data_ticket': 'C4YM3zZ...

获取当前请求的响应的html代码
通过正则表达式获取html中的指定内容（Python的模块Beautiful Soup）
获取html中每个用户的 data-fakeid属性，该值是用户的唯一标识，通过它可向用户推送消息
# -*- coding:utf-8 -*- 
import requests
import time
import hashlib
import json
import re
 
LOGIN_COOKIES_DICT = {}
 
def _password(pwd):
    ha = hashlib.md5()
    ha.update(pwd)
    return ha.hexdigest()
 
def login():
    
    login_dict = {
        'username': "用户名",
        'pwd': _password("密码"),
        'imgcode': "",
        'f': 'json'
    }
 
    login_res = requests.post(
        url= "https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN",
        data=login_dict,
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'})
 
    # 登陆成功之后获取服务器响应的cookie
    resp_cookies_dict = login_res.cookies.get_dict()
    # 登陆成功后，获取服务器响应的内容
    resp_text = login_res.text
    # 登陆成功后，获取token
    token = re.findall(".*token=(\d+)", resp_text)[0]
 
    return {'token': token, 'cookies': resp_cookies_dict}
 
 
def standard_user_list(content):
    content = re.sub('\s*', '', content)
    content = re.sub('\n*', '', content)
    data = re.findall("""cgiData=(.*);seajs""", content)[0]
    data = data.strip()
    while True:
        temp = re.split('({)(\w+)(:)', data, 1)
        if len(temp) == 5:
            temp[2] = '"' + temp[2] + '"'
            data = ''.join(temp)
        else:
            break
 
    while True:
        temp = re.split('(,)(\w+)(:)', data, 1)
        if len(temp) == 5:
            temp[2] = '"' + temp[2] + '"'
            data = ''.join(temp)
        else:
            break
 
    data = re.sub('\*\d+', "", data)
    ret = json.loads(data)
    return ret
 
 
def get_user_list():
 
    login_dict = login()
    LOGIN_COOKIES_DICT.update(login_dict)
 
    login_cookie_dict = login_dict['cookies']
    res_user_list = requests.get(
        url= "https://mp.weixin.qq.com/cgi-bin/user_tag",
        params = {"action": "get_all_data", "lang": "zh_CN", "token": login_dict['token']},
        cookies = login_cookie_dict,
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'}
    )
    user_info = standard_user_list(res_user_list.text)
    for item in user_info['user_list']:
        print "%s %s " % (item['nick_name'],item['id'],)
    
get_user_list()
3、发送消息



分析给用户发送消息的页面，从网络请求中剖析得到发送消息的URL，从而使用Python代码发送消息：

发送消息的URL：https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&f=json&token=登陆时获取的token放在此处&lang=zh_CN
从登陆时相应的内容中获取：token和cookie
从用户列表中获取某个用户唯一标识： fake_id
封装消息，并发送POST请求

send_dict = {

    'token': 登陆时获取的token,

    'lang': "zh_CN",

    'f': 'json',

    'ajax': 1,

    'random': "0.5322618900912392",

    'type': 1,

    'content': 要发送的内容,

    'tofakeid': 用户列表中获取的用户的ID,

    'imgcode': ''

}

# -*- coding:utf-8 -*-
import requests
import time
import hashlib
import json
import re
 
LOGIN_COOKIES_DICT = {}
 
def _password(pwd):
    ha = hashlib.md5()
    ha.update(pwd)
    return ha.hexdigest()
 
def login():
    
    login_dict = {
        'username': "用户名",
        'pwd': _password("密码"),
        'imgcode': "",
        'f': 'json'
    }
 
    login_res = requests.post(
        url= "https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN",
        data=login_dict,
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'})
 
    # 登陆成功之后获取服务器响应的cookie
    resp_cookies_dict = login_res.cookies.get_dict()
    # 登陆成功后，获取服务器响应的内容
    resp_text = login_res.text
    # 登陆成功后，获取token
    token = re.findall(".*token=(\d+)", resp_text)[0]
 
    return {'token': token, 'cookies': resp_cookies_dict}
 
 
def standard_user_list(content):
    content = re.sub('\s*', '', content)
    content = re.sub('\n*', '', content)
    data = re.findall("""cgiData=(.*);seajs""", content)[0]
    data = data.strip()
    while True:
        temp = re.split('({)(\w+)(:)', data, 1)
        if len(temp) == 5:
            temp[2] = '"' + temp[2] + '"'
            data = ''.join(temp)
        else:
            break
 
    while True:
        temp = re.split('(,)(\w+)(:)', data, 1)
        if len(temp) == 5:
            temp[2] = '"' + temp[2] + '"'
            data = ''.join(temp)
        else:
            break
 
    data = re.sub('\*\d+', "", data)
    ret = json.loads(data)
    return ret
 
 
def get_user_list():
 
    login_dict = login()
    LOGIN_COOKIES_DICT.update(login_dict)
 
    login_cookie_dict = login_dict['cookies']
    res_user_list = requests.get(
        url= "https://mp.weixin.qq.com/cgi-bin/user_tag",
        params = {"action": "get_all_data", "lang": "zh_CN", "token": login_dict['token']},
        cookies = login_cookie_dict,
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'}
    )
    user_info = standard_user_list(res_user_list.text)
    for item in user_info['user_list']:
        print "%s %s " % (item['nick_name'],item['id'],)
    
 
def send_msg(user_fake_id, content='啥也没发'):
 
    login_dict = LOGIN_COOKIES_DICT
    
    token = login_dict['token']
    login_cookie_dict = login_dict['cookies']
 
    send_dict = {
        'token': token,
        'lang': "zh_CN",
        'f': 'json',
        'ajax': 1,
        'random': "0.5322618900912392",
        'type': 1,
        'content': content,
        'tofakeid': user_fake_id,
        'imgcode': ''
    }
   
    send_url = "https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&f=json&token=%s&lang=zh_CN" % (token,)
    message_list = requests.post(
        url=send_url, 
        data=send_dict, 
        cookies=login_cookie_dict, 
        headers={'Referer': 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'}
    )
 
 
get_user_list()
fake_id = raw_input('请输入用户ID:')
content = raw_input('请输入消息内容:')
send_msg(fake_id, content)
以上就是“破解”微信公众号的整个过程，通过Python代码实现了自动【登陆微信公众号平台】【获取用户列表】【指定用户发送消息】。

 

Http请求和XML实例，检测QQ账号是否在线
import urllib
import requests
from xml.etree import ElementTree as ET
 
# 使用内置模块urllib发送HTTP请求，或者XML格式内容
"""
f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
result = f.read().decode('utf-8')
"""
 
 
# 使用第三方模块requests发送HTTP请求，或者XML格式内容
r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
result = r.text
 
# 解析XML格式内容
node = ET.XML(result)
 
# 获取内容
if node.text == "Y":
    print("在线")
else:
    print("离线")
案例：查看火车停靠信息
import urllib
import requests
from xml.etree import ElementTree as ET
 
# 使用内置模块urllib发送HTTP请求，或者XML格式内容
"""
f = urllib.request.urlopen('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
result = f.read().decode('utf-8')
"""
 
# 使用第三方模块requests发送HTTP请求，或者XML格式内容
r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
result = r.text
 
# 解析XML格式内容
root = ET.XML(result)
for node in root.iter('TrainDetailInfo'):
    print(node.find('TrainStation').text,node.find('StartTime').text,node.tag,node.attrib)
