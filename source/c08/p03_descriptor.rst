===============================
8.3 属性描述符和属性查找过程
===============================

property 实现在数据获取和设置时增加额外逻辑处理，并对外提供简单接口

在批量属性操作，如验证，则需要每个属性都要写一遍，代码重复

- 数据属性描述符：实现 __get__ 和 __set__ 方法
- 非数据属性描述符： 实现 __get__ 方法

.. code-block:: py

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



转变原先简单的属性获取顺序


.. code-block:: py

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


- 属性描述符优先级最高

.. code-block:: py

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
