===============================
8.1 property 动态属性
===============================

- 元类可以控制类的实例化过程

.. code-block:: py

    from datetime import date

    class User:
        def __init__(self, name, birthday):
            self.name = name
            self.birthday = birthday
            self._age = 0   # _ 一种编程规范

        @property
        def age(self):
            return date.today().year - self.birthday.year

        @age.setter
        def age(self, value):
            self._age = value

        def get_age(self):
            return self._age


    if __name__ == '__main__':
        user = User('linda', date(1987, 11, 14))
        print(user.age)     # @property 用变量的方式去封装逻辑
        user.age = 100      # @age.setter 接收参数
        print(user.get_age())   # self._age 实例内部有存储的变量 _age
