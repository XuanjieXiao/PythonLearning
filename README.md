# list

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210312100219697.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDc0OTA0Mw==,size_16,color_FFFFFF,t_70#pic_center)

## **转义字符**

注意事项：

 - 特别注意最后一个字符不能是反斜杠
 - r放在语句的最前面是表示回归到原字符
 - 注意查看相关的ASCLL码

	
变量
id（）标识符  
类型 type（）----------共有四种：int,float,bool,str  
如下：  
 - 	int整型
 - 	float 浮点型
 - 	str字符串型
 - bool布尔型，只有0和1
	
特别提醒：浮点数的计算具有不精确性，如果需要进行相关的计算，可以注意加上相关的语句。
举例说明：  
**from decimal import Decimal  
Decimal('3.3')+Decimal('3.3')=6.6
但是3.3+3.3不一定等于6.6**
		
 **- 三引号可以在多行进行书写，你的双引号不行，三引号有“”“ ”“”或者‘’‘  ’‘’**

数据类型转换
其中的相关转换关系，及相关的转换函数，见如下的转换图即可：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210312101535797.png#pic_center)

数据类型转换，直接转换			注意连接符+
	
进制的基本表示
		0b 二进制
		0o 八进制
		十进制就是直接的
		0x 十六进制

## **常用快捷键**


- 1.设置 (ctrl + alt + s)
- 2.快速创建文件 (alt + insert)
- 3.自动格式化 (ctrl + alt + l)
- 4.快速注释代码 (ctrl + /)
- 5.快速取消注释代码 (ctrl + /)
- 6.复制一行代码 (ctrl + d)
- 7.撤销操作 (ctrl + z)


## 注释方式


- 1.单行注释  用“#”
- 2.多行注释  用一对三引号表示    在这个部分内容的东西就是被注释掉了的，下面举例：
例如:  
“”"  
这是一个  
多行注释  
“”"  
或者：
'''
嘿嘿，
我是一个
多行注释哦
'''

提醒：有中文编码声明注释  我们通常在文件的开头添加，用以指定源码文件的编码格式,如：

```python
#coding:gbk
```

```python
#coding:utf-8
```