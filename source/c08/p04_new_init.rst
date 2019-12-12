===============================
8.4 __new__ 和 __init__ 的区别
===============================

- 自定义类中 __new__: 用来控制对象的生成过程，返回 self 对象，如果没有返回值，则不会调用 __init__
- 自定义类中 __init__: 用来完善对象，如初始化
- __new__ 在 __init__ 之前调用


.. code-block:: py

    class User(object):

        # 新式类才有，生成对象 user 之前加逻辑
        def __new__(cls, *args, **kwargs):
            # args = ('linda', )
            # kwargs = {'age': 20}
            # 与自定义 metaclass 中的 __new__ 有区别
            print('from __new__')
            self = super().__new__(cls)
            return self

        def __init__(self, name, age=18):
            self.name = name
            self.age = age
            print('from __init__')


    if __name__ == '__main__':
        user = User('linda', age=20)


PS: 统一描述

- 元类 -> 类对象
- 类 -> 实例
