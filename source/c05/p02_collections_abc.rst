===============================
5.2 序列的abc继承关系
===============================

python 中内置的 collections.abc 抽象基类，可以帮助我们理解数据类型实现细节

python 是基于协议的语言，结合鸭子类型和魔法函数，就可以达到实现某种类型

from collections.abc import *

- Iterable: __iter__
- Reversible: __reversed__
- Sized: __len__
- container: __contains__
- Collection: Sized, Iterable, container
- Sequence: __getitem__, Reversible, Collection
- MutableSequence: __setitem__, __delitem__, Sequence
