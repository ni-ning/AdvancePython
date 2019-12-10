# -*- coding:utf-8 -*-

# set 不重复、无序
s1 = set('abcc')
print(s1)   # {'a', 'c', 'b'}

# frozenset 不可变可以作为 dict key
f1 = frozenset('abcc')
print(f1)
