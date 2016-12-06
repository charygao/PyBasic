# # coding=utf-8
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(1)  # 创建图表1
# plt.figure(2)  # 创建图表2
# ax1 = plt.subplot(211)  # 在图表2中创建子图1
# ax2 = plt.subplot(212)  # 在图表2中创建子图2
# x = np.linspace(0, 3, 100)
# for i in xrange(5):
#     plt.figure(1)  # ❶ # 选择图表1
#     plt.plot(x, np.exp(i * x / 3))
#     plt.sca(ax1)  # ❷ # 选择图表2的子图1
#     plt.plot(x, np.sin(i * x))
#     plt.sca(ax2)  # 选择图表2的子图2
#     plt.plot(x, np.cos(i * x))
# plt.show()
#
#

import numpy as np
import matplotlib.pyplot as plt

xData = np.arange(0, 10, 1)
yData1 = xData.__pow__(2.0)
yData2 = np.arange(15, 61, 5)
plt.figure(num=1, figsize=(8, 6))
plt.title('Plot 1', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
plt.show()