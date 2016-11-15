# coding=utf-8
from __future__ import print_function
import random

for num in range(10):
    # 顾客定义
    guests = [random.randint(1, 1000000000000) for _ in range(1)]
    # 点菜
    foods = [random.randint(1, 30) for _ in range(10)]
    # print(guests + foods)


def main():
    fout = open("/home/lele/文档/Codes/Pycharm/PyBasic/PyBasic/PyBasic/Basic_2/test.txt", "w")

    for i in range(5):
        line = str(i) + "\n"
        fout.write(line)

    fout.close()
