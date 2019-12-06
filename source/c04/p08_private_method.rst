===============================
4.8 python对象的自省机制
===============================

通过一定的机制查询对象的内部结构

- __dict__
- dir()

.. code-block:: py

    class User:
        name = 'user'

    class Student(User):
        def __init__(self):
            self.school_name = 'school'

    if __name__ == '__main__':
        stu = Student()

        # 通过__dict__ 查询属性, C语言实现，经过优化，较快
        print(stu.__dict__)
        stu.__dict__['age'] = 18
        print(stu.age)

        print(User.__dict__)

        print(dir(stu))
