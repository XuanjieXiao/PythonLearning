# -*- coding: utf-8 -*-
# @Time : 2021/3/14 21:37
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：xuanjiexiao@163.com
# @File : chp2-9
# @Project : pythonlearning
for item in range(3):
    ppp = input('请输入密码:')
    if ppp == '666666':
        print('密码正确哦，嘿嘿！')
        break
    else:
        print('密码不正确哦，亲爱的！请重新输入！')
else:
    print('您已经输入了三次错误的密码，你的账号被锁定了！')