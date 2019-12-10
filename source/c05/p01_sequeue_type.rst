===============================
5.1 python中的序列分类
===============================

序列是 python 中重要的协议


按照元素类型是否相同

- 容器序列：list、tuple、deque
- 扁平序列：str、bytes、bytearray、array.array

按照元素是否可变

- 可变类型：list、deque、bytearray、array.array
- 不可变：str、tuple、bytes


.. code-block:: py

    # 元素类型任意
    my_list = list()
    my_list.append(100)
    my_list.append(True)

    # 指定元素类型
    import array
    my_array = array.array('i')
    my_array.append(100)
    # 初始化数组需要整型，附加字符串抛异常
    my_array.append('abc')
