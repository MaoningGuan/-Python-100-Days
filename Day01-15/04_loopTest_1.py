#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
猜数字游戏
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入你猜测的数字：'))
    if number > answer:
        print('大一点')
    elif number < answer:
        print('小一点')
    else:
        print('猜测的数字正确，正确数字为：%d' % answer)
        break
print('你总共猜了%d次。' % counter)
if counter > 7:
    print('你的智商和运气都不太行哦。')