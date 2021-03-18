# -*- coding: utf-8 -*-
# @Time : 2021/3/14 21:31
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-8
# @Project : pythonlearning
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print('1-50内5的倍数包含有', item)
