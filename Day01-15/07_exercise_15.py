#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
练习：
练习1：在屏幕上显示跑马灯文字。
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
练习3：设计一个函数返回给定文件名的后缀名。
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
练习5：计算指定的年月日是这一年的第几天。
练习6：打印杨辉三角。
"""
import os
import random
import time


def marquee():
    """
    在屏幕上显示跑马灯文字
    :return:
    """
    content = '北京欢迎你为你开天辟地......'
    while True:
        # 清理屏幕上的输出
        # os.system('cls')  # Linux: os.system('clear')
        os.system('clear All')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len：验证码的长度（默认4个字符）
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    # filename_list = filename.split('.')
    # print(filename_list)
    # if len(filename_list) > 1:
    #     return '.' + filename_list[-1] if has_dot else filename_list[-1]
    # else:
    #     return ''
    pos = filename.rfind('.')  # 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    """
    返回传入的列表中最大和第二大的元素的值
    :param x: 传入的列表
    :return: 列表中最大和第二大的元素的值
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in  range(month - 1):
        total += days_of_month[index]
    return total + day


def triangle(rows):
    """
    打印杨辉三角
    :param rows: 行数
    :return:
    """
    yh = [[]] * rows
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    rows = int(input('Number of rows: '))
    triangle(rows)
