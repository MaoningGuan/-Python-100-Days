#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python读文本文件
"""
import time


def main_1():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()


def main_2():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')

def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    print('-'*100)
    # 通过for-in循环逐行读取
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    print('-'*100)

    # 读取文件按行读取到列表中
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
