# -*- coding:utf-8 -*-


class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
print(a.x, a.y, A.aa)

A.aa = 111
a.aa = 100  # 新建一个a的属性aa， 100赋值给该aa
print(A.aa, a.aa)
