# coding=utf-8
from __future__ import print_function
from functools import reduce

# lambda的使用
a = 2
a1 = [1, 2, 4, 5, 6, 9, 10, 15]

b = lambda x: x * 2
print(b(a))

c = lambda c, d, e: c * d * e
print(c(1, 2, 3))


# filter的使用

# 去掉偶数
def is_odd(n):
    return n % 2 == 1


print(filter(is_odd, a1))
# 去掉偶数lambda版
is_o = lambda x: x % 2 == 1
print(filter(is_o, a1))


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()


# 去除指定字符
print(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))

str = ['a', 'b', 'c', 'd', 'e']

filterStr = lambda x: x != 'a'

print(filter(filterStr, str))

# map的使用

# 对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
listStr = [11, 22, 33, 44, 55]
listStrOper = lambda x: x + 100
print(map(listStrOper, listStr))

# 如果给出了额外的可迭代参数，
# 则对每个可迭代参数中的元素‘并行’的应用‘function’。

list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]

abcOper = lambda a, b, c: a * 10000 + b * 100 + c

# 在每个list中，取出了下标相同的元素，执行了abcOper()。
print(map(abcOper, list1, list2, list3))

# 如果'function'给出的是‘None’，自动假定一个‘identity’函数

print(map(None, list1))

print(map(None, list1, list2, list3))

'''
map(function, iterable)
基本上等于：
[function(x) for x in iterable]
'''

result = []

# 列表推导
for a in list1:
    for b in list2:
        for c in list3:
            result.append(abcOper(abcOper))

'''
若是将三个list看做矩阵的话：
11 22 33
44 55 66
77 88 99

map()只做了列上面的运算，而列表推导（也就是嵌套for循环）做了笛卡尔乘积。
'''


# reduce 使用

# 实现一个整形集合的累加
def myadd(x, y):
    return x + y


# 结果便是输出1+2+3+4+5+6+7
sum = reduce(myadd, (1, 2, 3, 4, 5, 6, 7))
print(sum)

lst = [1, 2, 3, 4, 5]
print()
reduce(lambda x, y: x + y, lst)
# 这种方式用lambda表示当做参数，因为没有提供reduce的第三个参数，所以第一次执行时x=1,y=2,第二次x=1+2,y=3,即列表的第三个元素


# 或者
lst = [1, 2, 3, 4, 5]
print()
reduce(lambda x, y: x + y, lst, 0)


# 这种方式用lambda表示当做参数，因为指定了reduce的第三个参数为0，所以第一次执行时x=0,y=1,第二次x=0+1,y=2,即列表的第二个元素，
# 假定指定reduce的第三个参数为100，那么第一次执行x = 100, y仍然是遍历列表的元素，最后得到的结果为115

# 或者
def add(x, y):
    return x + y


print()
reduce(add, lst)


# 与方式1相同，只不过把lambda表达式换成了自定义函数

# 或者
def add(x, y):
    return x + y


print()
reduce(add, lst, 0)
# 与方式2相同，只不过把lambda表达式换成了自定义函数
