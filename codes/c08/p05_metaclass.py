# -*- coding:utf-8 -*-

# 类也是对象，type创建类的类
# 如何不写 class 关键字，更加灵活创建类呢

# 什么是元类，元类是创建类的类， 对象 <- class(对象) <- type


def create_class(name):

    if name == 'user':
        class User:
            def __str__(self):
                return 'User'
        return User

    elif name == 'company':
        class Company:
            def __str__(self):
                return 'Company'
        return Company


def func(self):
    return 'I am from func.'


class Base:
    def answer(self):
        return 'I am from Base.answer.'


if __name__ == '__main__':
    # MyClass = create_class('user')
    # obj = MyClass()
    # print(obj)
    # print(type(obj))

    # type 动态创建类
    User = type('User', (Base, ), {'name': 'user', 'func': func})
    user = User()
    print(user.name)
    print(user.func())
    print(user.answer())
    print(type(user))

