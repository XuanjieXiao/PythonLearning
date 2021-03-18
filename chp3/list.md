@[TOC](零基础学Python-说说列表的那些事，列表的增删查询改，列表元素的排序（6）append，extend，clear,index,list,remove,pop)

# list
## 列表的创建
![列表的创建](https://img-blog.csdnimg.cn/20210315160536127.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_7,color_FFFFFF,t_70)
注意：
元素与元素之间需要用逗号进行分隔开。大家可以看看右边的内存示意图，可以知道其中的list的内容。
特别提醒，列表存储的是什么？是对应的元素的ID，这个很重要，注意理解这个其中。他不是直接存储的元素的值，是ID。

## 列表的特点

 1. 列表是有序的
 2. 列表的索引是从0开始的，类比于数组
 3. 列表可以存储重复的数据
 4. 任意的数据类型可以混存，因为他是存储的是ID，注意理解
 5. 根据需要进行动态的分配和回收对应的内存

## 列表的查询操作
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210315161436886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_16,color_FFFFFF,t_70)
### 查询重复元素时
通过代码进行演示，我们可以看到：
当列表中有重复元素的时候，利用index函数，返回的是首个数据的索引。
```python
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210315161931511.png)
下面举例：
### 查找索引里面1-3但是不包括3的数据里面包含有hello不？
可以观察index函数的解释，这里写的是自己，目标，开始，停止的英语，可以看出其格式。
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021031516223156.png)

```python
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))
print(lst.index('hello', 1, 3))
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210315162106868.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_16,color_FFFFFF,t_70)
## 获取列表中单个元素
==正向索引 0到N-1==
==逆向索引 -N到-1==
下面开始举例说明
获取索引为2的元素，完全可以参照数组
```python
lst = ['hello', 'world', 98, 'hello', 'world', 222]
# 获取索引为2的元素
print(lst[2])
```
获取索引为-3的元素，==***这个内容就不能参照数组了***==

## 列表元素的查询操作
看到下面的这个语法格式，注意中间是冒号
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210315163806537.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_16,color_FFFFFF,t_70)
### 当Step为正数的时候
```python
# -*- coding: utf-8 -*-
# @Time : 2021/3/15 16:38
# @Department of Aeronautics and Astronautics, Fudan University
# @Author : XuanjieXiao
# @Email：
# @File : chp3-3
# @Project : pythonlearning
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('原列表',id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))
print(lst[1:6])#默认步长为1
print(lst[:6:2])#默认起始位置是0
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210315164920832.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_16,color_FFFFFF,t_70)
### 当Step为负数的时候

```python
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))
print(lst[::])  # 全部默认,就开始逆向输出
print(lst[7::-1])  # 默认终止位置是0
print(lst[8:0:-2])  #
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210315165432864.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_16,color_FFFFFF,t_70)
## 列表元素的添加操作

 - **append()** &emsp;列表末尾添加一个元素
 - **extend()**  &emsp;列表末尾至少添加一个元素
 -  **insert()**  &nbsp;&emsp;列表任意位置添加一个元素
 - **切片**     &nbsp;&emsp; &emsp;列表任意位置添加至少一个元素

下面的这个部分的代码可以有助于我们去理解这些函数：
```python
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
```

## 列表元素的删除操作
|函数名|操作注意事项|
|--|--|
|remove| 移除元素，一次只移除一个元素，重复元素只删除第一个，元素不存在时候会报错ValueError |
|pop|  删除一个指定索引上的元素，指定索引不存在的时候报错IndexError，不指定索引的时候，就删除最后一个元素|
|切片|一次至少删除一个元素|
|clear|清空列表|
|del|删除列表|

```python
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
print(lst)#这里就会报错了，因为删除了列表了，没有列表了，肯定就打印不出来了，就会报错了
```

## 列表的修改操作
直接使用索引操作赋值
还可以使用切片操作对其进行赋值

```python
lst = [10, 20, 30, 40]
lst[2] = 100
print(lst)
lst[1:3] = [100, 300, 1000, 20000]
print(lst)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210317160203820.png)

## 排序操作
### 调用sort()，默认是升序

```python
lst = [10, 20, 90, 15, 30, 40]
print('排序前', lst, id(lst))
lst.sort()
print('排序后', lst, id(lst))

```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210317160533555.png)
### 还可以通过指定关键字参数使得列表使得降序排序
lst.sort(reverse = True) 这样使得函数为降序排列
lst.sort(reverse = False) 这样使得函数为升序排列

```python
lst = [10, 20, 90, 15, 30, 40]
print('排序前', lst, id(lst))
# lst.sort()
print('排序后', lst, id(lst))
lst.sort(reverse=False)
print('排序后', lst, id(lst))

```
### 使用内置函数Sorted()对列表进行排序，这里是产生了一个新的列表对象

```python
lst = [10, 20, 90, 15, 30, 40]
print('排序前', lst, id(lst))
# lst.sort()
# print('排序后', lst, id(lst))
# lst.sort(reverse=False)
# print('排序后', lst, id(lst))

new = sorted(lst)
print('排序后', new, id(new))
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210317161058810.png)
同样，可以指定关键词来进行指定升降序

```python
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
```

## 列表生成式
[i*i for i in range(1,10)]
注意这个i*i是列表真正存储的值，也叫列表元素的表达式
```python
lst=[i for i in range(1,10)]
print(lst)
lst2=[i*i for i in range(1,10)]
print(lst2)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210317161516176.png)

