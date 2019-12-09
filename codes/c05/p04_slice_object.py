# -*- coding:utf-8 -*-
"""
自定义序列对象
"""

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

