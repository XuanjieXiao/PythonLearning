# -*- coding: utf-8 -*-
# @Time : 2021/3/12 9:15
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-2
# @Project : pythonlearning

money=12000
s=int(input('请输入要取款的金额'))
if s <= money:
    money-=s
    print('取款金额为：', s, '当前余额为', money)
else:
    print('取款错误')