import pymysql
import pymssql

# -----------------------------------------------------基本语句--------------------------------------------
(1) 数据记录筛选：
sql="select * from 数据表 where 字段名 = 字段值 order by 字段名[desc]"（按某个字段值降序排列，默认升序ASC）。
sql="select * from 数据表 where 字段名 like '%字段值%' order by 字段名 [desc]"
sql="select top 10 * from 数据表 where字段名=字段值 order by 字段名 [desc]"
sql="select * from 数据表 where字段名 in ('值1','值2','值3')"
sql="select * from 数据表 where 字段名 between 值1 and 值2"
sql="select 列名1，列名2 from 数据表 where 字段名=字段值 group by 列名1，列名2 " （group by 用来分组，并且只有出现自group by 中的列名，才允许出现在select 语句中）。
分类汇总，
示例：SELECT itemCode,SUM(requestQty) AS requestQty FROM shipment_detail WHERE shipmentCode = 'S2008100107' GROUP BY itemCode,requestQty
上面语句可以 去重itemCode 并按itemCode来统计数量SUM(requestQty)
(2) 更新数据记录：
sql="update 数据表 set 字段名=字段值 where 条件表达式"
sql="update 数据表 set 字段1=值1,字段2=值2 …… 字段n=值n where 条件表达式"
(3) 删除数据记录：
sql="delete from 数据表 where 条件表达式"
sql="delete from 数据表" (将数据表所有记录删除)
(4) 添加数据记录：
sql="insert into 数据表 (字段1,字段2,字段3 …) values (值1,值2,值3 …)"
sql="insert into 目标数据表 select * from 源数据表" (把源数据表的记录添加到目标数据表)
(6) 其它
SELECT DISTINCT Company FROM table_name  # 关键词 DISTINCT 用于返回唯一不同的值。
SELECT SUM(字段名) FROM 数据表    # 单列求和:




--------------------------------------------定义参数（默认值）---------------------------------
# DECLARE maxNo INT DEFAULT 0 ; -- 定义maxNo为离现在最近的满足条件的订单编号的流水号最后5位，如：2018042600002的maxNo=2      
# DECLARE oldOrderNo CHAR (13) DEFAULT '' ;-- 定义oldOrderNo为离现在最近的订单编号，默认为空     
# DECLARE newOrderNo CHAR (13) DEFAULT '' ;-- 定义newOrderNo为新生成的订单编号，默认为空




#----------------------------------------------- MySQL字符串相加函数用法-------------------------------
# 在MySQL数据库中是不能使用+等运算符来进行MySQL字符串的实际连接。需要使用的是concat()函数。
# 例如：update company set note=concat(note,'hello')
# 上面的语句就是在字段note字段值后面MySQL字符串hello后再赋值给字段note
# 列参与相加不能直接用加号(+)，需要引用函数concat，
# 例： concat('字符串',concat(列名,'字符串')) 上面的例子是包含了两次相加。
# 普通字符串直接相加即可 '字符串'+'字符串'。 MySQL的日期类型可以当作MySQL字符串处理。





#------------------------------------------------在sql中定义并赋值变量----------------------------------
declare @x int,@y varchar(20),@z datetime,@k datetime
select @x=1,@y='海昌',@z='2019-01-01',@k='2019-06-30'

#在sql中使用like后接变量时 
WHERE pinpai LIKE ('%'+@y+'%')

#在sql中使用like后接字段时 
 LIKE qianzhui_yxyj.spqzid+'%'
 



# -------------------------------------------- group by 的意思为分组汇总。------------------------------------------
使用了group by 后，要求Select出的结果字段都是可汇总的，否则就会出错。
group by 有一个原则,就是 select 后面的所有列中,没有使用聚合函数的列,必须出现在 group by 后面。
比如，有：{学号，姓名，性别，年龄，成绩}字段
这样写：
SELECT 学号，姓名，性别，年龄，sum(成绩)
FROM 学生表
GROUP BY 学号
就是错的，因为 “姓名、性别、年龄”未被汇总，且不一定是单一。
这样写：
SELECT MAX(学号)，MAX(姓名)，MAX(性别)，MAX(年龄)，sum(成绩)
FROM 学生表
GROUP BY 学号
是对的，汇总出每一同学号学生的总成绩。注意的是，只要学号相同，别的如果有不同，取它们值最大的一条作为显示输出。
这样写：
SELECT 学号，姓名，性别，年龄，sum(成绩)
FROM 学生表
GROUP BY 学号，姓名，性别，年龄
这样写也是对的，但注意的是，学号，姓名，性别，年龄中，只要有一个不同，就会当成另一条记录来汇总。



# ---------------------------------------关键词 DISTINCT 用于返回唯一不同的值。----------------------------------
# 语法：
SELECT DISTINCT 列名称 FROM 表名称
# 如：
SELECT DISTINCT Company FROM table_name



# ---------------------------------------ORDER BY 语句用于对结果集进行排序。-------------------------------------
# ORDER BY 语句默认按照升序对记录进行排序。
# 如果您希望按照降序对记录进行排序，可以使用 DESC 关键字。
# 如：
SELECT Company, OrderNumber FROM Orders ORDER BY Company
# 降序：
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC
# 可以对多列以不同方式排序
# 如：
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC



# --------------------------LIKE 操作符 与 通配符 % _ [charlist] [^charlist]或者[!charlist]-------------------------
%	                              替代一个或多个字符
_	                              仅替代一个字符
[charlist]	                      字符列中的任何单一字符
[^charlist] 或者 [!charlist]      不在字符列中的任何单一字符

# 例：
SELECT * FROM Persons WHERE City LIKE 'Ne%'
SELECT * FROM Persons WHERE City LIKE '%lond%'
# 现在，我们希望从上面的 "Persons" 表中选取名字的第一个字符之后是 "eorge" 的人：
# 我们可以使用下面的 SELECT 语句：
SELECT * FROM Persons WHERE FirstName LIKE '_eorge'
# 我们希望从 "Persons" 表中选取的这条记录的姓氏以 "C" 开头，然后是一个任意字符，然后是 "r"，然后是任意字符，然后是 "er"：
# 我们可以使用下面的 SELECT 语句：
SELECT * FROM Persons WHERE LastName LIKE 'C_r_er'
# 现在，我们希望从上面的 "Persons" 表中选取居住的城市以 "A" 或 "L" 或 "N" 开头的人：
# 我们可以使用下面的 SELECT 语句：
SELECT * FROM Persons WHERE City LIKE '[ALN]%'
# 现在，我们希望从上面的 "Persons" 表中选取居住的城市不以 "A" 或 "L" 或 "N" 开头的人：
# 我们可以使用下面的 SELECT 语句：
SELECT * FROM Persons WHERE City LIKE '[!ALN]%'



# ------------------------------------IN 操作符---------------------------------------
# IN 操作符允许我们在 WHERE 子句中规定多个值。
# SQL IN 语法
SELECT column_name(s) FROM table_name WHERE column_name IN (value1,value2,...)
# 例：
# 现在，我们希望从上表中选取姓氏为 Adams 和 Carter 的人：
# 我们可以使用下面的 SELECT 语句：
SELECT * FROM Persons WHERE LastName IN ('Adams','Carter')



#---------------------- UNION 操作符用于合并两个或多个 SELECT 语句的结果集。-----------------------------
# 请注意，UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。
# SQL UNION 语法
SELECT column_name(s) FROM table_name1
UNION   #只列出不同的
SELECT column_name(s) FROM table_name2
# 注释：默认地，UNION 操作符选取不同的值。如果允许重复的值，请使用 UNION ALL。

# SQL UNION ALL 语法
SELECT column_name(s) FROM table_name1
UNION ALL   #会列出所有
SELECT column_name(s) FROM table_name2
# 另外，UNION 结果集中的列名总是等于 UNION 中第一个 SELECT 语句中的列名。



# ---------------------------------------------SQL Date 函数  日期-----------------------------------------

# MySQL Date 函数
# 下面的表格列出了 MySQL 中最重要的内建日期函数：
NOW()	    返回当前的日期和时间
CURDATE()	返回当前的日期
CURTIME()	返回当前的时间
DATE()	    提取日期或日期/时间表达式的日期部分
EXTRACT()	返回日期/时间按的单独部分
DATE_ADD()	给日期添加指定的时间间隔
DATE_SUB()	从日期减去指定的时间间隔
DATEDIFF()	返回两个日期之间的天数
DATE_FORMAT()	用不同的格式显示日期/时间

# SQL Server Date 函数
# 下面的表格列出了 SQL Server 中最重要的内建日期函数：
GETDATE()	返回当前日期和时间
DATEPART()	返回日期/时间的单独部分
DATEADD()	在日期中添加或减去指定的时间间隔
DATEDIFF()	返回两个日期之间的时间
CONVERT()	用不同的格式显示日期/时间

# SQL Date 数据类型
# MySQL 使用下列数据类型在数据库中存储日期或日期/时间值：
DATE - 格式 YYYY-MM-DD
DATETIME - 格式: YYYY-MM-DD HH:MM:SS
TIMESTAMP - 格式: YYYY-MM-DD HH:MM:SS
YEAR - 格式 YYYY 或 YY

# SQL Server 使用下列数据类型在数据库中存储日期或日期/时间值：
DATE - 格式 YYYY-MM-DD
DATETIME - 格式: YYYY-MM-DD HH:MM:SS
SMALLDATETIME - 格式: YYYY-MM-DD HH:MM:SS
TIMESTAMP - 格式: 唯一的数字


#------------------------------------------------------ SQL 函数-----------------------------------------------
# 函数的语法
# 内建 SQL 函数的语法是：
SELECT function(列) FROM 表
# 函数的类型
# 在 SQL 中，基本的函数类型和种类有若干种。函数的基本类型是：
Aggregate 函数
Scalar 函数
# 合计函数（Aggregate functions）
# Aggregate 函数的操作面向一系列的值，并返回一个单一的值。

# 在 SQL Server 中的合计函数
AVG(column)	                返回某列的平均值 
COUNT(column)              	返回某列的行数（不包括NULL值）
COUNT(*)	                返回被选行数
COUNT(DISTINCT column)   	返回相异结果的数目
FIRST(column)	            返回在指定的域中第一个记录的值（SQLServer2000 不支持）
LAST(column)	            返回在指定的域中最后一个记录的值（SQLServer2000 不支持）
MAX(column)	                返回某列的最高值
MIN(column)	                返回某列的最低值
SUM(column)	                返回某列的总和


#---------------------------------------------------- SQL HAVING 子句--------------------------------------------------
# HAVING 子句
# 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与合计函数一起使用。
# SQL HAVING 语法
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
HAVING aggregate_function(column_name) operator value
# 如：
# 现在，我们希望查找订单总金额少于 2000 的客户。
# 我们使用如下 SQL 语句：
SELECT Customer,SUM(OrderPrice) FROM Orders
GROUP BY Customer
HAVING SUM(OrderPrice)<2000


# UCASE() 函数
# UCASE 函数把字段的值转换为大写。
# SQL UCASE() 语法
SELECT UCASE(column_name) FROM table_name


# LCASE() 函数
# LCASE 函数把字段的值转换为小写。
# SQL LCASE() 语法
SELECT LCASE(column_name) FROM table_name


# -----------------------------------MID() 函数 在sqlserver中是substring()函数------------------------------------
# MID 函数用于从文本字段中提取字符。
# SQL MID() 语法
SELECT MID(column_name,start[,length]) FROM table_name
# 参数           描述
column_name     必需。要提取字符的字段。
start	        必需。规定开始位置（起始值是 1）。
length       	可选。要返回的字符数。如果省略，则 MID() 函数返回剩余文本。
# 如：
# 现在，我们希望从 "City" 列中提取前 3 个字符。
# 我们使用如下 SQL 语句：
SELECT MID(City,1,3) as SmallCity FROM Persons


# LEN() 函数
# LEN 函数返回文本字段中值的长度。
# SQL LEN() 语法
SELECT LEN(column_name) FROM table_name


# ROUND() 函数
# ROUND 函数用于把数值字段舍入为指定的小数位数。
# SQL ROUND() 语法
SELECT ROUND(column_name,decimals) FROM table_name
# 如：
# 现在，我们希望把名称和价格舍入为最接近的整数。
# 我们使用如下 SQL 语句：
SELECT ProductName, ROUND(UnitPrice,0) as UnitPrice FROM Products


# ----------------------------------------------NOW() 函数----------------------------------------------
# NOW 函数返回当前的日期和时间。
# 提示：如果您在使用 Sql Server 数据库，请使用 getdate() 函数来获得当前的日期时间。
# SQL NOW() 语法
SELECT NOW() FROM table_name


# ---------------------------------------------FORMAT() 函数--------------------------------------------
# FORMAT 函数用于对字段的显示进行格式化。
# SQL FORMAT() 语法
SELECT FORMAT(column_name,format) FROM table_name
# 如：
# 现在，我们希望显示每天日期所对应的名称和价格（日期的显示格式是 "YYYY-MM-DD"）。
# 我们使用如下 SQL 语句：
SELECT ProductName, UnitPrice, FORMAT(Now(),'YYYY-MM-DD') as PerDate FROM Products





---------------------------------------------MySQL函数-------------------------------------------------
参考网址：https://www.yiibai.com/mysql/functions.html#article-start


--------------------------------------------MySQL聚合函数-----------------------------------------------
MySQL聚合函数 - 提供最常用的MySQL聚合函数的简要概述。
avg()函数 -  计算一组值或表达式的平均值。
count()函数 - 计算表中的行数。
instr()函数 - 返回子字符串在字符串中第一次出现的位置。
sum()函数 - 计算一组值或表达式的总和。
min()函数 - 在一组值中找到最小值。
max()函数 - 在一组值中找到最大值。
group_concat()函数 - 将字符串从分组中连接成具有各种选项(如DISTINCT，ORDER BY和SEPARATOR)的字符串。
MySQL标准偏差函数 - 显示如何计算人口标准偏差和样本标准偏差。




------------------------------------------MySQL字符串函数---------------------------------------------
concat()函数 - 将两个或多个字符串组合成一个字符串。
length()函数&char_length()函数 - 以字节和字符获取字符串的长度。
left()函数 - 获取指定长度的字符串的左边部分。
replace()函数 - 搜索并替换字符串中的子字符串。
substring()函数 - 从具有特定长度的位置开始提取一个子字符串。
trim()函数 - 从字符串中删除不需要的字符。
find_in_set()函数 - 在逗号分隔的字符串列表中找到一个字符串。
format()函数 - 格式化具有特定区域设置的数字，舍入到小数位数。




---------------------------------------------MySQL控制流函数-----------------------------------------
case()函数 - 如果满足WHEN分支中的条件，则返回THEN分支中的相应结果，否则返回ELSE分支中的结果。
if语句 - 根据给定的条件返回一个值。
ifnull()函数 - 如果第一个参数不为NULL，则返回第一个参数，否则返回第二个参数。
nullif()函数 - 如果第一个参数等于第二个参数，则返回NULL，否则返回第一个参数。
1、if (expr1,expr2,expr3) 　　　　　　　　　　#如果expr1成立，则返回expr2，否则返回expr3
示例：
select  name, if (sex=1,'男','女')  sex  from  tb_user	　　　　　　	#如果sex是1，sex查询结果返回‘男’，否则返回‘女’

2、ifnull(expr1,expr2)	　　　　　　　　　　　　	#如果expr1不为null，则返回expr1，否则返回expr2
示例：
select  name  姓名, ifnull(sex, '其他')  sex  from  tb_user 　　　　　　　　　　 #如果sex是null，则返回‘其他；sex不是null，则正常返回

3、case  column_name  when  expr1  then  result1  else  result2  end 
#如果column_name是1，sex查询结果返回‘男’，否则返回‘女’
示例：
select  name  名字,  case  sex  when  1  then   '男'   else   '女'   end   性别  from  tb_user
#如果sex是1，sex查询结果返回‘男’，否则返回‘女’

4、case  column_name  when  expr1  then  result1  when  expr2  then  result2  end 
#如果column_name是expr1返回result1，如果column_name是expr2返回result2，when * then *可以写多个，end 表示结束
示例1：
select   name  名字,  case  sex  when  1  then  '男'   when  2  then  '女'  end  性别  from   tb_user
#如果sex是1，sex查询结果返回‘男’；sex是2，sex查询结果返回‘女’

示例2（多条件）：
select  name  名字, case  sex  when  1  then  '男'  when  2  then  '女'  end  性别,  case  when  age<=16   then  '未成年'   when  age>16   and   age<=30   then  '青年'   when   age>30  and   age<=50  then   '壮年'   else   '老年'   end   年龄   from   tb_user
#年龄小于等于16显示为‘未成年’；年龄大于16且小于等于30显示为‘青年’；
#年龄大于30且小于等于50显示为‘壮年’；年龄大于50显示为‘老年’；




--------------------------------------------MySQL日期和时间函数--------------------------------------
curdate()函数 - 返回当前日期。
datediff()函数 - 计算两个DATE值之间的天数。
day()函数 - 获取指定日期月份的天(日)。
date_add()函数 - 将时间值添加到日期值。
date_sub()函数 - 从日期值中减去时间值。
date_format()函数 - 根据指定的日期格式格式化日期值。
dayname()函数 - 获取指定日期的工作日的名称。
dayofweek()函数 - 返回日期的工作日索引。
extract()函数 - 提取日期的一部分。
now()函数 - 返回当前日期和时间。
month()函数 - 返回一个表示指定日期的月份的整数。
str_to_date()函数 - 将字符串转换为基于指定格式的日期和时间值。
sysdate()函数 - 返回当前日期。
timediff()函数 - 计算两个TIME或DATETIME值之间的差值。
timestampdiff()函数 - 计算两个DATE或DATETIME值之间的差值。
week()函数 -  返回一个日期的星期数值。
weekday()函数 - 返回一个日期表示为工作日/星期几的索引。
year()函数 - 返回日期值的年份部分。




-------------------------------------------------MySQL比较函数---------------------------------------------
coalesce()函数 - 返回第一个非NULL参数，这非常适合用于将值替换为NULL。
greatest()函数&least()函数 – 使用n个参数，并分别返回n个参数的最大值和最小值。
isnull()函数 - 如果参数为NULL，则返回1，否则返回0。




-------------------------------------------------其他MySQL函数--------------------------------------------
last_insert_id()函数 - 获取最后插入的记录的最后生成的序列号。
cast()函数 - 将任何类型的值转换为具有指定类型的值。
CONVERT(nvarchar(30), GETDATE(), 126) 日期转换为字符串











(5) 数据记录统计函数：
AVG(字段名) 得出一个表格栏平均值
COUNT(*;字段名) 对数据行数的统计或对某一栏有值的数据行数统计
MAX(字段名) 取得一个表格栏最大的值
MIN(字段名) 取得一个表格栏最小的值
SUM(字段名) 把数据栏的值相加
引用以上函数的方法：
sql="select sum(字段名) as 别名 from 数据表 where 条件表达式"
set rs=conn.excute(sql)
用 rs("别名") 获取统计的值，其它函数运用同上。
查询去除重复值：select distinct * from table1
(6) 数据表的建立和删除：
CREATE TABLE 数据表名称(字段1 类型1(长度),字段2 类型2(长度) …… )
(7) 单列求和:
SELECT SUM(字段名) FROM 数据表
最新语句编辑
查询数据库中含有同一这字段的表：
select name from sysobjects where xtype = 'u' and id in(select id from syscolumns where name = 's3')
根据出生日期可以算出年龄：
select datediff(year,scrq,'2013') as 年龄 from page_shsjgrgl
根据当前年份自动算出年龄
select datediff(year,csny,cast(YEAR(GETDATE()) as char))
年
select year(djsj) from page_shsjgrgl
月
select month(djsj) from page_shsjgrgl
日
select day(djsj) from page_shsjgrgl
在同一数据库中复制表结构：
select * into a from b where 1<>1
当 IDENTITY_INSERT 设置为 OFF 时，不能为表 'aa' 中的标识列插入显式值。
set identity_insert aa ON----设置打开，
批量插入：
insert into aa(Customer_ID, ID_Type, ID_Number) select Customer_ID, ID_Type, ID_Number from TCustomer;
set identity_insert aa OFF－－－关闭
不同数据库之间的复制：
复制结构：
select * into test.dbo.b from GCRT.dbo.page_shsjgrgl where 1<>1
复制内容：
insert into test.dbo.b(xm,ssdq) select xm,ssdq from GCRT.dbo.page_shsjgrgl
查看数据库中所有的数据表表名：
select name from SysObjects where type='u'
查看数据库中所有表含有同一字段的表：
select name from sysobjects where xtype = 'u' and id in(select id from syscolumns where name = '同一字段')
查看数据表中的所有字段：
select name from Syscolumns where id=object_id('表名')
查询数据库时前10条记录：
select top 10 * from td_areacode order by newid()
修改字段类型：
ALTER TABLE 表名 ALTER COLUMN 字段名 varchar(30) NOT NULL
use ZHJIANGJGYL
declare @temp nvarchar(30)
set @temp = 'ZWI4'
select hllx from page_yljg_zyry where hllx not in(
select
case @temp when ''
then ''
else b1 end
from (
select * from TD_Code where page_en='page_yljg_zyry' and B2='ZWI'
) s where s.b1 !=
case @temp when '' then '' else @temp end
)
更改数据库表字段类型：
alter table page_shsjgrgl alter column s1 int
高级查询
A：UNION运算符
UNION 运算符通过组合其他两个结果表（例如TABLE1 和TABLE2）并消去表中任何重复行而派生出一个结果表。当 ALL 随UNION 一起使用时（即UNION ALL），不消除重复行。两种情况下，派生表的每一行不是来自TABLE1 就是来自TABLE2。
B： EXCEPT运算符
EXCEPT 运算符通过包括所有在TABLE1 中但不在TABLE2 中的行并消除所有重复行而派生出一个结果表。当ALL 随EXCEPT 一起使用时(EXCEPT ALL)，不消除重复行。
C：INTERSECT运算符
INTERSECT 运算符通过只包括TABLE1 和TABLE2 中都有的行并消除所有重复行而派生出一个结果表。当ALL 随INTERSECT 一起使用时(INTERSECT ALL)，不消除重复行。
注：使用运算词的几个查询结果行必须是一致的。
外连接
A、left outer join：
左外连接（左连接）：结果集既包括连接表的匹配行，也包括左连接表的所有行。
SQL: select a.a, a.b, a.c, b.c, b.d, b.f from a LEFT OUT JOIN b ON a.a = b.c
B：right outer join:
右外连接(右连接)：结果集既包括连接表的匹配连接行，也包括右连接表的所有行。
C：full outer join：
全外连接：不仅包括符号连接表的匹配行，还包括两个连接表中的所有记录。
判断对象编辑
判断数据库是否存在
if exists (select* from sysdatabases where name = '数据库名')
dropdatabase[数据库名]
判断表是否存在
if not exists (select * from sysobjects where [name] = '表名' and xtype='U')
begin
--这里创建表
end
判断存储过程是否存在
if exists (select*fromsysobjectswhereid = object_id(N'[存储过程名]') and OBJECTPROPERTY(id, N'IsProcedure') = 1)
dropprocedure[存储过程名]
判断临时表是否存在
if object_id('tempdb..#临时表名')isnot null
droptable#临时表名
判断视图是否存在
--SQL Server 2000
IF EXISTS (SELECT*FROMsysviewsWHEREobject_id = '[dbo].[视图名]'
--SQL Server 2005
IF EXISTS (SELECT*FROMsys.viewsWHEREobject_id = '[dbo].[视图名]'
判断函数是否存在
if exists (select*fromdbo.sysobjectswhereid = object_id(N'[dbo].[函数名]') and xtype in (N'FN', N'IF', N'TF'))
dropfunction[dbo].[函数名]
获取创建信息
SELECT[name],[id],crdateFROMsysobjectswherextype='U'
/*
xtype 的表示参数类型，通常包括如下这些 C =CHECK约束 D = 默认值或DEFAULT约束 F =FOREIGNKEY约束 L =日志FN =标量函数IF = 内嵌表函数 P =存储过程PK =PRIMARYKEY约束（类型是K） RF = 复制筛选存储过程 S = 系统表 TF = 表函数 TR =触发器U = 用户表 UQ =UNIQUE约束（类型是K） V = 视图 X = 扩展存储过程 */
判断列是否存在
if exists(select*fromsyscolumnswhereid=object_id('表名') andname='列名')
altertable表名dropcolumn列名
判断列是否自增列
if columnproperty(object_id('table'),'col','IsIdentity')=1
print '自增列'
else
print '不是自增列'
SELECT*FROMsys.columnsWHEREobject_id=OBJECT_ID('表名')
AND is_identity=1
判断表中是否存在索引
if exists(select*fromsysindexeswhereid=object_id('表名') andname='索引名')
print '存在'
else
print '不存在
查看数据库中对象
SELECT*FROMsysobjectsWHEREname='对象名'
select * from table（所要查询的表名） where coloum(条件)
提升编辑
复制表
(只复制结构，源表名：a 新表名：b) (Access可用)
法一：select * into b from a where 1<>1
法二：select top 0 * into b from a
拷贝表
(拷贝数据,源表名：a 目标表名：b) (Access可用)
insert into b(x, y, z) select d,e,f from a;
跨数据库之间表的拷贝
(具体数据使用绝对路径) (Access可用)
insert into b(x, y, z) select d,e,f from a in ‘具体数据库’ where 条件
例子：。.from b in '"&Server.MapPath("."&"\data.mdb" &"' where..
子查询
(表名1：a 表名2：b)
select a,b,c from a where a IN (select d from b 或者： select a,b,c from a where a IN (1,2,3)
显示文章最后时间
select a.title,a.username,b.adddate from table a,(select max(adddate) adddate from table where table.title=a.title) b
外连接查询
(表名1：a 表名2：b)
select a.a, a.b, a.c, b.c, b.d, b.f from a LEFT OUT JOIN b ON a.a = b.c
在线视图查询
(表名1：a
select * from (Select a,b,c FROM a) T where t.a > 1;
between的用法
between为查询某字段的指定范围，限制查询数据范围时包括了边界值，not between不包括边界值
select * from table1 where time between time1 and time2
select a,b,c, from table1 where a not between 数值1 and 数值2
in 的使用方法
select * from table1 where a [not] in (‘值1’，’值2’,’值4’，’值6’)
删除主表没有的信息
两张关联表delete from table1 where not exists ( select * from table2 where table1.field1=table2.field1
四表联查问题
select * from a left inner join b on a.a=b.b right inner join c on a.a=c.c inner join d on a.a=d.d where .....
日程安排提前五分钟
SQL: select * from 日程安排 where datediff('minute',f开始时间，getdate())>5
一条sql 搞定数据库页
select top 10 b.* from (select top 20 主键字段,排序字段 from 表名 order by 排序字段 desc) a,表名 b where b.主键字段= a.主键字段 order by a.排序字段
前10条记录
select top 10 * from table1 where 范围
选择排名
选择在每一组b值相同的数据中对应的a最大的记录的所有信息(类似这样的用法可以用于论坛每月排行榜，每月热销产品分析,按科目成绩排名，等等。)
select a,b,c from tablename ta where a=(select max(a) from tablename tb where tb.b=ta.b)
派生结果表
包括所有在TableA 中但不在TableB和TableC 中的行并消除所有重复行而派生出一个结果表
(select a from tableA except (select a from tableB) except (select a from tableC)
随机取出10条数据
select top 10 * from tablename order by newid()
随机选择记录
select newid()
删除重复记录
Delete from tablename where id not in (select max(id) from tablename group by col1,col2,...)
列出数据库里的表名
select name from sysobjects where type='U'
列出表里的所有的
select name from syscolumns where id=object_id('TableName')
列示排列
列示type、vender、pcs字段，以type字段排列，case可以方便地实现多重选择，类似select 中的case。
select type,sum(case vender when 'A' then pcs else 0 end),sum(case vender when 'C' then pcs else 0 end),sum(case vender when 'B' then pcs else 0 end) FROM tablename group by type
显示结果：
type vender pcs
电脑A 1
电脑A 1
光盘B 2
光盘A 2
手机B 3
手机C 3
初始化表table1
TRUNCATE TABLE table1
选择从10到15的记录
select top 5 * from (select top 5 * from (select top 15 * from table order by id asc) table_别名 order by id desc) table_2 order by id
数据类型转换
declare @numid int
declare @id varchar(50)
set @numid=2005
set @id=convert(varchar,@numid)
通过上述语句完成数据类型Int转换成varchar，其他转换类似，可参看convert函数
技巧编辑
1=1，1=2的使用
在SQL语句组合时用的较多
“where 1=1”是表示选择全部 “where 1=2”全部不选，
如：
if @strWhere !='
begin
set @strSQL = 'select count(*) as Total from [' + @tblName + '] where ' + @strWhere
end
else
begin
set @strSQL = 'select count(*) as Total from [' + @tblName + ']'
end
我们可以直接写成
set @strSQL='select count(*) as Total from tablename where 1+1'
if(@strWhere!='')
{set @strSQL=@strSQL+’and’+strWhere}
收缩数据库
--重建索引
DBCC REINDEX
DBCC INDEXDEFRAG
--收缩数据和日志
DBCC SHRINKDB
DBCC SHRINKFILE
压缩数据库
dbcc shrinkdatabase(dbname)0

4
转移数据库给新用户以已存在用户权限
exec sp_change_users_login 'update_one','newname','oldname'
go
检查备份集
RESTORE VERIFYONLY from disk='E:\dvbbs.bak'
修复数据库
Alter DATABASE [dvbbs] SET SINGLE_USER
GO
DBCC CHECKDB('dvbbs',repair_allow_data_loss) WITH TABLOCK
GO
Alter DATABASE [dvbbs] SET MULTI_USER
GO
日志清除
SET NOCOUNT ON
DECLARE @LogicalFileName sysname,
@MaxMinutes INT,
@NewSize INT
USE tablename -- 要操作的数据库名
Select @LogicalFileName = 'tablename_log', --日志文件名
@MaxMinutes = 10, -- Limit on time allowed to wrap log.
@NewSize = 1 -- 你想设定的日志文件的大小(M)
-- Setup / initialize
DECLARE @OriginalSize int
Select @OriginalSize = size
FROM sysfiles
Where name = @LogicalFileName
Select 'Original Size of ' + db_name() + ' LOG is ' +
CONVERT(VARCHAR(30),@OriginalSize) + ' 8K pages or ' +
CONVERT(VARCHAR(30),(@OriginalSize*8/1024)) + 'MB'
FROM sysfiles
Where name = @LogicalFileName
Create TABLE DummyTrans
(DummyColumn char (8000) not null)
DECLARE @Counter INT,
@StartTime DATETIME,
@TruncLog VARCHAR(255)
Select @StartTime = GETDATE(),
@TruncLog = 'BACKUP LOG ' + db_name() + ' WITH TRUNCATE_ONLY'
DBCC SHRINKFILE (@LogicalFileName, @NewSize)
EXEC (@TruncLog)
-- Wrap the log if necessary.
WHILE @MaxMinutes > DATEDIFF (mi, @StartTime, GETDATE()) -- time has not expired
AND @OriginalSize = (Select size FROM sysfiles Where name = @LogicalFileName)
AND (@OriginalSize * 8 /1024) > @NewSize
BEGIN -- Outer loop.
Select @Counter = 0
WHILE ((@Counter < @OriginalSize / 16) AND (@Counter < 50000))
BEGIN -- update
Insert DummyTrans VALUES ('Fill Log')
Delete DummyTrans
Select @Counter = @Counter + 1
END
EXEC (@TruncLog)
END
Select 'Final Size of ' + db_name() + ' LOG is ' +
CONVERT(VARCHAR(30),size) + ' 8K pages or ' +
CONVERT(VARCHAR(30),(size*8/1024)) + 'MB'
FROM sysfiles
Where name = @LogicalFileName
Drop TABLE DummyTrans
SET NOCOUNT OFF
更改某个表
exec sp_changeobjectowner 'tablename','dbo'
存储更改全部表
Create PROCEDURE dbo.User_ChangeObjectOwnerBatch
@OldOwner as NVARCHAR(128),
@NewOwner as NVARCHAR(128)
AS
DECLARE @Name as NVARCHAR(128)
DECLARE @Owner as NVARCHAR(128)
DECLARE @OwnerName as NVARCHAR(128)
DECLARE curObject CURSOR FOR
select 'Name' = name,
'Owner' = user_name(uid)
from sysobjects
where user_name(uid)=@OldOwner
order by name
OPEN curObject
FETCH NEXT FROM curObject INTO @Name, @Owner
WHILE(@@FETCH_STATUS=0)
BEGIN
if @Owner=@OldOwner
begin
set @OwnerName = @OldOwner + '.' + rtrim(@Name)
exec sp_changeobjectowner @OwnerName, @NewOwner
end
-- select @name,@NewOwner,@OldOwner
FETCH NEXT FROM curObject INTO @Name, @Owner
END
close curObject
deallocate curObject
GO
循环写入数据
declare @i int
set @i=1
while @i<30
begin
insert into test (userid) values(@i)
set @i=@i+1
end










创建数据库
创建之前判断该数据库是否存在
if exists (select * from sysdatabases where name='databaseName')
drop database databaseName
go
Create DATABASE databasename
on primary-- 默认就属于primary文件组,可省略
（
/*--数据文件的具体描述--*/
name=‘databasename_data’，-- 主数据文件的逻辑名称
filename=‘'所存位置：\databasename_data.mdf’， -- 主数据文件的物理名称
size=数值mb, --主数据文件的初始大小
maxsize=数值mb, -- 主数据文件增长的最大值
filegrowth=数值%--主数据文件的增长率
）
log on
（
/*--日志文件的具体描述,各参数含义同上--*/
name='databasename_log', -- 日志文件的逻辑名称
filename='所存目录:\databasename_log.ldf', -- 日志文件的物理名称
size=数值mb, --日志文件的初始大小
filegrowth=数值%--日志文件的增长值
）
删除数据库
drop database databasename
备份
--- 创建备份数据的 device
USE master
EXEC sp_addumpdevice 'disk', 'testBack', 'c:\mssql7backup\MyNwind_1.dat'
--- 开始备份
BACKUP DATABASE pubs TO testBack
创建新表
create table tabname(col1 type1 [not null] [primary key] identity(起始值,递增量)
,col2 type2 [not null],..)--primary key为主键 identity表示递增数量
根据已有的表创建新表：
A：go
use 原数据库名
go
select * into 目的数据库名.dbo.目的表名 from 原表名(使用旧表创建新表)
B：create table tab_new as select col1,col2… from tab_old definition only
创建序列
create sequence SIMON_SEQUENCE
minvalue 1 -- 最小值
maxvalue 999999999999999999999999999 -- 最大值
start with 1 -- 开始值
increment by 1 -- 每次加几
cache 20;
删除表
drop table tabname--这是将表连同表中信息一起删除但是日志文件中会有记录
删除信息
delete from table_name-这是将表中信息删除但是会保留这个表
增加列
Alter table table_name add column_name column_type [default 默认值]--在表中增加一列，[]内的内容为可选项
删除列
Alter table table_name drop column column_name--从表中删除一列
添加主键
Alter table tabname add primary key(col)
说明：删除主键：Alter table tabname drop primary key(col)
创建索引
create [unique] index idxname on tabname(col…。)
删除索引：drop index idxname on tabname
注：索引是不可更改的，想更改必须删除重新建。
创建视图
create view viewname as select statement
删除视图：drop view viewname












-------------------------------------------MySQL一些好用的函数---------------------------------------------
一、增强查询语句的函数：
1、on duplicate key update 新增或者更新数据（这个语法慎用，当设置了唯一索引时，如果更新的数据唯一索引已在数据库存在，但主键不一致，会导致更新失效；另外如果更新进去的数据跟数据库完全一致，虽然是更新，但返回的是1）
2、if（a?,b,c），有点像三元运算符，a为条件，b为条件成立时的值，c为条件不成立时的值
3、设置主键为uuid：
UPDATE t_mdm_cus_customer_copy SET mdm_id = UUID()
UPDATE t_mdm_cus_customer_copy SET mdm_id = REPLACE(UUID(),'-','')
4、union用于连接两个以上的select语句，将结果合并到一起，重复数据会被删除
5、使用group by查询数据时获取的是查询结果的第一条，想要获取最新一条可以跟order by结合使用，但是注意要加上limit（这就很鸡肋）参考博客：https://blog.csdn.net/HXNLYW/article/details/102681680
6、mysql中将查询结果的list转为一个字段，使用函数group_concat()；
7、查询是否存在满足条件的记录时，不要使用select count(*)查询全表，可使用select 1 from table where 条件 limit 1 在查询到一条满足条件的记录时就返回，提高效率；
8、Row_Number() OVER()对重复数据进行分组编号排序：https://www.cnblogs.com/weifeng123/p/8931598.html；
9、没有主键时count(1)更快，有主键时查询行数可使用count(*)，msysql5.6之后的版本做了优化，会使用最优方式来进行查询，count(字段名)会过滤掉为null的记录；

二、时间相关：
1、字符串转时间：UPDATE TABLE SET add_date = STR_TO_DATE(add_date,'%Y-%m-%d %H:%i:%s')
2、时间转字符串：select date_format(now(), '%Y-%m-%d');
3、时间转时间戳：select unix_timestamp(now());
4、字符串转时间戳：select unix_timestamp('2016-01-02');
5、时间戳转时间：select from_unixtime(1451997924);
6、时间戳转字符串：select from_unixtime(1451997924,'%Y-%d');
7、获取时间差函数：
TIMESTAMPDIFF：按指定方式获取时间差
–相差1天
　　select TIMESTAMPDIFF(DAY, '2018-03-20 23:59:00', '2015-03-22 00:00:00');
　　--相差49小时
　　select TIMESTAMPDIFF(HOUR, '2018-03-20 09:00:00', '2018-03-22 10:00:00');
　　--相差2940分钟
　　select TIMESTAMPDIFF(MINUTE, '2018-03-20 09:00:00', '2018-03-22 10:00:00');
　　--相差176400秒
　　select TIMESTAMPDIFF(SECOND, '2018-03-20 09:00:00', '2018-03-22 10:00:00');
DATEDIFF：获取相差的天数
– 相差2天
　　select DATEDIFF('2018-03-22 09:00:00', '2018-03-20 07:00:00');

三、json相关
关于mysql的json类型可参考：https://blog.csdn.net/ghostyusheng/article/details/84260831，https://blog.csdn.net/qq_21187515/article/details/90760337，https://www.cnblogs.com/waterystone/p/5626098.html
1、查找json格式列的指定字段值：SELECT json_extract(字段名,'$.json结构') FROM 表名
2、查找json格式列中的指定属性（不带双引号）：select json->>'$.field' from table 或者 select json_unquote(json_extract(json,'$.field')) from table
3、比较json格式字段时，除了比较内容外，还需要比较类型，因此需要使用cast（字段名 as json）转为json格式进行比较

四、字符串相关
1、替换字段某个字符：update 表名 set 字段名=REPLACE (字段名,'原来的值','要修改的值')
2、查询字段是否包含某个字符：like，find_in_set，locate，instr，REGEXP正则表达式函数（select field REGEXP 'abc'查找field列包含‘abc’的记录）
3、字符串截取：left（str,n）左边n位，right（str,n）右边n位，substring（str,n）从第n位开始截取
4、获取字段长度：length获取字段字节的长度（一个汉字三个字节，数字或字母一个字节）；char_length获取字段字符的个数（不区分中英文，一个中文或一个字母或一个符号都算一个字符）
5、大小写转换：小写转大写upper()；大写转小写lower()；
6、去除指定字符函数：trim()，参考：https://blog.csdn.net/moakun/article/details/82110700

五、数值计算相关
int类型的字段存储小数时会被四舍五入取整数位；
max(xx)函数求的是查询结果中某一列的最大值，greatest(a,b,c,d)函数求的是某一行数据中某几列的最大值；
查找某一列中纯数字的最大记录：SELECT MAX(cus_property_id) FROM t_mdm_cus_attributes WHERE cus_property_id REGEXP '^[0-9]+$'；

六、MySql查询内置信息的函数：
查询当前所在数据库：select database()
查询所有表信息：SELECT * FROM information_schema.tables
查询某个数据库中某个表的字段信息：SELECT * FROM information_schema.columns WHERE table_schema = 'user-center' AND table_name = 'sys_user'；

七、操作表属性相关：
设置表自增主键从哪个值开始：向表中插入数据前执行alter table user AUTO_INCREMENT=10000；




1.LOCATE
类似indexOf函数

LOCATE(substr, str), LOCATE(substr, str, pos)

第一个语法返回substr在字符串str的第一个出现的位置。

第二个语法返回字符串substr在字符串str,从pos处开始的第一次出现的位置。如果substr不在str中,则返回值为0

2.CONCAT
 CONCAT(str1,str2,…)  

 拼接函数，用于将多个字符串连接成一个字符串，返回结果为连接参数产生的字符串。如有任何一个参数为NULL ，则返回值为 NULL。

3.LENGTH/CHAR_LENGTH
用来获取字符串长度的函数

              a>、length()： 单位是字节，utf8编码下,一个汉字三个字节，一个数字或字母一个字节。gbk编码下,一个汉字两个字节，一个数字或字母一个字节。
　　　　b>、char_length()：单位为字符，不管汉字还是数字或者是字母都算是一个字符

所以，length()<>char_length()，可以用来检验是否含有中文字符。

4.CAST
类型转换函数

语法：CAST( value AS type )

SELECT CAST(1995 AS CHAR) as result
运行结果："1995"
 
SELECT CAST('2019-08-29 16:50:21' as date) as result
运行结果：2019-08-29
 
SELECT CAST('2019-08-29 16:50:21' as DATETIME) as result
运行结果：2019-08-29 16:50:21
 
SELECT CAST('2019-08-29 16:50:21' as TIME) as result
运行结果：16:50:21
 
SELECT CAST(220.23211231 AS DECIMAL(10, 3)) AS result 
运行结果：220.232
 


 












