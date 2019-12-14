# -*- coding:utf-8 -*-

# 什么是迭代协议？ Iterable，Iterator

# 迭代器是什么？ 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性访问数据的方式

# [] list __iter__

from collections.abc import Iterable, Iterator
a = [1, 2]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
