# 如果一台电脑上安装过python及一些依赖包，另一台电脑也想安装同样的包，如何操作。

   a.  pip freeze >PackagesInfo.txt”

        此时会生成一个PackagesInfo.txt文件，里面有目前python的pip下已安装所有package的信息。

   b. 这个文件 拷贝到另一台电脑 执行 pip install -r PackagesInfo.txt，即可批量安装python包。

       python3 -m pip install -r PackagesInfo.txt 多版本python使用pip方法

       pip install -r PackagesInfo.txt -i https://pypi.tuna.tsinghua.edu.cn/simple



Python windows运行环境的迁移与离线安装
依赖包(全环境)和版本号
自动生成当前Python环境的所有依赖包及其精确版本号： pip freeze > requirements.txt

离线下载安装包
下载单个离线包 - pip download -d your_offline_packages <package_name>

批量下载离线包 - pip download -d your_offline_packages -r requirements.txt

离线安装

安装单个离线包 - pip install --no-index --find-links=/your_offline_packages/ package_name

批量安装离线包 - pip install --no-index --find-links=/your_offline_packages/ -r requirements.txt



国内pip镜像
让python pip使用国内镜像
国内源：
清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/ 

note：新版ubuntu要求使用https源，要注意。

临时使用：
可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple
例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider，这样就会从清华这边的镜像去安装pyspider库。

永久修改，一劳永逸：
Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)

内容如下：

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com


