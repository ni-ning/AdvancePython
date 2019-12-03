# -*- coding:utf-8 -*-

num = 1
name = 'linda'
print(type(num))
print(type(int))
print(type(name))
print(type(str))

# type -> int -> 1
# type -> str -> 'linda'
# type -> Student -> stu
# so: type -> class -> obj


class Student:
    pass


class MyStudent(Student):
    pass


# object 是最顶层基类
# type 是一个类，同时 type 也是一个对象

stu = Student()
print(type(stu))
print(type(Student))

print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(MyStudent.__bases__)

print(type.__bases__)       # (<class 'object'>,)
print(object.__bases__)     # () 最顶层基类，即没有基类

print(type(object))         # <class 'type'>
