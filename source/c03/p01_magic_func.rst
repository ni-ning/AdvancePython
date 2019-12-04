===============================
3.1 什么是魔法函数
===============================

python 定义类时中，以双下划线开头，以双下划线结尾函数为魔法函数

- 魔法函数可以定义类的特性
- 魔法函数是解释器提供的功能
- 魔法函数只能使用 python 提供的魔法函数，不能自定义

.. code-block:: py

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
