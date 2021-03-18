# -*- coding: utf-8 -*-
# @Time : 2021/3/17 16:04
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：
# @File : chp3-8
# @Project : pythonlearning
lst = [10, 20, 90, 15, 30, 40]
print('排序前', lst, id(lst))
# lst.sort()
# print('排序后', lst, id(lst))
# lst.sort(reverse=False)
# print('排序后', lst, id(lst))

# new = sorted(lst)
# print('排序后', new, id(new))
new = sorted(lst, reverse=True)
print('排序后', new, id(new))