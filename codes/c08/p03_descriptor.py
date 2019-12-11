# -*- coding:utf-8 -*-

# property 可以更好低获取和设置，如果大量属性需要执行相同操作，如类型检测，则需要每个属性都要写一遍
# ORM 比较常见

# 实现了 __get__ 和 __set__ 数据属性描述符
# 只实现了 __get__ 非数据属性描述符
# 查找顺序也不同

import numbers


class IntField:
    def __init__(self):
        self._data = None

    def __get__(self, instance, owner):
        print(instance)     # <__main__.User object at 0x000002B88B270288>
        print(owner)        # <class '__main__.User'>
        print(type(instance) is owner)          # True
        print(instance.__class__ is owner)      # True
        return self._data

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('Need int value')
        # 重点来了，如何保存 value 呢，instance or self
        # 如果 instance.attribute 又会触发 __set__ 描述符
        self._data = value

    def __delete__(self, instance):
        pass


class User:
    age = IntField()
    num = IntField()


if __name__ == '__main__':
    user = User()
    user.age = 18
    print(user.__dict__)    # {} "age" 并没有进入到 __dict__

    print(user.age)
