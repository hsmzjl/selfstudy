import os 
import json
from urllib import parse

# ---------------------------------目录与文件--------------------------
#获取当前目录
os.getcwd()

# 将一个路径名分解为目录名和文件名两部分
# fpath , fname = os.path.split( "你要分解的路径")
# 例如：
a, b = os.path.split( "c:\\123\\456\\test.txt" )
print a
print b
显示：
c:\123\456
test.txt

# 分解文件名的扩展名
# fpathandname , fext = os.path.splitext( "你要分解的路径")
# 例如：
a, b = os.path.splitext( "c:\\123\\456\\test.txt" )
print a
print b
显示：
c:\123\456\test
.txt

# 判断一个路径（ 目录或文件）是否存在
b = os.path.exists( "你要判断的路径")
返回值b： True 或 False

# 判断一个路径是否文件
b = os.path.isfile( "你要判断的路径")
返回值b： True 或 False

# 判断一个路径是否目录
b = os.path.isdir( "你要判断的路径")
返回值b： True 或 False

# 获取某目录中的文件及子目录的列表        
# L = os.listdir( "你要判断的路径")
# 例如：
L = os.listdir( "c:/" )
print L
显示 :
['1.avi', '1.jpg', '1.txt', 'CONFIG.SYS', 'Inetpub', 'IO.SYS', 'KCBJGDJC', 'KCBJGDYB', 'KF_GSSY_JC', 'MSDOS.SYS', 'MSOCache', 'NTDETECT.COM', 'ntldr', 'pagefile.sys', 'PDOXUSRS.NET', 'Program Files', 'Python24', 'Python31', 'QQVideo.Cache', 'RECYCLER', 'System Volume Information', 'TDDOWNLOAD', 'test.txt', 'WINDOWS']
# 这里面既有文件也有子目录

# 获取某指定目录下的所有子目录的列表
def getDirList( p ):
        p = str( p )
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isdir( p + x ) ]
        return b
print   getDirList( "C:\\" )
# 结果:
['Documents and Settings', 'Downloads', 'HTdzh', 'KCBJGDJC', 'KCBJGDYB', 'KF_GSSY_JC', 'MSOCache', 'Program Files', 'Python24', 'Python31', 'QQVideo.Cache', 'RECYCLER', 'System Volume Information', 'TDDOWNLOAD', 'WINDOWS']

# 获取某指定目录下的所有文件的列表
def getFileList( p ):
        p = str( p )
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isfile( p + x ) ]
        return b
print   getFileList( "C:\\" )
# 结果:
['1.avi', '1.jpg', '1.txt', '123.txt', '12345.txt', '2.avi', 'a.py', 'AUTOEXEC.BAT', 'boot.ini', 'bootfont.bin', 'CONFIG.SYS', 'IO.SYS', 'MSDOS.SYS', 'NTDETECT.COM', 'ntldr', 'pagefile.sys', 'PDOXUSRS.NET', 'test.txt']

# 创建子目录
os.makedirs(   path )   # path 是"要创建的子目录"
# 例如:
os.makedirs(   "C:\\123\\456\\789")
# 调用有可能失败，可能的原因是：
# (1) path 已存在时(不管是文件还是文件夹)
# (2) 驱动器不存在
# (3) 磁盘已满
# (4)磁盘是只读的或没有写权限

# 删除子目录
os.rmdir( path )   # path: "要删除的子目录"
# 产生异常的可能原因:
# (1) path 不存在
# (2) path 子目录中有文件或下级子目录
# (3) 没有操作权限或只读
# 测试该函数时，请自已先建立子目录。

# 删除文件
os.remove(   filename )   # filename: "要删除的文件名"
# 产生异常的可能原因:
# (1)   filename 不存在
# (2) 对filename文件， 没有操作权限或只读。

# 文件改名
os.name( oldfileName, newFilename)
# 产生异常的原因：
# (1) oldfilename 旧文件名不存在
# (2) newFilename 新文件已经存在时，此时，您需要先删除 newFilename 文件。




# --------------------------------json----------------------------------
#json.dumps()  把python字典对象转换成文本
filter={}
filterstr=json.dumps(filter)

#json.loads()  把文本转换成python字典对象
json.loads(filterstr)



# ------------------------------字符串操作-----------------------------------
# 查找 替换
# Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# str.replace(old, new[, max])
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))


#r 表示该文本不转义  如果 \ 在最后一位则会出错
str=r'\fffffdsafda'


# 切片 
str = "this is string example....wow!!! this is really string"
str = str[0:3]
str[0] # 获取第一个元素
str[-2] # 获取倒数第二个元素
str[-1:-3] 和 str[2:0] 获取的为空字符，系统不提示错误: ""


# 如果要检查字符串中的前缀或后缀，请使用“.startswith()”和“.endswith()"，而不是字符串切片。它们更干净，更不容易出错
# 正确
if name.endswith('and'):
    print('Great!')



# in 
# 成员运算符 - 如果字符串中包含给定的字符返回 True
print('给发送' in 'hanz发给发送到汉字')    # 结果是 True
# not in 
# 成员运算符 - 如果字符串中不包含给定的字符返回 True
print('给发送' not in 'hanz发给发送到汉字')    # 结果是 False

# Python 的字符串内建函数
capitalize()
# 将字符串的第一个字符转换为大写
count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
find(str, beg=0, end=len(string))
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index(str, beg=0, end=len(string))
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False..
islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isnumeric()
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
isspace()
# 如果字符串中只包含空白，则返回 True，否则返回 False.
join(seq)
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
len(string)
# 返回字符串长度
lower()
# 转换字符串中所有大写字符为小写.
lstrip()
# 截掉字符串左边的空格或指定字符。
rstrip()
# 删除字符串字符串末尾的空格.
strip([chars])
# 在字符串上执行 lstrip()和 rstrip()
swapcase()
# 将字符串中大写转换为小写，小写转换为大写
upper()
# 转换字符串中的小写字母为大写
zfill (width)
# 返回长度为 width 的字符串，原字符串右对齐，前面填充0

# find 函数
# Python find() 方法检测字符串中是否包含子字符串 str ，
# 如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str.find(str, beg=0, end=len(string))
# 参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

# ------------------------------------format 格式化函数--------------------------------
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。
"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
"{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 数字格式化
print("{:.2f}".format(3.1415926))
3.14
3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
-1	        {:+.2f}	-1.00	带符号保留小数点后两位
2.71828	    {:.0f}	3	    不带小数
5	        {:0>2d}	05	    数字补零 (填充左边, 宽度为2)
5	        {:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
10	        {:x<4d}	10xx	数字补x (填充右边, 宽度为4)
1000000	    {:,}	1,000,000	以逗号分隔的数字格式
0.25	    {:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
13	        {:>10d}	        13	右对齐 (默认, 宽度为10)
13	        {:<10d}	13	    左对齐 (宽度为10)
13	        {:^10d}	    13	中间对齐 (宽度为10)
11	
'{:b}'.format(11)    1011
'{:d}'.format(11)    11
'{:o}'.format(11)    13
'{:x}'.format(11)    b
'{:#x}'.format(11)   0xb
'{:#X}'.format(11)	 0XB	进制


# -----------------------------------可迭代对象-----------------------------------
Python 编程语言中有四种集合数据类型：
列表（List）是一种有序和可更改的集合。允许重复的成员。
元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
集合（Set）是一个无序和无索引的集合。没有重复的成员。
词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

# -------------------------------字典----------------------------------
d = {key1 : value1, key2 : value2 }
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# 访问字典里的值
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
# 像这样直接访问字典中的值，如果key不存在，则会报错

# 修改字典
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 删除字典元素
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 字典内置函数&方法
len(dict)
# 计算字典元素个数，即键的总数。
radiansdict.clear()
# 删除字典内所有元素
radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
key in dict
# 如果键在字典dict里返回true，否则返回false
radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里
radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.values()
# 返回一个迭代器，可以使用 list() 来转换为列表
pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
radiansdict.keys()
# 返回一个迭代器，可以使用 list() 来转换为列表
radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组


# 字典列表排序
lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "Runoob", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wiki" , "age" : 200 }] 
# 通过 age 升序排序
print ("列表通过 age 升序排序: ")
print (sorted(lis, key = lambda i: i['age']) )
print ("\r") 
# 先按 age 排序，再按 name 排序
print ("列表通过 age 和 name 排序: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])) )
print ("\r") 
# 按 age 降序排序
print ("列表通过 age 降序排序: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True) )




# ----------------------------------------列表list-----------------------------------
# 数组：存储同一种数据类型的集合 scores=[1,2,3,4]  一个变量存储多个信息  python中没有数组的概念
# 列表：（打了激素的数组）：可以存储任意数据类型的集合
#列表里：可以存储不同的数据类型
列表还支持拼接操作：
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表函数&方法
len(list)
# 列表元素个数
max(list)
# 返回列表元素最大值
min(list)
# 返回列表元素最小值
list(seq)
# 将元组转换为列表
# 方法
list.append(obj)
# 在列表末尾添加新的对象
list.count(obj)
# 统计某个元素在列表中出现的次数
list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)
# 将对象插入列表
list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)
# 移除列表中某个值的第一个匹配项
list.reverse()
# 反向列表中元素
list.sort( key=None, reverse=False)
# 对原列表进行排序
list.clear()
# 清空列表
list.copy()
# 复制列表

# -----------------------------------元组-----------------------------------
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 创建空元组
# tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
# 您可以通过引用方括号内的索引号来访问元组项目：
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# 更改元组值
# 创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。

# 检查项目是否存在
# 要确定元组中是否存在指定的项，请使用 in 关键字：
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# 元组长度
# 要确定元组有多少项，请使用 len() 方法：
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# 合并两个元组
# 如需连接两个或多个元组，您可以使用 + 运算符：
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple() 构造函数
# 也可以使用 tuple() 构造函数来创建元组。
thistuple = tuple(("apple", "banana", "cherry")) # 请注意双括号
print(thistuple)

# ---------------------------------------集合-----------------------------------------
# 集合（Set）
# 集合是无序和无索引的集合。在 Python 中，集合用花括号编写。
# 创建集合：
thisset = {"apple", "banana", "cherry"}
print(thisset)
# 注释：集合是无序的，因此您无法确定项目的显示顺序。

# -----python集合的运算-----
# 在对集合做运算时，不会影响原来的集合，而是返回一个运算结果
# 创建两个集合
s = {1,2,3,4,5}
s2 = {3,4,5,6,7}

# & 交集运算
result = s & s2 # {3, 4, 5}

# | 并集运算
result = s | s2 # {1,2,3,4,5,6,7}

# - 差集
result = s - s2 # {1, 2}

# ^ 异或集 获取只在一个集合中出现的元素
result = s ^ s2 # {1, 2, 6, 7}

# <= 检查一个集合是否是另一个集合的子集
# 如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合是a集合超集
a = {1,2,3}
b = {1,2,3,4,5}

result = a <= b # True
result = {1,2,3} <= {1,2,3} # True
result = {1,2,3,4,5} <= {1,2,3} # False

# < 检查一个集合是否是另一个集合的真子集
# 如果超集b中含有子集a中所有元素，并且b中还有a中没有的元素，则b就是a的真超集，a是b的真子集
result = {1,2,3} < {1,2,3} # False
result = {1,2,3} < {1,2,3,4,5} # True

# >= 检查一个集合是否是另一个的超集
# > 检查一个集合是否是另一个的真超集
print('result =',result)



# 访问项目
# 您无法通过引用索引来访问 set 中的项目，因为 set 是无序的，项目没有索引。
# 但是您可以使用 for 循环遍历 set 项目，或者使用 in 关键字查询集合中是否存在指定值。
# 遍历集合，并打印值：
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# 实例
# 检查 set 中是否存在 “banana”：
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# 更改项目
# 集合一旦创建，您就无法更改项目，但是您可以添加新项目。

# 添加项目
# 要将一个项添加到集合，请使用 add() 方法。
# 要向集合中添加多个项目，请使用 update() 方法。

# 实例
# 使用 add() 方法向 set 添加项目：
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# 实例
# 使用 update() 方法将多个项添加到集合中：
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# 获取 Set 的长度
# 要确定集合中有多少项，请使用 len() 方法。

# 删除项目
# 要删除集合中的项目，请使用 remove() 或 discard() 方法。

# 实例
# 使用 remove() 方法来删除 “banana”：
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# 注释：如果要删除的项目不存在，则 remove() 将引发错误。

# 实例
# 使用 discard() 方法来删除 “banana”：
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# 注释：如果要删除的项目不存在，则 discard() 将引发错误。
# 您还可以使用 pop() 方法删除项目，但此方法将删除最后一项。请记住，set 是无序的，因此您不会知道被删除的是什么项目。
# pop() 方法的返回值是被删除的项目。

# 实例
# 使用 pop() 方法删除最后一项：
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# 注释：集合是无序的，因此在使用 pop() 方法时，您不会知道删除的是哪个项目。

# 实例
# clear() 方法清空集合：
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# 实例
# del 彻底删除集合：
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# 合并两个集合
# 在 Python 中，有几种方法可以连接两个或多个集合。
# 您可以使用 union() 方法返回包含两个集合中所有项目的新集合，也可以使用 update() 方法将一个集合中的所有项目插入另一个集合中：

# 实例
# union() 方法返回一个新集合，其中包含两个集合中的所有项目：
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# 实例
# update() 方法将 set2 中的项目插入 set1 中：
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# 注释：union() 和 update() 都将排除任何重复项。
# 还有其他方法将两个集合连接起来，并且仅保留重复项，或者永远不保留重复项，请查看此页面底部的集合方法完整列表。
# set() 构造函数
# 也可以使用 set() 构造函数来创建集合。

# 实例
# 使用 set() 构造函数来创建集合：
thisset = set(("apple", "banana", "cherry")) # 请留意这个双括号
print(thisset)

# 可迭代对象转换成集合
set 语法：
class set([iterable])
# 参数说明：
# iterable -- 可迭代对象对象；
# 返回值：
# 返回新的集合对象。
将列表转为集合：

list1=[1,3,4,3,2,1]
list1=set(list1)
print(list1)
# 结果如下：
（1，2,3,4）

difference()	返回包含两个或更多集合之间差异的集合。
difference_update()	删除此集合中也包含在另一个指定集合中的项目。
discard()	删除指定项目。
intersection()	返回为两个其他集合的交集的集合。
intersection_update()	删除此集合中不存在于其他指定集合中的项目。
isdisjoint()	返回两个集合是否有交集。
issubset()	返回另一个集合是否包含此集合。
issuperset()	返回此集合是否包含另一个集合。
pop()	从集合中删除一个元素。
remove()	删除指定元素。
symmetric_difference()	返回具有两组集合的对称差集的集合。
symmetric_difference_update()	插入此集合和另一个集合的对称差集。
union()	返回包含集合并集的集合。
update()	用此集合和其他集合的并集来更新集合。







