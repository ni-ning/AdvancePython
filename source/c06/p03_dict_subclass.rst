===============================
6.3 dict的子类
===============================

- 不建议直接继承 c 语言实现的内置结构 dict，list

.. code-block:: py

    class MyDict(dict):
        def __setitem__(self, key, value):
            super().__setitem__(key, value * 2)


    my_dict = MyDict(one=1)
    print(my_dict)  # 1, 某些情况下，不会调用重写的__setitem__
    my_dict['one'] = 1
    print(my_dict)  # 2, 触发重写的 __setitem__


- 可继承 UserDict 实现自定义
- python 语法模拟 c 语言实现细节


.. code-block:: py
    from collections import UserDict

    # python 语法模拟 c 语言实现细节
    class CustomDict(UserDict):
        def __setitem__(self, key, value):
            super().__setitem__(key, value * 2)


    dd = CustomDict(one=1)
    print(dd)


    d1 = UserDict({'kk': 'vv'}, k1='v1')
    print(d1)


- defaultdict 实现 __missing__

.. code-block:: py

    from collections import defaultdict

    d2 = defaultdict(list)
    # 实现了 __missing__ 魔法函数，可参考UserDict __getitem__ 实现
    value = d2['key']
    print(value)
    print(dict(d2))
