==========================================
8.2 __getattr__、__getattribute__魔法函数
==========================================

--------------------
__getattr__
--------------------

.. code-block:: py

    class User:
        def __init__(self, name):
            self.name = name

        def __getattr__(self, item):
            return 'Not found attribute %s' % item

    if __name__ == '__main__':
        user = User('linda')
        print(user.age) # Not found attribute age

- __getattr__, 在查找不到属性的时候调用
- 类似 else 机制


.. code-block:: py

    class User:
        def __init__(self, info=None):
            if not info:
                info = {}
            self.info = info

        def __getattr__(self, item):
            return self.info[item]


    if __name__ == '__main__':
        user = User({'name': 'linda', 'age': 18})
        print(user.name)
        print(user.age)

- 神奇的代理操作


--------------------
__getattribute__
--------------------

.. code-block:: py

    class User:
        def __init__(self, name):
            self.name = name

        def __getattribute__(self, item):
            return 'get_attribute'


    if __name__ == '__main__':
        user = User('linda')
        print(user.name)    # get_attribute
        print(user.test)    # get_attribute
        print(user.other)   # get_attribute


- 只要调用属性，就会触发 __getattribute__
- 把持了整个属性调用入口，尽量不要重写这个方法
- 写框架时会涉及到
