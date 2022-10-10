import pymssql


# sql语句
# 查询
"SELECT djid,djlx,dxid,ywyid,beizhu,dxlx FROM yw WHERE beizhu like '%#%'"
# 查询对象要用 单引号 '' 包裹起来
# 更新


# 一个简单的mssql类
class MSSQL():
    def __init__(self, server='192.168.1.10', user='zd', password='011463'):
        # 类的构造函数，初始化DBC连接信息
        self.server = server
        self.user = user
        self.password = password

    def connect(self, database='yxtma'):
        self.database = database
        # autocommit = True 表示在更新，删除，增加的操作后，自动提交到数据库。如果不填写，则需要在更新，删除，增加的操作后调用self.conn.commit()函数来完成操作
        self.conn = pymssql.connect(self.server,
                                    self.user,
                                    self.password,
                                    self.database,
                                    autocommit=True)  # 服务器名,账户,密码,数据库名
        if self.conn:
            print("连接成功!")
        return self.conn

    # 查询数据，返回dict数组，查询失败和返回数组长度等于0时都返回False
    def select(self, sql):
        try:
            cursor = self.conn.cursor(as_dict=True)
            cursor.execute(sql)
            row = cursor.fetchall()
            if len(row) > 0:
                return row
            else:
                return False
        except:
            return False

    #关闭数据库连接
    def close(self):
        self.conn.close()



一、创建数据库Test、表tb、插入数据

特别需要注意的是：为了避免乱码问题，这里Name列是nvarchar类型的（适合中文），不会出现乱码现象，一开始用的varchar类型出现了乱码。
create database Test;
go
use test;
go
if object_id('tb') is not null
  drop table tb;
go
CREATE TABLE TB(ID INT,NAME NVARCHAR(20),SCORE NUMERIC(10,2));
INSERT INTO TB(ID,NAME,SCORE)
VALUES(1,'语文',100),
   (2,'数学',80),
   (3,'英语',900),
   (4,'政治',65),
   (5,'物理',65),
   (6,'化学',85),
   (7,'生物',55),
   (8,'地理',100)

二、连接数据库、查询、增加、更新数据

connect的参数：

user：用户名
password：密码
trusted：布尔值,指定是否使用windows身份认证登陆
host :主机名
database：数据库
timeout：查询超时
login_timeout：登陆超时
charset：数据库的字符集
as_dict：布尔值,指定返回值是字典还是元组
max_conn：最大连接数
autocommit:自动提交


# -*- coding:gbk -*-
import pymssql
#数据库连接
conn=pymssql.connect(host='wc-pc',user='sa',password='ggg',database='Test')
#打开游标
cur=conn.cursor();
if not cur:
  raise Exception('数据库连接失败！')
sSQL = 'SELECT * FROM TB'
#执行sql，获取所有数据
cur.execute(sSQL)
result=cur.fetchall()
#1.result是list，而其中的每个元素是 tuple
print(type(result),type(result[0]))
#2.
print('\n\n总行数：'+ str(cur.rowcount))
#3.通过enumerate返回行号
for i,(id,name,v) in enumerate(result):
  print('第 '+str(i+1)+' 行记录->>> '+ str(id) +':'+ name+ ':' + str(v) )
#4.修改数据
cur.execute("insert into tb(id,name,score) values(9,'历史',75)")
cur.execute("update tb set score=95 where id=7")
conn.commit() #修改数据后提交事务
#再查一次
cur.execute(sSQL)
#5.一次取一条数据,cur.rowcount为-1
r=cur.fetchone()
i=1
print('\n')
while r:
  id,name,v =r #r是一个元祖
  print('第 '+str(i)+' 行记录->>> '+ str(id) +':'+ name+ ':' + str(v) )
  r=cur.fetchone()
  i+= 1
conn.close()

基本的步骤就是：

（1）连接数据库，指定连接参数
（2）打开cursor，执行sql
（3）通过cursor获取数据，具体可以是一次获取所有数据，也可以是一次获取一行。
 整个结果集是元组列表，就是list类型的，而每一条记录是一个tuple，也就是元祖。
（4）如果是增、改数据，必须就要调用commit()函数来提交事务，否则程序已退出，数据库里的数据不会有变化。
（5）最后要用close关闭连接。






