#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个正整数判断是不是素数。
"""
# number = int(input('请输入整数：'))
#
# flag = 1
# if number > 1:
#     for num in range(2, number):
#         if number % num == 0:
#             flag = 0
#             break
#     if flag:
#         print('%d是素数。' % number)
#     else:
#         print('%d不是素数。' % number)
# else:
#     print('%d不是素数。' % number)


from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
