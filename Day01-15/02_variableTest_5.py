#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入圆的半径计算计算周长和面积。
"""
PI = 3.141592653
r = float(input('请输入圆的半径：'))
c = 2 * PI * r
s = PI * r * r

print('圆的半径为%.2f，周长为%.2f，面积为%.2f。' %
      (r, c, s))
