# coding=utf-8
# 求解非线性方程组

from scipy.optimize import fsolve


# 定义求解的线性方程组
def f(x):
    x1 = [0]
    x2 = [1]
    return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]


# 输入初值并求解
result = fsolve(f, [1, 1])
print (result)

# 数值积分
# 倒入积分函数
from scipy import integrate


# 定义被积函数
def g(x):
    return (1 - x ** 2) ** 0.5


# 积分结果和误差
pi_2, err = integrate.quad(g, 1, 1)

# 由为积分知识知道积分结果为圆周率的一半
print (pi_2 * 2)
