===============================
7.4 一个经典的参数错误
===============================

a, b 都是整型时

.. code-block:: py

    def add(a, b):
        a += b
        return a

    if __name__ == '__main__':
        a, b = 1, 2
        c = add(a, b)
        print('a: %s, b: %s, c: %s' % (a, b, c))
        # 结果为 a: 1, b: 2, c: 3
        # a 未发生变化


a, b 都是列表时

.. code-block:: py

    def add(a, b):
        a += b
        return a

    if __name__ == '__main__':
        a, b = [1, 2], [3, 4]
        c = add(a, b)
        print('a: %s, b: %s, c: %s' % (a, b, c))
        # 结果为 a: [1, 2, 3, 4], b: [3, 4], c: [1, 2, 3, 4]
        # a 发生变化


a, b 都是元组时

.. code-block:: py

    def add(a, b):
        a += b
        return a


    if __name__ == '__main__':
        a, b = (1, 2), (3, 4)
        c = add(a, b)
        print('a: %s, b: %s, c: %s' % (a, b, c))
        # 结果为 a: (1, 2), b: (3, 4), c: (1, 2, 3, 4)
        # a 未发生变化


默认类型为可变类型时

.. code-block:: py

    class Company:
        def __init__(self, name, staff_list=[]):
            self.name = name
            self.staff_list = staff_list

        def add(self, staff):
            self.staff_list.append(staff)

        def remove(self, staff):
            self.staff_list.remove(staff)


    if __name__ == '__main__':
        com1 = Company('com1', ['staff1', 'staff11'])
        com1.add('staff111')
        com1.remove('staff11')
        print(com1.staff_list)

        com2 = Company('com2')
        com2.add('staff2')

        com3 = Company('com3')
        com3.add('staff3')

        print(com2.staff_list)  # ['staff2', 'staff3']
        print(com3.staff_list)  # ['staff2', 'staff3']

- 默认值为可变类型 []，com2.staff_list 和 com3.staff_list 指向一块内存空间
