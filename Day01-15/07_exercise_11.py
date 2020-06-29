#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
如何实现一个生成斐波拉切数列的生成器
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # print(type(fib(20)))
    for val in fib(20):
        print(val, end=' ')


if __name__ == '__main__':
    main()
