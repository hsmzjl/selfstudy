import pymysql


# 创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='lytest',charset='utf8')
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("update students set name = 'ly' where id = 1;")
# 执行SQL，并返回受影响行数
#effect_row = cursor.execute("update students set name = 'niuhy' where id = %s;", (1,))
# 执行SQL，并返回受影响行数
effect_row = cursor.executemany("insert into students (name,age) values (%s,%s); ", [("wangzhj",18),("12345",20)])
#执行select语句
cursor.execute("select * from students;")
#获取查询结果的第一条数据，返回的是一个元组
row_1 = cursor.fetchone()
# 获取前n行数据
row_2 = cursor.fetchmany(3)
# 获取所有数据
row_3 = cursor.fetchall()
# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 获取最新自增ID
new_id = cursor.lastrowid
print(new_id)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
# =====================================================================================================

# 上面的操作，获取到的返回结果都是元组，如果想获取到的结果是一个字典类型的话，可以使用下面这样的操作

# =====================================================================================================

import pymysql
# 创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='lytest',charset='utf8')
# 创建游标
cursor = conn.cursor()

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)#需要指定游标的类型，字典类型
# 执行SQL
cursor.execute("select * from user;")
#获取返回结果，这个时候返回结果是一个字典
res = cursor.fetchone()#返回一条数据，如果结果是多条的话
print(res)
res2 = cursor.fetchall()#所有的数据一起返回

# =====================================================================================================

# 批量插入数据

# =====================================================================================================
import pymysql

mydb = pymysql.connect(
    host="192.168.1.115",
    user="root",
    passwd="123456",
    database="lytest"
)
cursor = mydb.cursor()

sql = "INSERT INTO author (name, sex,age) VALUES (%s, %s, %s)"
val = [
        ('射手1', '女','20'),
        ('射手2', '女', '20'),
        ('射手3', '女', '20'),
        ('射手4', '女', '20'),
    ]
cursor.executemany(sql, val)
mydb.commit()    # 数据表内容有更新，必须使用到该语句
print(cursor.rowcount, "记录插入成功。")
