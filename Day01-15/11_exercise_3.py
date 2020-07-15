#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
读写二进制文件
"""


def main():
    try:
        with open('星座.jpg', 'rb') as f1:
            data = f1.read()
            print(type(data))
        with open('星座复制.jpg', 'wb') as f2:
            f2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开！')
    except IOError as e:
        print('读写文件时出现错误！')
    print('程序执行结束.')


if __name__ == '__main__':
    main()