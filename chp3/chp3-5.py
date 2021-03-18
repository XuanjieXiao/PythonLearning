# -*- coding: utf-8 -*-
# @Time : 2021/3/17 9:16
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：
# @File : chp3-5
# @Project : pythonlearning
lst = [10, 20, 30]
lst.append(10)
print(lst)
lst2 = [10, 20, 30]
lst.extend(lst2)
print(lst)
lst.insert(1, 66)
print(lst)
lst3 = ['hello', 'world']
print(lst)
lst[1:] = lst3
print(lst)
