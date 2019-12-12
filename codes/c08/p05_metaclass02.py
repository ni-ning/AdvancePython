# -*- coding:utf-8 -*-

# 元类创建类的类 metaclass(type) -> class -> instance


class MetaClass(type):
    # 用来控制 User 的创建过程 与 User 中的 __new__ 有区别
    def __new__(cls, name, bases, attrs, **kw):
        return super().__new__(cls, name, bases, attrs, **kw)


class User(object, metaclass=MetaClass):

    def __init__(self, name):
        self.name = name

    def bar(self):
        print('from bar.')


# python 在实例化的过程 user = User()
# (1) 首先寻找 metaclass，来创建 User，否则
# (2) 再次寻找基类 BaseUser 的 metaclass，来创建 User，否则
# (3) 接着寻找模块 metaclass，来创建 User，否则
# (4) 最后默认 type 为 metaclass 来创建 User

