# 一次赋值多个变量
# 在 Python 代码的编写中，可以一次给多个变量赋值，例如：

x = y = z = 10086
# 该代码表示给x,y,z同时赋值了数字10086，也可以给 x,y,z 分别赋值，代码如下：

x,y,z = 1,2,3
# 注意，左侧变量数量和右侧值的数量要保持一致。



# 2.1.4 扩展几个数值数据类型常用的函数
# 虽然学的不多，你现在应该注意到一个词 – 函数出现的频率在 Python 中极高，这也是为什么很多其他语言的使用者，会把 Python 藐视成一堆函数凑成的语言了，哼~浅薄者。

# 数值数据类型常用的函数，这里简单举几个例子，后面还会详细学习。

# abs() 计算绝对值
# pow() 次方运算
# round() 四舍五入
# max() 取最大值
# min() 去最小值
# 参考代码如下，临摹 2 遍知道是在干啥就行，下面的代码涉及了函数中参数的概念，不做过多的解释。

# abs() 计算绝对值
a = -1
print(abs(a))
# pow() 次方运算
x = 2
c = 3
print(pow(x,c))
# round() 四舍五入

d = 34.6
print(round(d))
# max()  取最大值
print(max(1,2,3))
# min() 去最小值
print(max(9,10,6))


# 字符串快速复制
# Python 中有一个独特的小技巧，可以快速复制字符串，使用的是数学符号 *，例如下述代码，将快速复制一堆 # 号。
print("#"*100)

# 内置函数 help 该函数可以查看其它函数的使用文档。比如使用 print 测试：
help(print)
# 输出如下：
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

# 这其中就包含了 print 函数的完整说明，最重要的部分如下：
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# 其中：
# value 表示要输出的数据，可以多个，用逗号 , 分隔
# sep 输出多个数据时，分隔符号，默认是空格
# end 输出一行末尾输出的符号
# file 输出位置，默认输出控制台，就是黑窗口中，可以设置到具体文件
# flush 是否清除数据流缓冲区，默认为 False（该内容先不做涉及）
# 以上这些其实准确的说法是函数参数。


列表
# 索引除了为正数以外，还可以为负数，获取列表的最后一个元素的索引是 -1，代码如下：

nums = [1,2,3,4,5,6]
print("列表最后一个元素为：",nums[-1])
# 依据顺序，-1 表示最后一个元素，-2 表示倒数第 2 项…

4.1.3 列表切片
# 读取从索引 m 到 n-1 的列表元素
my_list[m:n]
# 读取列表的前 n 项元素
my_list[:n]
# 读取列表从 m 开始到结尾的元素
my_list[m:]
# 间隔 s，读取从 m 到 n 的列表元素
my_list[m:n:s]
# 以上内容反映到代码中呈现如下，该部分呈现到代码中如下，尤其注意 m 与 n 的取值。
my_list = ["a","b","c","d","e","f"]

# 输出 ['a', 'b', 'c'] 注意 a,b,c 的索引分别是 0,1,2
print(my_list[0:3])
# 输出 ['b', 'c', 'd', 'e'] 注意 b,c,d,e 的下标分别是 1,2,3,4
print(my_list[1:5])
# 输出 ['b', 'c', 'd', 'e', 'f']
print(my_list[1:])
# 输出 ['a', 'b', 'c', 'd', 'e']
print(my_list[:5])
# 输出 ['b', 'd']  从索引 1 到索引 3，间隔 1 个索引取
print(my_list[1:4:2])

# 4.1.4 列表相关内置函数
# 在 Python 中与列表相关的内置函数常见的有 4 个，分别是获取最大值 max、最小值 min、求和 sum 以及获取列表元素个数 len。
# 最大值与最小值
# 使用 max 与 min 函数可以直接获取列表中的最大值与最小值，该函数使用有些注意事项需要了解下，具体还是参照代码：
my_list1 = ["a","b","c","d","e","f"]
my_list2 = [1,2,3,4,5,6]
my_list3 = ["a",1,2,3,4]

# 输出 f
print(max(my_list1))
# 输出 6
print(max(my_list2))
# 报错
print(max(my_list3))
# 上述代码在运行时发现，前面 2 个列表可以输出最大值，但是第三个直接报错，这是因为 max 与 min 只能用于元素全是数字或者全是字符串的列表，
# 如果列表中有其他数据类型或者数字与字符串混合就会报错。
# min 用法和 max 完全一致

# 4.1.5 列表元素的修改与删除
my_list1 = ["a","b","c","d","e","f"]

# 通过索引删除某一元素
del my_list1[0]
print(my_list1)

my_list1 = ["a","b","c","d","e","f"]
# 通过索引删除列表区间元素
del my_list1[0:3]
print(my_list1)

my_list1 = ["a","b","c","d","e","f"]
# 通过索引删除列表区间元素
del my_list1[0:3:2]
print(my_list1)

# 4.1.6 列表相加，相乘，删除
# 在 Python 中可以直接对列表进行相加与相乘操作，列表与列表之间的相加可以理解为列表的连接，代码如下：
my_list1 = ["a","b"]
my_list2 = ["c"]
my_list3 = my_list1 + my_list2
print(my_list3)
# 任意多个列表直接如果用 “+” 进行操作，那么这些列表将会连接起来形成一个新的大列表。

# 列表可以与一个数字进行乘法计算，表示重复前面的列表多次，例如下述代码：
my_list1 = ["a","b"]
my_list2 = ["c"]
my_list3 = my_list1 * 4
# 输出结果为 ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
print(my_list3)
# 上述代码用 [a,b] * 4 得到结果为列表 [a,b] 重复出现了 4 次。


# 4.2 初识 Python 面向对象
# 字符串对象的方法
lower 将字符串转换成小写
upper 将字符串转换成大写
title 将字符串首字母大写，其余小写
rstrip 移除字符串右侧空白
lstrip 移除字符串左侧空白
strip 移除字符串两侧空白
#  快速获取系统内置方法
在实际开发中，我们很难记住一个对象的所有方法，对于橡皮擦来说编写代码的时候也要借助于手册，方法太多不可能记住的，常用的记住就好了，那如何查询一个对象的所有方法呢，用到的是一个内置函数 dir。
例如，你想知道一个字符串对象的所有方法，可以编写如下代码。
my_str = "good moring"
print(dir(my_str))
代码运行之后，会得到如下内容，其中红框内容就是刚才提及到的方法。
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
   'title', 'translate', 'upper', 'zfill']
# 对于某个方法是如何使用的，可以调用之前学习的 help 内置函数进行学习，语法格式如下：
# help(对象.方法)
# 例如获取字符串对象的 rfind 方法。
my_str = "good moring"
print(help(my_str.rfind))
# 结果如下，稍微阅读一下即可了解 rfind 方法的使用方式。
# rfind(...) method of builtins.str instance
#     S.rfind(sub[, start[, end]]) -> int
    
#     Return the highest index in S where substring sub is found,
#     such that sub is contained within S[start:end].  Optional
#     arguments start and end are interpreted as in slice notation.
    
#     Return -1 on failure.

# None

# 4.3 通过方法增删列表元素
4.3.2 列表插入元素
append 方法是在列表末尾固定插入元素，如何在任意位置插入元素是一个新的方法，名称叫做 insert，语法格式如下：
my_list.insert(索引位置,"新增元素")
尝试在索引 1，索引 2，索引 0 的位置插入元素，代码如下：
my_list = ["pear", "apple", "orange"]
my_list.insert(0, "插入")
print(my_list)
my_list = ["pear", "apple", "orange"]
my_list.insert(2, "插入")
print(my_list)
# 这里需要注意下当索引超过列表长度时，默认插入末尾。

# 4.3.3 删除列表元素
# 之前的内容中已经介绍过一种删除列表元素的方式，通过关键字 del，
# 该方式存在一个问题就是删除元素之后没有获取到被删除的元素。接下来的方法将解决该问题，你将能获取到被删除的值，该方法是 pop ，语法格式如下：
item = my_list.pop()
item = my_list.pop(索引)
# 注意在 pop 方法中可以携带一个索引值，直接删除索引位置的元素，如果没有默认删除最后一项。变量 item 用于获取被删除的值。注意该方法删除元素的时候，索引不能超过列表长度。
my_list = ["pear", "apple", "orange"]
item = my_list.pop()
print(item)
print("删除元素之后")
print(my_list)
# 代码运行结果为：
orange
删除元素之后
['pear', 'apple']
# pop 方法是按照索引删除元素，你还可以直接删除指定元素，具体方法是 remove，该方法的语法格式如下。
my_list.remove(待删除元素内容)
# 注意 remove 删除元素之后，不会返回被删除的元素，还存在一个问题是如果待删除的元素不在列表中，会提示代码错误。
# 如果待删除的元素在列表中出现多个，默认只删除第一个，如果想要删除多个，需要用到后面的循环知识。

# 4.4.1 sort 排序
# sort 方法可以对列表元素进行排序，默认从小到大，当然也可以修改成从大到小，该方法一般用于纯数字或者纯英文字符列表排序，
# 如果列表中的元素数据类型比较复杂，该方式不在适用，需要注意一下。

# sort 方法的语法格式如下：
my_list.sort()
# 声明一个所有元素都是数字的列表，然后进行排序。
my_list = [3, 4, 1, 2, 9, 8, 7]
print("排序前：", my_list)
my_list.sort()
print("排序后：", my_list)
# 输出结果如下：
排序前： [3, 4, 1, 2, 9, 8, 7]
排序后： [1, 2, 3, 4, 7, 8, 9]
# 如果希望按照从大到下进行排序，只需要增加参数（参数概念后面还会继续学习）reverse=True 即可。
my_list = [3, 4, 1, 2, 9, 8, 7]
print("排序前：", my_list)
my_list.sort(reverse=True)
print("排序后：", my_list)
# 英文字符串的排序结果希望你可以进行一下测试，需要注意对英文字符列表进行排序，建议将字符串英文全部修改为小写。
# 注意上述 sort 方法排序之后是对原列表中元素顺序修改，即修改的是 my_list 列表的顺序，如果不想修改原列表的顺序，想要新生成一个列表，需要用到的是下述方法。

# 4.4.2 sorted 排序
# sort 排序将造成列表元素顺序永久修改，很多时候并不需要修改原列表，这种情况下需要借助 sorted 函数，
# 注意 sorted 是一个内置函数，并不是列表对象的一个方法，也就是说 sorted 可以用于很多对象的排序。
# sorted 函数的语法格式如下：
sorted(待排序列表) # 正序，从小到大
sorted(待排序列表,reverse=True) # 逆序，从大到小
# 该函数使用之后会返回一个新的列表，你可以用新变量接收一下，具体代码如下：
my_list = [3, 4, 1, 2, 9, 8, 7]
print("排序前：", my_list)
new_list = sorted(my_list)
print("排序后：", my_list)
print("排序后：", new_list)
# 注意排序后新变量为 new_list 对于原 my_list 列表中元素的顺序并无影响。

# 4.5.1 列表检索元素索引
# 通过 index 方法可以获取某内容在列表中第一次出现的索引值，格式如下：
索引值 = my_list.index(待查找值)
# 该方法注意如果没有检索到索引值，会提示错误。
my_list = [3, 4, 1, 2, 9, 8, 7]
ke = my_list.index(4)
ke = my_list.index(10)
print(ke)

# 4.5.2 列表统计元素出现次数
# 通过 count 方法可以获取列表特定元素出现的次数，它的语法格式如下：
次数 = my_list.count(待查找值)
# 该方法同样当在列表中找不到待查找值时会返回 0。
my_list = [3, 4, 3, 2, 3, 8, 7]
nums = my_list.count(3)
print(nums)

# 4.5.3 列表转换为字符串
# 通过 join 方法可以将列表中的所有元素组合成一个字符串，语法格式如下：
# 连接字符串.join(待转换列表)
# 该方法其实准确的说应该是 字符串对象的一个方法。
my_list = ["pear", "apple", "orange"]
my_str = "#".join(my_list)
print(my_str)
# 该方法在使用的时候需要注意，列表中所有元素都必须是字符串，否则会出现 expected str instance, int found 错误。

# 4.5.4 列表追加列表
# append 方法可以给列表追加元素，extend 可以给一个列表追加一个列表，相当于将两个列表进行连接。

列表1.extend(列表2)
# 注意追加的列表默认在原列表末尾追加，所以追加之后原列表中的元素已经发生了改变。
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list1.extend(my_list2)
print(my_list1)


# 5.3.4 for … else 循环
for i in range(0,5):
    if i > 3 :
        continue

    print("当前数字为：",i)
else:
    print("不管上面的 for 循环干了啥，我都要执行一次")



# 6.5 内置函数 zip
# 函数 zip 可以将一个可迭代对象，如列表打包成元组，打包之后返回的是一个 zip 对象，说起来有点绕，而且应用的场景不是很明确，可以先看代码学习一下。

en_names = ["apple", "orange", "pear"]
cn_names = ["苹果", "橘子", "梨"]

zipData = zip(en_names, cn_names)

print(zipData)  # 打印 zipData
print(type(zipData))  # 打印 zipData 数据类型
print(list(zipData))  # 输出 zipData 中的数据内容
# 输出结果：
<zip object at 0x0000024C1E4FF648>
<class 'zip'>
[('apple', '苹果'), ('orange', '橘子'), ('pear', '梨')]
# 通过代码你可以看到，zip 把两个列表的数据合并了，每个列表中对应索引位置的元素合并在了一个元组里面。上述代码中就出现了 apple 与 苹果 对应，orange 与 橘子 对应，pear 与 梨 对应。
# 如果放在 zip 函数的列表参数长度不相同，那 zip 会选择元素最少的那个列表作为依据，形成对应关系。

en_names = ["apple", "orange"]
cn_names = ["苹果", "橘子", "梨"]

zipData = zip(en_names, cn_names)

print(zipData)  # 打印 zipData
print(type(zipData))  # 打印 zipData 数据类型
print(list(zipData))  # 输出 zipData 中的数据内容
# 该代码第一个列表有 2 个元素，第二个列表有 3 个元素，最终输出的结果为：

<zip object at 0x0000026DE2F7F608>
<class 'zip'>
[('apple', '苹果'), ('orange', '橘子')]
# 如果在 zip 中的参数前面增加 * 符号，相当于解压，返回二维矩阵式。

# 代码如下：
en_names = ["apple", "orange"]
cn_names = ["苹果", "橘子", "梨"]

zipData = zip(en_names, cn_names)

print(zipData)  # 打印 zipData
unzipData = zip(*zipData)
print(unzipData)  # 打印 unzipData
print(list(unzipData))  # 打印 unzipData 内容


# 7.1.3 字典中增加元素、修改元素、删除元素
# 删除元素
# 如果想要删除字典中某一个具体的元素，只需要通过 del 关键字加上 my_dict[待删除元素的键] 即可完成。
my_dict = {"red": "红色", "green": "绿色", "blue": "蓝色"}
del my_dict["red"]
print(my_dict)

# 以上内容可以删除特定元素，使用字典的一个 clear 方法，可以将字典清空。
my_dict = {"red": "红色", "green": "绿色", "blue": "蓝色"}
my_dict.clear()
print(my_dict)
# 以上内容会输出 {} 该符号表示空字典。

# 除了将字典清空以外，还可以直接将字典变量删除。
my_dict = {"red": "红色", "green": "绿色", "blue": "蓝色"}
del my_dict
print(my_dict)
# 删除字典变量之后，在打印 my_dict 程序直接报错，提示 name 'my_dict' is not defined 变量未定义，
# 在删除字典的时候一定要注意别误删整个字典，除非程序要求这么实现。

# 获取字典元素数量
# 列表与元组都可以使用 len 来获取元素数量，同样的方法适用于字典，语法格式如下：
my_dict_length = len(my_dict)
# 空字典的元素数量为 0，可以进行尝试一下。
# 获取字典元素数量
# 列表与元组都可以使用 len 来获取元素数量，同样的方法适用于字典，语法格式如下：

my_dict_length = len(my_dict)
# 空字典的元素数量为 0，可以进行尝试一下。
# 调用字典的 items 方法可以获取字典的所有键值，例如下述代码：

my_dict = {"red": "红色",
           "green": "绿色",
           "blue": "蓝色"}

print(my_dict.items())
# 该内容输入为：

dict_items([('red', '红色'), ('green', '绿色'), ('blue', '蓝色')])
# 接下来循环输出字典内容，有几种不同的写法，先尝试编写如下代码，在进行知识点学习。

my_dict = {"red": "红色",
           "green": "绿色",
           "blue": "蓝色"}
# 直接对 my_dict 进行遍历
for item in my_dict:
    print(item)

# 遍历 my_dict 的 items 方法
for item in my_dict.items():
    print(item)

# 遍历 my_dict 的 items 方法，并用 key 与 value 接收
for key,value in my_dict.items():
    print("键:{}，值:{}".format(key,value))
# 以上三种输出内容请自行查阅。

# 第一种输出的是所有的键；
red
green
blue
# 第二种将每个键值对当做一个元组输出；
('red', '红色')
('green', '绿色')
('blue', '蓝色')
# 第三种通过变量与元组之间的赋值直接将键与值输出。
键:red，值:红色
键:green，值:绿色
键:blue，值:蓝色

# 关于变量与元组之间的赋值可以参考下属代码：
a,b = (1,2)
print(a)
print(b)
# 输出
1
2
# 注意通过该方式进行变量的赋值一定要将左侧的变量与右侧元组中的元素做好对应，一个变量对应元组中的一项，顺序也对应。
# 如果不对应就会出现下述错误 ValueError: too many values to unpack 。


# 7.2.2 遍历字典的键
# 上文学习到的是遍历字典的键值，你可以直接通过 keys 方法获取字典的所有键，例如下述代码：
my_dict = {"red": "红色",
           "green": "绿色",
           "blue": "蓝色"}
for key in my_dict.keys():
    print(key)
# 7.2.3 遍历字典的值
# 有 keys 方法获取键，对应的就是通过 values 获取所有值。

# 7.4 字典的方法
# 字典有一些特殊的方法需要单独说明一下，如果想要查看字典所有的方法，依据使用 dir 内置函数调用。

# 7.4.1 fromkeys 方法
# 该方法目的是创建一个字典，语法格式如下：

# 注意该方法直接通过 dict 调用
# seq 是一个序列，可以为元组，也可以是字典
my_dict = dict.fromkeys(seq)
# 接下来就通过该方法实际创建一个字典。

my_list = ['red', 'green']
my_dict = dict.fromkeys(my_list)
# 以下内容输出 {'red': None, 'green': None}
print(my_dict)
my_dict1 = dict.fromkeys(my_list, "字典的值")
print(my_dict1)
# 第一种方式发现输出的字典中所有值为 None（Python 中的特殊值，相当于空），该内容是由于没有设置字典默认值，缺省为 None，
# 如果需要在定义字典的时候初始化该值，在方法中的第二个参数赋值即可。

# 7.4.4 pop 方法
# 该方法用于删除字典元素，语法格式如下：
ret_value = dict.pop(key[,default])
# 既然已经写出了这种标准格式，那先补充一下语法格式的规范，例如 dict.pop(key[,default]) 中 key 表示必填参数，[] 包括的参数为非必填参数，这样你可以理解上述语法格式内容是什么了。

my_dict = {"red": "红色",
           "green": "绿色",
           "blue": "蓝色"}

# 删除指定项
ret_value = my_dict.pop('red')
# 输出被删除的红色
print(ret_value)
# 查看字典 {'green': '绿色', 'blue': '蓝色'}
print(my_dict )
# 在使用 pop 方法的时候如果找到 key，就会删除该键值对，如果找不到 key 会返回 defalut 设置的值，如果该值没有设置，会报错。

my_dict = {"red": "红色",
           "green": "绿色",
           "blue": "蓝色"}

# 删除指定项，如果没有设置找不到返回的值，直接报错
ret_value = my_dict.pop('red2')

# 删除指定项，找不到 key1 返回后面设置的值
ret_value = my_dict.pop('red1',"找不到返回的值")


# 八、Python 中一个无序且元素唯一的数据类型，它是集合。
# 8.1 集合是啥
# 集合是一个数据类型，它其中的每个元素的顺序不固定，但唯一。多么绕的一句话，回味，一定要好好回味。
集合中的元素内容必须是不可变类型，例如整数、浮点数、字符串、元组等内容，可变的列表、字典、集合不可以。
集合中的元素内容必须是不可变类型，例如整数、浮点数、字符串、元组等内容，可变的列表、字典、集合不可以。
集合中的元素内容必须是不可变类型，例如整数、浮点数、字符串、元组等内容，可变的列表、字典、集合不可以。
# 集合本身是可变的，跟列表一样可以增删元素。
# 8.1.1 集合的声明
# 截止到现在，小括号用来声明元组，中括号用来声明列表，大括号用来声明字典，那集合怎么办？Python 中也是用大括号来声明集合。当然你也可以通过 set 函数建立集合。
# 集合定义的语法格式如下：

my_set = {元素1,元素2,...}
# 简单的代码示例如下：
my_set = {1, 2, 3, 3, 10, 4, 5, 6}
print(my_set)
# 数据输出之后，会发现重复的整数 3 只剩下一个了。还是因为集合的元素是唯一的，出现重复多的部分将会舍去。
# 如果在集合中使用了可变类型作为元素，会报错。
my_set = {1, 2, 3, [3, 10, 4, 5, 6]}
# 错误提示：TypeError: unhashable type: 'list'
print(my_set)
# 这里需要注意下，空集合的声明不能使用 {}，只用一个大括号表示的是空字典。声明一个空集合需要用到 set 函数。

# 8.1.2 set 函数定义集合
# 使用 set 函数可以定义集合，并且可以定义空集合。set 函数参数可以为字符串、列表、元组。
# 通过 set 定义空集合

my_dict = {}
my_set = set()
# 空字典
print(type(my_dict))
# 空集合
print(type(my_set))
# set 将字符串转换成集合
# set 函数类似一个强制转换，可以将其它类型的转换成集合。

my_set = set("my name is xiangpica")
print(my_set)
# 该内容会过滤重复字母，并且输出的顺序不定，因为集合是无序的。
# 集合可以对元组去重
# 借助集合元素的不允许重复，可以实现一些特定的效果，例如去重。

my_tuple = ("apple", "orange", "orange", "pear", "banana", "food")
my_set = set(my_tuple)
print(my_set)

# 8.2 集合的操作
# 在学集合相关操作前，需要在学习一些符号。

符号	含义
&	交集
|	并集
-	差集
^	对称差集
# 接下来的内容就非常类似高中线代里面的概念了，求集合的交并差集。

# 8.2.1 交集（intersection）
# 交集就是求两个集合共有的元素。
my_set1 = {"apple", "orange", "pear", "banana", "food"}
my_set2 = {"apple", "orange", "pear"}
both = my_set1 & my_set2
print(both)
# 输出
{'apple', 'orange', 'pear'}
# 除了通过 & 符号以外，还可以通过集合的 intersection 方法完成。
my_set1 = {"apple", "orange", "pear", "banana", "food"}
my_set2 = {"apple", "orange", "pear"}
both = my_set1.intersection(my_set2)
print(both)
# 输出
{'orange', 'apple', 'pear'}

# 8.2.2 并集（union）
# 并集就是取所有集合的所有元素，如果出现重复的保留一个。使用符号 | 或者 union 方法完成。
my_set1 = {"apple", "orange", "pear", "banana", "food"}
my_set2 = {"apple", "orange", "pear"}
both = my_set1 | my_set2
print(both)
# 输出
{'food', 'orange', 'apple', 'banana', 'pear'}
# 使用 union 完成。
my_set1 = {"apple", "orange", "pear", "banana", "food"}
my_set2 = {"apple", "orange", "pear"}
both = my_set1.union(my_set2)
print(both)
# 输出
{'food', 'orange', 'apple', 'banana', 'pear'}

# 8.2.3 差集（difference）
# 对于求集合的差集与交并集不同，有个先后顺序问题，例如属于 A 但不属于 B 表示为 A-B，同理属于 B 但不属于 A，表示为 B-A。
# 差集的符号是 -，可以使用 difference 方法进行运算。
my_set1 = {"apple", "orange", "pear", "banana", "food"}
my_set2 = {"apple", "orange", "pear", "grape"}
# 求解属于 A，但不属于 B 的元素
dif1 = my_set1 - my_set2
print(dif1)
# 输出
{'banana', 'food'}
# 求解属于 B，但不属于 A 的元素
dif2 = my_set2 - my_set1
print(dif2)
# 输出
{'grape'}
# 接下来如何使用 difference 方法去求差集就交给你自己完成啦。

# 8.2.4 对称差集（symmetric difference）
# A 与 B 两个集合，如果想要获得属于 A 或者 B 集合的元素，但又不要属于 A 且属于 B 的元素，这时就是对称差集的应用场景了。
# 对称差集的符号是 ^，方法名是 symmetric_difference。
my_set1 = {"apple", "orange", "pear", "banana", "food"}
my_set2 = {"apple", "orange", "pear", "grape"}
dif = my_set1 ^ my_set2
print(dif)
# 输出
{'banana', 'grape', 'food'}
# 上述代码就会输出既不属于 A 也不属于 B 的元素，即对称差集。


# 8.3 集合的方法
# 8.3.1 集合的增删
# add 方法可以在集合中增加元素，语法格式如下：
my_set.add(新增元素)
# 第一个需要注意的新的元素如果已经存在集合中，不会新增进去，第二个需要注意的是集合是无序的，新增加元素的位置将不确定。
my_set = {"apple", "orange", "pear", "grape"}
my_set.add("new")
my_set.add("new")
print(my_set)
# remove 方法可以删除集合中元素，前提是该元素在集合中，如果删除不存在的元素报错。
my_set = {"apple", "orange", "pear", "grape"}
my_set.remove("apple")
print(my_set)
# 第二次删除报错 因为 apple 已经不在集合中
my_set.remove("apple")
print(my_set)
# discard 方法可以删除集合元素，如果元素不存在不会报错。
my_set = {"apple", "orange", "pear", "grape"}
my_set.discard("apple")
print(my_set)
my_set.discard("apple")
print(my_set)
# pop 方法为随机删除一个元素，被删除的元素会被返回，即可以用一个变量接收被删除的元素，如果集合为空使用 pop 会报错。
my_set1 = {"apple", "orange", "pear", "grape"}
# pop 方法随机删除一个元素，将被删除的元素返回
var = my_set1.pop()
print(var)
# 空集合使用 pop 方法报错
my_set2 = set()
var = my_set2.pop()
print(var)
# clear 方法删除集合内的所有元素
my_set1 = {"apple", "orange", "pear", "grape"}
my_set1.clear()
print(my_set1)

# 8.3.1 集合的其它方法
# isdisjoint 方法用于判断两个集合是否存在相同元素，没有返回 True，否则返回 False。
my_set1 = {"apple", "orange", "pear", "grape"}
my_set2 = {"banana", "watermelon"}
# 两个集合没有相同元素
ret_bool = my_set1.isdisjoint(my_set2)
print(ret_bool) # 返回 True
my_set1 = {"apple", "orange", "pear", "grape"}
my_set2 = {"banana", "watermelon","apple"}
# 两个集合有相同元素
ret_bool = my_set1.isdisjoint(my_set2)
print(ret_bool)
# issubset 该方法用于判断一个集合是否是另一个集合的子集，确定是返回 True，否则返回 False。
my_set1 = {"apple", "orange", "pear", "grape"}
my_set2 = {"banana", "watermelon"}
# 第二个集合不是第一个集合的子集
ret_bool = my_set2.issubset(my_set1)
print(ret_bool) # 返回 False
# 第二个集合是第一个集合的子集
my_set1 = {"apple", "orange", "pear", "grape"}
my_set2 = {"orange","apple"}
ret_bool = my_set2.issubset(my_set1)
print(ret_bool) # 返回 True
# 注意判断 A 是 B 的子集，格式是 A.issubset(B)，顺序别搞错。
# issuperset 方法用于判断一个集合是否是另一个集合的父集，与 issubset 恰好相反，具体实现由大家自行完成。
# update 方法用于将一个集合的元素添加到另一个集合内，语法格式如下：
# 被添加的集合A.update(待添加的集合B)
# 该方法谁在前就是给谁添加。
my_set1 = {"apple", "orange", "pear", "grape"}
my_set2 = {"banana", "watermelon"}
my_set1.update(my_set2)
print(my_set1)
# 其它一些方法，本轮滚雪球阶段只做了解。
# intersection_update 此方法用于求多个集合的交集
# difference_update 删除集合内与另一集合重复的元素
# symmetric_difference_update 类似对称差集的用法

# 8.4 集合可用的内置函数
# 8.4.1 max、min、sum
# 以上内置函数作用域集合与列表使用规则一致，自行测试即可。

# 8.4.2 len
# 获取集合元素的数量。

# 8.4.3 sorted
# 使用该函数可以对集合进行排序。

# 8.5 冻结集合 frozenset
# 集合中的元素可以添加与删除，与列表可以对应。
# 还存在一种不可进行添加与删除元素的集合，叫做冻结集合，与元组可以对应学习。



# 九、Python 中函数是基础部分第一道难关
# 9.3.3 关键词参数（参数名称=值）
# 该参数使用的方式是在调用函数时，参数用 参数名称=值 这种形式传递。其实在上述传递一个和多个参数的时候，也可以应用该方式传递参数，例如修改代码如下。
# 声明一个带一个参数的函数
def show(name):
    print("传递进来的姓名是：", name)
show(name="橡皮擦")
# 声明一个带多参数的函数
def show1(name, age):
    print("传递进来的姓名是：", name, " 年龄是：", age)
show1(name="橡皮擦", age=20)
# 用这种形式调用函数，参数的位置就不在重要了，因为已经指定参数具体值是多少。

# 9.3.4 参数默认值
# 在定义函数的时候可以给参数一个默认值，如果调用该函数没有给该参数赋值，程序会使用默认值而不会报错。
# 没有默认值的参数
def show(name):
    print("传递进来的姓名是：", name)
show() # 该函数调用时会报错
# 有默认值的参数
def show(name="橡皮擦"):
    print("传递进来的姓名是：", name)
show() # 该函数调用没有问题，即使没有传递参数会使用默认值
# 如果一个参数有默认值，注意该参数必须放在函数参数位置的最右侧，例如下述函数定义。
def show(a,b,c,name="橡皮擦"):
	pass


# 9.4.3 返回多个值
# 使用 return 返回函数数据，可以一次性返回多个值，返回的数据之间用逗号分隔即可。
# 定义一个减法函数
def sub(a, b):
    c = a - b
    d = a + b
    f = a / b
    return c, d, f

# 参数为 2 和 1，将结果进行返回
ret = sub(2, 1)
print(ret)
# 返回的结果是一个元组 (1, 3, 2.0)。


# 9.5 调用函数时参数是列表
# 为什么单独将其参数是列表时拿出来讲解，是因为列表这个有点特殊，里面还会引出全局变量与局部变量的一个概念，放心第一遍学习 100%迷糊。
# 如果你有其他编程语言的功底，那另当别论。
# 具体代码如下，注意看出现的问题。
names = ["aaa","bbb","ccc"]
def change_list(one_names):
    # 修改传递进来的列表索引 0 的位置上为 jjj
    one_names[0] = "jjj"
# 函数调用，同时将 name 作为参数传递进函数内部
change_list(names)
print(names)
# 最终的输出结果是 ['jjj', 'bbb', 'ccc']，这个表示啥？表示函数外面的 names 被函数给修改了。疑问是所有在函数外面的变量传递到参数内部都会被修改吗？换个整数试试。
score = 1
def change_list(one_score):
    one_score = 333
# 函数调用，同时将 score 作为参数传递进函数内部
change_list(score)
print(score)
# 此时 score 虽然在函数内部被修改为了 333，但是在函数外打印并没有被修改，还是 1。现在问题就出现了，Python 并不是一视同仁的，
# 列表变量在函数内被修改影响到了外部变量，而整型变量并没有受到影响。


# 9.7 传递任意数量的参数
# 9.7.1 一般参数与任意参数的组合
# 在 Python 编写代码的过程中，很容易出现一种情况是你不知道有多少个参数，这时函数定义时参数就不好设定了，好在 Python 已经想到了这个情况。

def show(*keys):
    print("传入的参数可以循环打印")
    for key in keys:
        print(key)

show(1,2,3,4,5,6,7)
# 在函数定义的时候，参数位置使用 *参数名，然后在函数体重的代码块位置就可以进行循环打印了，可以捕获到任意数量的参数。
# 如果又有一般参数，又有不定数量的参数怎么办？好办，使用下面的格式。

def show(name,age,*keys):
    print("传入的参数可以循环打印")
    print(name)
    print(age)
    for key in keys:
        print(key)

show("www",18,1,2,3)
# 希望你现在发现规律，函数调用的时候先依次去匹配函数定义的参数，一一对应，都对应完毕，发现没有一般参数了，剩下的都打包给 *keys 就好了。
# 还要不要写两个带 * 的参数，例如 def show(name,*keys,*keys1) ，这样就报错了。

# 9.7.2 一般参数与任意数量的关键词参数
# 参数里面还有一种情况是需要传不定数量的关键词参数，这又如何设计呢？

def show(**args):
    print("传入的参数可以循环打印")

    for key in args.items():
        print(key)

show(name="橡皮擦", age=18)

# 这种情况，你把传递进去的所有参数当成一个字典即可，自动聚合成了一个字典类型的数据。
# 如果与一般参数进行匹配，规则也非常简单。

def show(name,**args):
    print("传入的参数可以循环打印")
    print(name)
    for key in args.items():
        print(key)

show(name="橡皮擦", age=18)
# 上述代码先去匹配关键词参数，匹配成功了就赋值到对应关键词上，例如上面的 name 变量在函数调用时赋值了 橡皮擦，那它就等于橡皮擦，
# 其余的例如 age 没有关键词参数对应，只好打包给 **args 了。


# 高阶函数-map、filter、reduce
# map函数
# 接收一个函数 f 和一个或多个序列list，并通过把函数 f 依次作用在 序列list 的每个元素上，得到一个新的 list 并返回。
# 语法：map(function, iterable, ...)
# 参数：function -- 函数，iterable -- 一个或多个序列
# 返回值：Python 2.x 返回列表。Python 3.x 返回迭代器。

# 实例
def square(x) :            # 计算平方数
    return x ** 2
 
a = map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
print(list(a))
# 输出
[1, 4, 9, 16, 25]
map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(list(a))
# 输出
[1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]


# filter函数
# filter函数也是接收一个函数和一个序列的高阶函数，其主要功能是过滤。其返回值也是迭代器对象，例如：<filter object at 0x000002042D25EA90>，其图示如下：
# 接下来我们看一下filter函数的用法以及其机制是怎么样的：
names=["Alex","amanda","xiaowu"]
#filter函数机制
def filter_test(func,iter):
    names_1=[]
    for i in iter:
        if func(i): #传入的func函数其结果必须为bool值，才有意义
            names_1.append(i)
    return names_1
#filter_test函数
print(filter_test(lambda x:x.islower(),names))
# 输出
['amanda', 'xiaowu']
#filter函数
print(list(filter(lambda x:x.islower(),names)))
# 输出
['amanda', 'xiaowu']


# sorted() 函数
# 对所有可迭代的对象进行排序操作。
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
sorted(iterable, key=None, reverse=None)
# iterable – 可迭代对象。
# key – 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse – 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

# 返回重新排序的列表
print(sorted([5, 2, 8, 1, 3]))
# 输出
[1, 2, 3, 5, 8]
print(sorted({5: 'a', 2: 'd', 8: 'c', 1: 'f', 3: 'b'}))
# 输出
[1, 2, 3, 5, 8]

# 利用key进行倒序排序
exlist = [5, 0, 1, 9, 6, 4, 3]
reslist = sorted(exlist, key=lambda x: x * -1)
print(reslist)
# 输出
[9, 6, 5, 4, 3, 1, 0]

dlist=[{'name':'a','num':10},{'name':'e','num':5},{'name':'b','num':7},{'name':'c','num':2},{'name':'f','num':9}]
reslist = sorted(dlist, key=lambda x: x.get('name'))
print(reslist)
# 输出
[{'name': 'a', 'num': 10}, {'name': 'b', 'num': 7}, {'name': 'c', 'num': 2}, {'name': 'e', 'num': 5}, {'name': 'f', 'num': 9}]
reslist = sorted(dlist, key=lambda x: x.get('num'))
print(reslist)
# 输出
[{'name': 'c', 'num': 2}, {'name': 'e', 'num': 5}, {'name': 'b', 'num': 7}, {'name': 'f', 'num': 9}, {'name': 'a', 'num': 10}]

# 要进行反向排序，也可以通过传入第三个参数 reverse=True：
exlist = [5, 0, 1, 9, 6, 4, 3]
reslist = sorted(exlist, reverse=True)
print(reslist)
# 输出
[9, 6, 5, 4, 3, 1, 0]


