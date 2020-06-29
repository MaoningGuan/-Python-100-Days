#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
列表的相关函数操作
"""
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
print(list1)
list1.insert(1, 400)
print(list1)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)
print(len(list1))  # 获取列表长度
print(list1)
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)
# 从指定的位置删除元素
list1.pop(0)
print(list1)
list1.pop(len(list1)-1)
print(list1)
# 清空列表元素
list1.clear()
print(list1)

