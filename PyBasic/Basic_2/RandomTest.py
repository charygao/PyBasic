# coding=utf-8
from __future__ import print_function
import random
import threading


def newData():
    # 顾客定义
    guests = [random.randint(1, 9999999999) for _ in range(1)]
    # 点菜
    foods = [random.randint(1, 30) for _ in range(random.randint(1, 20))]
    return str(guests + foods) + "\n"


# 写入
def writeData(file,num):
    count = 0
    while count < num:
        try:
            file.write(newData())
            count += 1
        except Exception as e:
            print()
            'write warn log error', str(e)
            break
    print()
    'write data finished'


def main():
    global f
    fileName = 'Datas/orders.txt'
    # 模式：追加
    mode = 'w+'
    # 生成的数据量
    dataNum=1000
    # 创建线程来写文件
    try:
        f = open(fileName, mode)
        t = threading.Thread(target=writeData, args=[f,dataNum])
        t.start()
        t.join()

    except Exception as e:
        print()
        'write data failed,', str(e)
    finally:
        f.close()
    print()
    'write data finished'


if __name__ == '__main__':
    main()
