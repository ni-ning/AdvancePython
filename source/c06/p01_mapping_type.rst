===============================
6.1 dict的abc继承关系
===============================

from collections.abc import *


- Sized: __len__
- Iterable: __iter__
- Container: __contains__
- Collection: Sized, Iterable, Container
- Mapping: Collection
- MutableMapping: Mapping

可以看出来 dict 和 list 有一些共有的魔法函数

.. code-block:: py

    from collections.abc import Mapping

    # dict 属于 Mapping 类型
    d = dict()
    print(isinstance(d, Mapping))
