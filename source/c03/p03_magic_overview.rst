===============================
3.3 魔法函数一览
===============================

-------------
非数据运算
-------------

字符串表示

- __repr__
- __str__

.. code-block:: py

    class Company:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return '<Company [%s]>' % self.name

        def __repr__(self):
            return '<Company [%s]>' % self.name


    company = Company('Apple')
    print(company)

    # Python 解释器会隐含调用
    print(company.__repr__())



集合、序列相关

- __len__
- __getitem__
- __setitem__
- __delitem__
- __contains__

迭代相关

- __iter__
- __next__

可调用

- __call__

with 上下文管理器

- __enter__
- __exit__



-------------
数据运算
-------------

- __abs__
- __add__

.. code-block:: py

    class Num:
        def __init__(self, num):
            self.num = num

        def __abs__(self):
            return abs(self.num)


    n = Num(-1)
    print(abs(n))


    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __str__(self):
            return 'Vector(%s, %s)' % (self.x, self.y)


    v1 = Vector(1, 3)
    v2 = Vector(2, 4)
    print(v1 + v2)
