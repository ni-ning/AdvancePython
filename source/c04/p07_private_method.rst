===============================
4.7 数据封装和私有属性
===============================


定义类时双下划线的属性，为私有属性


.. code-block:: py

    class User:
        def __init__(self):
            self.__age = 18

        def get_age(self):
            return self.__age

    if __name__ == '__main__':
        user = User()
        print(user.get_age())

        # print(user.__age)

        # _class__attr, 做了变形
        print(user._User__age)


- python并不能严格限制私有属性的使用，这是一种写代码规范
