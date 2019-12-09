===============================
5.6 什么时候我们不该用列表
===============================

- 比 list 更好的 python 内置数据结构
- array 数组 连续的内存空间，性能高
- deque 双向列表

--------------------
array 数组
--------------------

array 与 list 一个重要区别，array 只能存储指定的数据类型数据


.. code-block:: py

    import array

    list
    my_array = array.array('i')
    my_array.append(100)
    my_array.append('abc')




- 某些应用场景，除了 list 我们还有其他更好的选择
