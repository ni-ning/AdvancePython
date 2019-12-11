# -*- coding:utf-8 -*-

# __getattr__, 在查找不到属性的时候调用

# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattr__(self, item):
#         return 'Not found attribute %s' % item
#
#
# if __name__ == '__main__':
#     user = User('linda')
#     print(user.age)


# class User:
#     def __init__(self, info=None):
#         if not info:
#             info = {}
#         self.info = info
#
#     def __getattr__(self, item):
#         return self.info[item]
#
#
# if __name__ == '__main__':
#     user = User({'name': 'linda', 'age': 18})
#     print(user.name)
#     print(user.age)

class User:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return 'get_attribute'


if __name__ == '__main__':
    user = User('linda')
    print(user.name)    # get_attribute
    print(user.test)    # get_attribute
    print(user.other)   # get_attribute
