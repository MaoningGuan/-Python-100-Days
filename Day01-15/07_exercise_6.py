#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
列表的相关原生操作
"""
list1 = [1, 3, 5, 7, 100]
print(list1)
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1))
# 下标(索引)运算
print(list1[0])
print(list1[4])
print(list1[-1])  # 100
print(list1[-3])  # 5
list1[2] = 300  # 修改元素的值
print(list1)  # [1, 3, 300, 7, 100]
print('-'*100)
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
print('-'*100)
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
print('-'*100)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
