#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
print('请输入三角形的边长：')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('三角形的周长为：%.2f' % (a + b + c))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('三角形面积为：%.2f' % s)
else:
    print('不能构成三角形。')
