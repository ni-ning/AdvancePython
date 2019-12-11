# -*- coding:utf-8 -*-
"""
user 某个类实例，user.age 等价于 getattr(user, 'age')
首先调用 __getattribute__
    如果定义了 __getattr__ 方法，调用 __getattribute__ 抛出异常 AttributeError 触发__getattr__
而对于描述符(__get__)的调用，则是发生在 __getattribute__内部

user = User(), 调用 user.age 顺序如下：
(1) 如果 'age' 是出现在 User 或基类的 __dict__ 中，且 age 是data descriptor，那么调用其 __get__(instance, owner) 方法，否则
(2) 如果 'age' 出现在 user 的 __dict__ 中，那么直接返回 user.__dict__['age']，否则
(3) 如果 'age' 出现在 User 或基类的 __dict__ 中
    (3.1) 如果 age 是 non-data descriptor, 那么调用其 __get__ 方法，否则
    (3.2) 返回 User.__dict__['age']
(4) 如果 User 有 __getattr__ 方法，调用 __getattr__ 方法，否则
(5) 抛出异常 AttributeError

"""


class NonDataIntFiled:
    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        return 100


class User:
    age = NonDataIntFiled()


if __name__ == '__main__':
    user = User()
    # user.__dict__['age'] = 18
    # user.age = 18
    # print(user.__dict__)
    print(user.age)

