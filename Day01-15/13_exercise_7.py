# -*- coding: utf-8 -*-


class A(object):
    def __init__(self, parameter):
        self.test = parameter


def set_to_None(parameter):
    print(parameter)
    parameter = None
    print(parameter)


print('----传递list---------')
l = [1, 2, 3]
a = A(l)
print(a.test)
l.append(4)
print(a.test)
a.test.append(5)
print(a.test)
print(l)
print('----------------')
set_to_None(l)
print(l)
print('----传递int---------')
k = 5
b = A(k)
print(b.test)
k = k + 2
print(b.test)
b.test += 1
print(b.test)
print(k)
print('----------------')
set_to_None(k)
print(k)


class X(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


print('----传递class---------')
x = X()
c = A(x)
print(c.test.a)
x.a = 4
print(c.test.a)
c.test.a = 5
print(c.test.a)
print(x.a)
print('----------------')
set_to_None(x)
print(x)


"""
----传递list---------
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
----------------
[1, 2, 3, 4, 5]
None
[1, 2, 3, 4, 5]
----传递int---------
5
5
6
7
----------------
7
None
7
----传递class---------
1
4
5
5
----------------
<__main__.X object at 0x00000215F042C708>
None
<__main__.X object at 0x00000215F042C708>
"""


