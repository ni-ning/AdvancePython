===============================
7.1 python 的变量是什么
===============================

- java 中变量相当于申请一个盒子，盒子有类型大小之说
- python 中变量，类似一个指针，指针的值是固定的，类似便利贴，可以贴到任何对象上

.. code-block:: py

    # a 贴到 1 上面
    a = 1
    # a 再贴到 'abc' 上
    a = 'abc'
    # 注意顺序: 先生成对象，然后贴便利贴

    la = [1, 2, 3]
    lb = la
    # is, 本质 id(a) 与 id(b) 比较
    print(lb is la)       # True, id 相同
    print(id(la), id(lb))

    la.append(100)
    print(lb)  # lb 和 la 指向相同对象，lb 会发生变化
