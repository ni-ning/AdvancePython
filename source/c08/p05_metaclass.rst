===============================
8.5 自定义元类
===============================

- class 关键字 可以字面创建类

.. code-block:: py

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

    MyClass = create_class('user')
    obj = MyClass()
    print(obj)
    print(type(obj))    # <class '__main__.create_class.<locals>.User'>


- type 可以动态创建类，动态添加属性和方法

.. code-block:: py

    def func(self):
        return 'I am from func.'

    class Base:
        def answer(self):
            return 'I am from Base.answer.'

    # type 动态创建类
    User = type('User', (Base, ), {'name': 'user', 'func': func})
    user = User()
    print(user.name)
    print(user.func())
    print(user.answer())
    print(type(user))


元类创建类的类 metaclass(type) -> class -> instance

.. code-block:: py

    class MetaClass(type):
        # 用来控制 User 的创建过程 与 User 中的 __new__ 有区别
        def __new__(cls, name, bases, attrs, **kw):
            return super().__new__(cls, name, bases, attrs, **kw)


    class User(object, metaclass=MetaClass):

        def __init__(self, name):
            self.name = name

        def bar(self):
            print('from bar.')



python 在实例化的过程 user = User()

(1) 首先寻找 metaclass，来创建 User，否则
(2) 再次寻找基类 BaseUser 的 metaclass，来创建 User，否则
(3) 接着寻找模块 metaclass，来创建 User，否则
(4) 最后默认 type 为 metaclass 来创建 User
