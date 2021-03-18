# -*- coding: utf-8 -*-
# @Time : 2021/3/17 9:29
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：
# @File : chp3-6
# @Project : pythonlearning
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 30]
lst.remove(30) #如果有重复的元素，只移除第一个
print(lst)
lst.pop()
print(lst)

#切片操作
lst[1:3] = []
print(lst)

lst.clear()
print(lst)


del lst
print(lst)