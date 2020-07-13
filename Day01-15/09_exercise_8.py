#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
扑克游戏
"""
import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌（随机乱序"""
        self._current = 0
        random.shuffle(self._cards)  # 将序列元素随机排序

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)


# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    game_name = '21点'
    cards_number = 2
    for _ in range(cards_number):
        for player in players:
            player.get(p.next)

    print(game_name + ':')
    cards_number = []
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)
        # 计算玩家的点数
        pokers_sum = 0
        cards = player.cards_on_hand
        card_0 = cards[0].face
        card_1 = cards[1].face
        if 1 not in [card_0, card_1]:
            if card_0 in [11, 12, 13]:
                card_0 = 10
            if card_1 in [11, 12, 13]:
                card_1 = 10
            pokers_sum = card_0 + card_1
        else:
            if card_0 == 1 and card_1 == 1:
                pokers_sum = 12
            else:
                if card_0 == 1:
                    if card_1 in [11, 12, 13]:
                        card_1 = 10
                    pokers_sum = card_0 + card_1
                    number = card_1 + 11
                    if pokers_sum < number <= 21:
                        pokers_sum = number
                elif card_1 == 1:
                    if card_0 in [11, 12, 13]:
                        card_0 = 10
                    pokers_sum = card_0 + card_1
                    number = card_0 + 11
                    if pokers_sum < number <= 21:
                        pokers_sum = number
        cards_number.append(pokers_sum)

    print(cards_number)
    max_card_num = 0
    player = -1
    for index, card_number in enumerate(cards_number):
        if max_card_num < card_number <= 21:
            max_card_num = card_number
            player = players[index]

    if max_card_num != 0:
        print(f'赢家为{player.name}，点数为{max_card_num}')


if __name__ == '__main__':
    main()
