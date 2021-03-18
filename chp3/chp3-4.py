# -*- coding: utf-8 -*-
# @Time : 2021/3/15 16:51
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：
# @File : chp3-4
# @Project : pythonlearning
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))
print(lst[::])  # 全部默认,就开始逆向输出
print(lst[7::-1])  # 默认终止位置是0
print(lst[8:0:-2])  #