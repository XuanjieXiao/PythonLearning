# -*- coding: utf-8 -*-
# @Time : 2021/3/12 20:46
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-5
# @Project : pythonlearning
sum=0
for item in range(1,101):
    if item % 2 == 0:
        sum+=item
print('1-100的偶数和',sum)