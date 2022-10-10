# 生成数据库迁移（当模型里数据表发生变化时）
python manage.py makemigrations
python manage.py migrate
# 创建app（cd到项目文件夹下）
1、python manage.py startapp appname
2、接下来在项目的settings.py中添加appname
INSTALLED_APPS = [
......
'appname',
]

