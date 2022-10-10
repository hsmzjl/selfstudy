# -----------------------------------------------基本语句--------------------------------------------
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



# ---------------------------------------------预定义变量--------------------------------------------
定义字符串 @变量名 类型（长度）
DECLARE @A VARCHAR(50),@B VARCHAR(20),@C VARCHAR(20)

定义整数 @变量名 类型
DECLARE @A INT

定义表变量 @变量名 类型
DECLARE @A TABLE(kehu varchar(200),khname varchar(200),khcode varchar(200))

##变量赋值##
方式1 
SET @A=1
SET @A='23'
SET @A=(SELECT MAX(number) FROM MASTER..spt_values)

方式2   
赋值一个变量  
SELECT @A='XYZ'  
赋值多个变量  
SELECT @A='XYZ',@B='CC'  
赋值表变量  
INSERT INTO @A SELECT kehu,khname,khcode FROM kh  




# -----------------------关键词 DISTINCT 用于返回唯一不同的值。---------------------
语法：  
SELECT DISTINCT 列名称 FROM 表名称  
如：  
SELECT DISTINCT Company FROM table_name  




# ----------------------ORDER BY 语句用于对结果集进行排序。------------------------
# ORDER BY 语句默认按照升序对记录进行排序。
# 如果您希望按照降序对记录进行排序，可以使用 DESC 关键字。
# 如：
SELECT Company, OrderNumber FROM Orders ORDER BY Company
# 降序：
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC
# 可以对多列以不同方式排序
# 如：
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC








# ---------LIKE 操作符 与 通配符 % _ [charlist] [^charlist]或者[!charlist]--------
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



#--------- UNION 操作符用于合并两个或多个 SELECT 语句的结果集。----------
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