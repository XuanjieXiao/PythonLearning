# -*- coding: utf-8 -*-
# @Time : 2021/3/12 13:13
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-4
# @Project : pythonlearning

i=0
j=0
while j <= 100:
    if((j%2)==0):
        i = i + j
    j += 1
print(i)


for item in 'python':
    print(item)

for _ in range(10):
    print('人生苦短，我要吃肉')