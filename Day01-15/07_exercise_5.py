#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符串的格式输出
"""
a, b = 5, 10

# method 1
print('%d * %d = %d' % (a, b, a * b))
# method 2
print('{a} * {b} = {c}'.format(a=a, b=b, c=a * b))
# method 3: python3.6以上
print(f'{a} * {b} = {a * b}')
