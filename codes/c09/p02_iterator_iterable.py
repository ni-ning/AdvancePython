# -*- coding:utf-8 -*-
# 实现__iter__时，必须返回Iterator对象

from collections.abc import Iterator


class MyIterator(Iterator):
    def __init__(self, employee):
        self.employee = employee
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        # 迭代器不支持切片，不会接收索引值，只能一步一步走
        # 遍历大文件
        try:
            word = self.employee[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


class Company:
    def __init__(self, employee):
        self.employee = employee

    # def __iter__(self):
    #     return 1        # TypeError: iter() returned non-iterator of type 'int'

    # def __iter__(self):
    #     return self     # TypeError: iter() returned non-iterator of type 'Company'

    # 使用内置方法 iter
    # def __iter__(self):
    #     return iter(self.employee)  # <iterator object at 0x000001F512B907C8>

    # 使用自定义 MyIterator ******
    def __iter__(self):
        return MyIterator(self.employee)    # <__main__.MyIterator object at 0x0000013462EF0848>

    def __getitem__(self, index):
        return self.employee[index]


if __name__ == '__main__':
    company = Company(['linda', 'alex', 'catherine'])
    my_iterator = iter(company)
    print(my_iterator)
    # for 循环首先查找 __iter__；如果没有自动生成一个__iter__，里面遍历__getitem__
    # for item in company:
    #     print(item)

    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            break

    """
    迭代器设计模式，不要在Company中实现 __next__ 方法，而要单独实现MyIterator实现，Company中__iter__调用MyIterator就行
    """
