===============================
4.2 抽象基类(abc模块)
===============================

--------------------
抽象基类
--------------------

- 抽象基类无法实例化
- 变量没有类型限制，可以指向任何类型
- 抽象基类和魔法函数构成了python的基础，即协议

在抽象基类定义了抽象方法，继承了抽象基类的类，必须实现这些方法

场景一：想判断某个对象的类型

.. code-block:: py

    # 检查某个类是否有某种方法
    class Company:
        def __init__(self, name):
            self.name = name

        def __len__(self):
            return len(self.name)


    company = Company('Linda Process Ltd.')
    print(hasattr(company, '__len__'))

    from collections.abc import Sized
    print(isinstance(company, Sized))



场景二：强制子类必须实现某些方法

.. code-block:: py

    import abc

    class CacheBase(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def get(self, key):
            pass

        @abc.abstractmethod
        def set(self, key, value):
            pass


    class MemoryCache(CacheBase):
        pass



注意：抽象基类容易设计过度，多继承推荐使用Mixin
