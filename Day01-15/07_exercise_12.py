#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
元组的使用
笔记：
1、元组在创建时间和占用的空间上面都优于列表。
2、元组中的元素是无法修改的：
如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组；
如果一个方法要返回多个值，使用元组也是不错的选择。
"""

# 定义元组
t = ('关茂柠', 25, True, '广东深圳')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# t[0] = '王大锤'  # TypeError
print('-'*100)
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 45
print(person)
print('-'*100)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
print(fruits_list)
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


