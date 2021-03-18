# -*- coding: utf-8 -*-
# @Time : 2021/3/14 22:18
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-11
# @Project : pythonlearning
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
            # break
        print(j, end='\t')
    print('结束了')
