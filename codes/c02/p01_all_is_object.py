# -*- coding: utf-8 -*-


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
obj_list = list()
obj_list.append(bar)
obj_list.append(Person)
for item in obj_list:
    print_type(item)
    # 可以作为参数传递给函数

# 可以当做函数的返回值
deco_bar = decorator_func()
deco_bar('deco_bar')
