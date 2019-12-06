===============================
4.3 isinstance 和 type 的区别
===============================

- isinstance 会去查找继承链
- type 只判断变量的内存地址

.. code-block:: py

    class A:
        pass

    class B(A):
        pass

    b = B()
    print(isinstance(b, B))
    print(isinstance(b, A))

    # is 判断 id 的意思
    print(type(b) is B)
    print(type(b) is A)     # False
