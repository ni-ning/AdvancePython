# -*- coding:utf-8 -*-


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, index):
        return self.employee[index]


company = Company(['alex', 'linda', 'catherine'])
employee = company.employee

for item in employee:
    print(item)

# for 首先去找 __iter__, 没有时优化去找__getitem__
for item in company:
    print(item)
