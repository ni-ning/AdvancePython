# -*- coding:utf-8 -*-

# __new__ cls： 用来控制对象的生成过程，在对象之前
# __init__ self：用来完善对象，如赋值

# new 在 init 之前
# 如果 __new__ 方法无返回值，则不会调用 __init__函数


class User(object):

    # 新式类才有，生成对象 user 之前加逻辑
    def __new__(cls, *args, **kwargs):
        print('from __new__')
        # self = super().__new__(cls)
        self = object.__new__(cls)
        return self

    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        print('from __init__')


if __name__ == '__main__':
    user = User('linda', age=20)
