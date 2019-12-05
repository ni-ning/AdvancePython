# -*- coding:utf-8 -*-


# class A:
#     name = 'linda'
#
#     def __init__(self):
#         self.name = 'object'
#
#
# a = A()
# print(a.name)

# class D:
#     pass
#
#
# class C(D):
#     pass
#
#
# class B(D):
#     pass
#
#
# class A(B, C):
#     pass
#
#
# print(A.__mro__)

class D:
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
