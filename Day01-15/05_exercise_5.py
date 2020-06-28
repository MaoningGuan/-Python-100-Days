#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成斐波那契数列的前20个数
"""
first = 1
second = 1
print(first, second, sep=', ', end=', ')
for _ in range(3, 21):
    first, second = second, first + second
    print(second, end=', ')
