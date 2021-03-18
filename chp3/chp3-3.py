# -*- coding: utf-8 -*-
# @Time : 2021/3/15 16:38
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：
# @File : chp3-3
# @Project : pythonlearning
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))
print(lst[1:6])  # 默认步长为1
print(lst[:6:2])  # 默认起始位置是0
print(lst[1::2])  # 默认末尾位置是最后的索引
