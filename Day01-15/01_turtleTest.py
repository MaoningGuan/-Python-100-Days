#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用turtle画图
"""
import turtle

turtle.pensize(4)  # 画笔的笔划线条大小
turtle.pencolor('red')  # 线条颜色

"""画一个正方形"""
turtle.forward(100)  # 向前100
turtle.right(90)  # 右转90度
turtle.forward(100)  # 向前100
turtle.right(90)  # 右转90度
turtle.forward(100)  # 向前100
turtle.right(90)  # 右转90度
turtle.forward(100)  # 向前100

turtle.mainloop()
