import re

# str.count(sub,start, end) 反回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法。
str='gfdsgfdsgfdsgfbfb'
print('gf在str中出现次数为：',str.count('gf'))
print('gf在str中0到len(str)之间出现次数为：',str.count('gf',0,len(str)))


str.encode(encoding="utf-8", errors="strict")
# 返回原字符串编码为字节串对象的版本。 默认编码为 'utf-8'。 可以给出 errors 来设置不同的错误处理方案。 
# errors 的默认值为 'strict'，表示编码错误会引发 UnicodeError。 其他可用的值为 'ignore', 'replace', 
# 'xmlcharrefreplace', 'backslashreplace' 


str='gfdsgfdsgfdsgfbfb'  
suffix=('a','b','c')   
# suffix='b'
print(str.endswith(suffix))
# str.endswith(suffix,0,len(str)) 如果字符串以指定的 suffix 结束返回 True，否则返回 False。 suffix 也可以为由多个供查找的后缀构成的元组。 
# 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。


str='gfdsgfdsgfdsgfbfb'
sub='d'
print(str.find(sub))
# str.find(sub, start, end)返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。 
# 可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。
# 注解 find() 方法应该只在你需要知道 sub 所在位置时使用。 要检查 sub 是否为子字符串，请使用 in 操作符:
# >>> 'Py' in 'Python'
# True

print("The sum of 1 + 2 is {0}".format(1+2))
# 'The sum of 1 + 2 is 3'
# str.format(*args, **kwargs)
# 执行字符串格式化操作。 调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域。 
# 每个替换域可以包含一个位置参数的数字索引，或者一个关键字参数的名称。 返回的字符串副本中每个替换域都会被替换为对应参数的字符串值。


str.lower()
# 返回原字符串的副本，其所有区分大小写的字符均转换为小写。
str.upper() # 到大写


str='gfdsgfdsgfdsgfbfb'
chars='g'
str.lstrip(chars)
str='   gfdsgfdsgfbfb'
str.lstrip()
# 返回原字符串的副本，移除其中的前导字符。 chars 参数为指定要移除字符的字符串。 
# 如果省略或为 None，则 chars 参数默认移除空格符。 实际上 chars 参数并非指定单个前缀；而是会移除参数值的所有组合:
str.rstrip(chars)  #与上条相似，右边
str.strip(chars)   #与上条相似，左右


str='gfdsgfdsgfdsgfbfb'
print(str.replace('gf', 'new',2))
# str.replace(old, new[, count]) 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 
# 如果给出了可选参数 count，则只替换前 count 次出现。







