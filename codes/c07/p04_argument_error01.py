# -*- coding:utf-8 -*-


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
