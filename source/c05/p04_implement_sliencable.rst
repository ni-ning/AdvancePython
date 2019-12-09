===============================
5.4 实现可切片的对象
===============================

--------------------
列表切片操作
--------------------

.. code-block:: py

    '''
    模式 [start:end:step]

    第一个数字 start 表示切片开始位置，默认 0
    第二个数字 end 表示切片截止(但不包含)位置，默认列表长度
    第三个数字 step 表示切片的步骤，默认为 1

    当 start 为 0 时可以省略
    当 end 为列表长度时可以省略
    当 step 为 1 时可以省略，并且省略步长时可以同时省略最后一个冒号
    当 step 为负数时，表示反向切片，这时 start 应该比 end 的值要大才行
    '''

    a_list = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
    a_list[::]      # 返回包含原列表中所有元素的新列表
    a_list[::-1]    # 返回包含原列表中所有元素的逆向新列表
    a_list[::2]     # 隔一个元素取一个，获取偶数位置的元素
    a_list[1::2]    # 隔一个元素取一个，获取奇数位置的元素
    a_list[3:6]     # 指定切片的开始和结束位置
    a_list[0:100]   # 切片结束位置大于列表长度是，从列表尾部截断
    a_list[100:]    # 切片开始位置大于列表长度时，返回空列表

    a_list[len(a_list):0] = [9]     # 在列表尾部增加元素
    a_list[:0] = [1, 2]             # 在列表头部增加元素
    a_list[3:3] = [100]             # 在列表中间位置插入元素
    a_list[:2] = [100, 200]         # 替换列表元素，等号两边长度相等
    a_list[3:] = [4, 5, 6]          # 替换列表元素，等号两边长度可以不相等
    a_list[:3] = []                 # 删除列表中前 3 个元素


--------------------
自定义序列类
--------------------

参考 collections.abc 序列类 Sequence 所需的魔法函数

.. code-block:: py

    import numbers

    class Group:
        def __init__(self, group_name, company_name, staff):
            self.group_name = group_name
            self.company_name = company_name
            self.staffs = staff

        def __reversed__(self):
            self.staffs.reverse()

        def __getitem__(self, item):
            cls = type(self)
            if isinstance(item, slice):
                return cls(group_name=self.group_name, company_name=self.company_name, staff=self.staffs[item])
            elif isinstance(item, numbers.Integral):
                return cls(group_name=self.group_name, company_name=self.company_name, staff=[self.staffs[item]])

        def __len__(self):
            return len(self.staffs)

        def __iter__(self):
            return iter(self.staffs)

        def __contains__(self, item):
            if item in self.staffs:
                return True
            else:
                return False


    staffs = ['linda', 'alex', 'catherine', 'nash', 'curry']
    group = Group(group_name='group', company_name='company', staff=staffs)
    sub_group = group[0]

    print('linda' in sub_group)
    print(len(sub_group))
