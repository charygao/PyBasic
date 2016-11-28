# coding=utf-8
from __future__ import print_function
import numpy as np
import scipy


'''
数组的使用

'''
# 创建数组
a = np.array([2, 0, 1, 6])
# 输出数组
print(a)

# 引用前三个数字（切片）
print(a[:3])

# 最大值和最小值
print(a.min())
print(a.max())

# 从小到大排序，直接修改数组a
a.sort()
print(a)

# 二维数组
b=np.array([[1,2,3],[4,5,6]])

# 输出数组的平方阵
print (b*b)