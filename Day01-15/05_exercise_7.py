#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输出100以内所有的素数。
"""

# for num in range(2, 100):
#     is_prime = True
#     end = int(num / 2)
#     for x in range(2, end + 1):
#         if num % x == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=', ')

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
