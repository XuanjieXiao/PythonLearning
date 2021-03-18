# -*- coding: utf-8 -*-
# @Time : 2021/3/12 20:54
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-6
# @Project : pythonlearning
for item in range(100,1000):
    ge=item%10
    shi=(item//10)%10
    bai=item//100
    # shuixianhua=ge*ge*ge+shi*shi*shi+bai*bai*bai
    shuixianhua=ge**3+shi**3+bai**3
    if item==shuixianhua:
        print(item)

