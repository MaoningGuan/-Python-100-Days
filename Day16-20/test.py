# -*- coding: utf-8 -*-
class B(object):
    def __init__(self, a):
        self.a = a


class A(object):
    def __init__(self, value):
        self.value = value


def func(value):
    data = value
    data.a = 300
    return data

def main():
    data1 = B(100)
    obj = A(data1)
    obj.value.a = 200
    print(data1.a)
    print(obj.value.a)

    print('------------------')
    data2 = B(400)
    b = func(data2)
    print(data2.a)
    print(b.a)

    print('------改变原始类参数--------')
    data1.a = 500
    print(data1.a)
    print(obj.value.a)


if __name__ == '__main__':
    a = {'a': 1, 'b': 2}
    b = a
    print(a)
    print(b)

    a['a'] = 3
    print(a)
    print(b)

    b['b'] = 4
    print(a)
    print(b)


