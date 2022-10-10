import random

a = 0
b = 6

random.random()
# 返回 [0.0, 1.0) 范围内的下一个随机浮点数。

random.randint(a, b)
# 随机生成[a,b]范围内一个整数。

random.uniform(a, b)
# 返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。
# 取决于等式 a + (b-a) * random() 中的浮点舍入，终点 b 可以包括或不包括在该范围内。

seq = ['d', 's', 'r', 'q']
print(random.choice(seq))
# 从非空序列 seq 返回一个随机元素。该序列可以是list、tuple、str、set。 如果 seq 为空，则引发 IndexError。

population = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
random.choices(population, weights=None, k=1)
# population：集群。
# weights：相对权重。
# cum_weights：累加权重。
# k：选取次数。
# 作用：从集群中随机选取k次数据，返回一个列表，可以设置权重。
# 注意每次选取都不会影响原序列，每一次选取都是基于原序列。

# 关于random.choices()函数我举几个例子：
# import random
a = [1, 2, 3, 4, 5]
#1
print(random.choices(a, k=5))
#2
print(random.choices(a, weights=[0, 0, 1, 0, 0], k=5))
#3
print(random.choices(a, weights=[1, 1, 1, 1, 1], k=5))
#4
print(random.choices(a, cum_weights=[1, 1, 1, 1, 1], k=5))

# 对于 #1–#4 的每一条语句不妨各自写一个循环语句让它输出个十遍八遍的，你就足以看出用法了。
# 这里我只提出运行结果和结论：
#1 ： 重复输出10次列表a中的各个成员出现概率基本持平。
#2 ： 重复输出10次每次输出均得到[3,3,3,3,3]结果。
#3 ： 重复输出10次列表a中的各个成员出现概率基本持平。
#4 ： 重复输出10次每次输出均得到[1,1,1,1,1]结果。

k = 1
random.sample(population, k)
# 从集群population中选取k个元素，返回一个列表，集群可以是list、tuple、str、set。
# 与random.choices()的区别：一个是选取k次，一个是选取k个，选取k次的相当于选取后又放回，选取k个则选取后不放回。故random.sample()的k值不能超出集群的元素个数。
# import random
# a = ['ahh','hhh','zzz','emm']
# print(random.sample(a,3))
#['hhh', 'zzz', 'ahh']

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
random.shuffle(lst)
print(lst)
# 随机打乱序列lst的顺序并重新排序，注意它无返回值，另外lst只能是一个可变序列，且只支持有下标的序列，因此它也不适用于set，你最好只把它用在列表上。