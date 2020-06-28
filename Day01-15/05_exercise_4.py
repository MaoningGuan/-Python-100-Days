#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version: 0.1
Author: 关茂柠
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产为：', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
        else:
            print('下注的钱要大于0和小于总资产')

    first = randint(1, 6) + randint(1, 6)
    print('你第一次摇到的数字为', first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        needs_go_on = False
        second = randint(1, 6) + randint(1, 6)
        print('你再次摇到的数字为', second)
        if second == 7:
            print('庄家胜')
            money -= debt
        elif second == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
    print('-'*100)
print('你破产啦！')
