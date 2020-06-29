#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字典的使用
"""
scores = {'关茂柠': 95, 'Tom': 89, 'John': 90}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)
# 通过键可以获取字典中对应的值
print(items3[9])
print(scores['关茂柠'])
print(items2['a'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')

for key in scores.keys():
    print(f'{key}: {scores[key]}')

for value in scores.values():
    print(value)

for key, value in scores.items():
    print(f'{key}: {value}')

# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('Tom', 100))
print(scores)
# 清空字典
scores.clear()
print(scores)

