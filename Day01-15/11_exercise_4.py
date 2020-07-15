#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
读写JSON文件
"""
import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('保存数据完成！')


if __name__ == '__main__':
    main()
