#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
《百钱百鸡》问题
"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print('公鸡：%d，母鸡：%d，小鸡：%d' % (x, y, z))
