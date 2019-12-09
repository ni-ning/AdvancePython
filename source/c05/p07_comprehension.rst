===========================================
5.7 列表推导式、生成器表达式和字典推导式
===========================================

--------------------
列表推导式
--------------------

列表推导式(列表生成式)： 通过一行代码生成列表

.. code-block:: py

    # 提取出 1-20 之间的奇数
    odd_list = [i for i in range(21) if i % 2 == 1]
    print(odd_list)

    # 逻辑复杂的情况
    def handle_item(item):
        return item * item

    odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]
    print(odd_list)

- 列表生成式性能高于列表操作
- 逻辑过于复杂时，列表生成式可读性降低

--------------------
生成器表达式
--------------------

列表推导 [] -> ()

.. code-block:: py

    my_gen = (i for i in range(21) if i % 2 == 1)
    print(type(my_gen))     # <class 'generator'>
    for i in my_gen:
        print(i)


--------------------
字典推导式
--------------------

.. code-block:: py

    d1 = {'key1': 'value1', 'key2': 'value2'}
    d2 = {v: k for (k, v) in d1.items()}
    print(d2)


--------------------
集合推导式
--------------------

.. code-block:: py

    set1 = {v for v in d1.values()}
    print(set1)
