#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
列表的切片操作
"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# 列表拼接
fruits += ['peach', 'pear', 'mango']
print(fruits)
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来赋值列表
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)

