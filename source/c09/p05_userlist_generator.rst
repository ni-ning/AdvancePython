===============================
9.5 生成器在UserList中的应用
===============================

- from collections import UserList

.. code-block:: py

    class MyList:
        def __init__(self):
            self.data = []

        def __getitem__(self, index):
            return self.data[index]

        def __setitem__(self, index, value):
            self.data[index] = value

        def insert(self, index, item):
            self.data.insert(index, item)


    ll = MyList()
    ll.insert(0, 1)
    ll.insert(0, 2)
    ll.insert(0, 3)
    print(ll.data)


- from collections import UserDict

.. code-block:: py

    class MyDict:
        def __init__(self):
            self.data = {}

        def __getitem__(self, item):
            return self.data[item]

        def __setitem__(self, key, value):
            self.data[key] = value

        def update(self, **kw):
            for key, value in kw.items():
                self[key] = value

    dd = MyDict()
    print(dd.data)

    dd.update(key1='value1', key2='value2')
    print(dd['key1'])
    print(dd.data)


具体源码分析参考模块 collections
