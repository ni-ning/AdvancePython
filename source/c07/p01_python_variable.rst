===============================
7.1 python 的变量是什么
===============================

- java 中的变量和python的变量定义不同，java 中什么变量时相当于会申请一个盒子，有类型大小
- python 中什么变量，实质上是一个指针，指针的值是固定的，类似便利贴，可以贴到任何对象上

.. code-block:: py

    # a 贴到 1 上面
    a = 1
    # a 再贴到 'abc' 上
    a = 'abc'

    # 先生成对象，然后贴便利贴

    la = [1, 2, 3]
    lb = la
    # is, 本质 id(a) 与 id(b) 比较
    print(lb is la)
    print(id(la), id(lb))

    la.append(100)
    print(lb)
