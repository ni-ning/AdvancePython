# -*- coding:utf-8 -*-


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))

# is 判断 id 的意思
print(type(b) is B)
print(type(b) is A)     # False
