# -*- coding: utf-8 -*-
class A(object):
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    print('----类对象之间赋值------')
    a = A(100)
    b = a
    print(a.value)
    print(b.value)
    a.value = 200
    print(a.value)
    print(b.value)
    b.value = 300
    print(a.value)
    print(b.value)

    print('----list之间赋值------')
    list1 = [1]
    list2 = list1
    print(list1)
    print(list2)
    list1.append(2)
    print(list1)
    print(list2)
    list2.append(3)
    print(list1)
    print(list2)

    print('----数值之间赋值------')
    a = 1
    b = a
    print(a)
    print(b)
    a = 2
    print(a)
    print(b)
    b = 3
    print(a)
    print(b)

"""
----类对象之间赋值------
100
100
200
200
300
300
----list之间赋值------
[1]
[1]
[1, 2]
[1, 2]
[1, 2, 3]
[1, 2, 3]
----数值之间赋值------
1
1
2
1
2
3
"""