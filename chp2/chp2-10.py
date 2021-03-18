# -*- coding: utf-8 -*-
# @Time : 2021/3/14 21:45
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-10
# @Project : pythonlearning
for i in range(1,10):           #行数
    for j in range(1,i+1):          #列数
        print(i, '*', j, '=', i*j, ' ', end='')
    print()