#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
综合案例3：井字棋游戏
"""
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def judge(board):
    """
    判断哪个玩家取胜
    :param board:
    :return:
    """
    values = list(board.values())
    win = ''
    # 取胜的所有组合
    groups = ['123', '456', '789', '147', '258', '369', '159', '357']
    for ele in groups:
        index = list(ele)
        if values[int(index[0])-1] == values[int(index[1])-1] == values[int(index[2])-1] == 'x':
            win = 'x'
            break
        elif values[int(index[0])-1] == values[int(index[1])-1] == values[int(index[2])-1] == 'o':
            win = 'o'
            break
    return win


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        result = ''
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
            result = judge(curr_board)
            if result:
                break
        if result:
            print(f'{result}玩家取胜。')
        else:
            print('和局。')
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
