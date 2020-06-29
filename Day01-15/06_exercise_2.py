#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1、求最大公约数
2、求最小公倍数的函数
3、判断一个数是不是回文数的函数。
4、判断一个数是不是素数
5、求一个数的反向排列：1234 ——> 4321
"""


def gcd(x, y):
    """
    求x和y的最大公约数
    :param x:
    :param y:
    :return: x和y的最大公约数
    """
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """
    求x和y的最小公倍数
    :param x:
    :param y:
    :return: x和y的最小公倍数
    """
    return x * y // gcd(x, y)


def is_palindrome(num):
    """
    判断一个数是不是回文数
    回文数n：将n的各位数字反向排列所得自然数n1与n相等
    :param num:
    :return: True or False
    """
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime(num):
    """
    判断一个数是不是素数
    :param num:
    :return:
    """
    # 因为num的因子存在具有对称性，所以只需要判断前半部分int(num ** 0.5) + 1即可。
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


def reversed_num(num):
    """
    求一个数的反向排列：1234 ——> 4321
    :param num:
    :return:
    """
    if num < 0:
        raise TypeError('输入的数必须为正数!')
    return int(str(a)[::-1])


if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数。' % num)
    else:
        print('%d不是回文素数。' % num)
