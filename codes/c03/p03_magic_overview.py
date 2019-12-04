# -*- coding:utf-8 -*-


class Company:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '<Company [%s]>' % self.name

    def __repr__(self):
        return '<Company [%s]>' % self.name


company = Company('Apple')
print(company)

# Python 解释器会隐含调用
print(company.__repr__())


class Num:
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


n = Num(-1)
print(abs(n))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)


v1 = Vector(1, 3)
v2 = Vector(2, 4)
print(v1 + v2)
