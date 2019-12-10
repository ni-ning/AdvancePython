===============================
7.2 is 和 == 区别
===============================

.. code-block:: py

    # is, 本质 id(a) 与 id(b) 比较
    # = 右边为对象时，表示生成新对象
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    print(a is b)   # False, 说明 id 不同
    print(id(a), id(b))
    print(a == b)   # True, 值相同，内部 __eq__ 魔法函数

    # 内部优化 小整数、小字符串 全局唯一 intern机制
    a1 = 1
    a2 = 1
    print(a1 is a2)     # True

    s1 = 'abc'
    s2 = 'abc'
    print(s1 is s2)     # True


    class People:
        pass


    # People 全局唯一
    person = People()
    print(type(person) is People)   # True
