# -*- coding:utf-8 -*-


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
