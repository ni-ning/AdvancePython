# -*- coding:utf-8 -*-


class Cat:
    def say(self):
        print('I am a cat.')


class Dog:
    def say(self):
        print('I am a dog.')


class Duck:
    def say(self):
        print('I am a duck.')


# Python中较灵活，只要实现say方法就行，实现了多态
animal = Cat
animal().say()

# 实现多态只要定义了相同方法即可
animal_list = [Cat, Dog, Duck]
for an in animal_list:
    an().say()

"""
class Animal:
    def say(self):
        print('I am a animal.')

# 需要继承Animal，并重写say方法
class Cat(Animal):
   def say(self):
       print('I am a cat.')

# Java 中定义需要指定类型
Animal an = new Cat()
an.say()
"""

li1 = ['i1', 'i2']
li2 = ['i3', 'i4']

tu = ('i5', 'i6')
s1 = set()
s1.add('i7')
s1.add('i8')

# 转变观念，传入的不单单是list，甚至自己实现 iterable 对象
li1.extend(li2)     # iterable
li1.extend(tu)
li1.extend(s1)
print(li1)

