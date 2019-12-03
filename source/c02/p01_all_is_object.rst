===============================
2.1 python中一切皆对象
===============================

-------------------------------
一切皆对象是python灵活性的根本
-------------------------------

- python是动态语言，面向对象更加彻底
- 函数和类也是对象，属于python的一等公民

一等公民特性

- 赋值给一个变量
- 可以添加到集合对象中
- 可以作为参数传递给函数
- 可以当做函数的返回值

.. code-block:: py

    def bar(name):
        print('Hello %s' % name)

    class Person(object):
        def __init__(self, name):
            print('Hello %s' % name)

    def decorator_func():
        print('from decorator_func')
        return bar

    def print_type(obj):
        print(type(obj))

    # 赋值给一个变量
    func = bar
    func('Linda')
    my_class = Person
    my_class('Tom')

    # 可以添加到集合对象中
    obj_list = []
    obj_list.append(bar)
    obj_list.append(Person)
    for item in obj_list:
        # 可以作为参数传递给函数
        print_type(item)

    # 可以当做函数的返回值
    deco_bar = decorator_func()
    deco_bar('deco_bar')
