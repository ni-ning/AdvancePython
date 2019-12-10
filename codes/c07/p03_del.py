# -*- coding:utf-8 -*-

# python 中垃圾回收算法为 引用计数

a = 1
b = a
del a

# del 触发 __del__ 逻辑

