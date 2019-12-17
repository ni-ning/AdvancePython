===============================
9.3 生成器函数的使用
===============================

生成器函数，函数里包含 yield 关键字

- yield
- 不再是普通的函数


.. code-block:: py

    def gen_func():
        yield 1
        yield 2
        yield 3

    # 惰性求值，延迟求值提供了可能性
    # 斐波拉契函数 0 1 1 2 3 5 8 ...
    def fib(index):
        if index <= 2:
            return 1
        else:
            return fib(index-1) + fib(index-2)

    def func():
        return 1

    if __name__ == '__main__':
        # 返回为生成器对象，python编译字节码的时候产生
        gen = gen_func()

        # 生成器对象也是实现了迭代协议的，可以for循环
        for value in gen:
            print(value)

        ret = func()

- 执行生成器函数得到生成器对象，可for循环取值
- 生成器函数可以多次返回值，流程的变化

.. code-block:: py

    # 获取对应位置的值
    def fib(index):
        if index <= 2:
            return 1
        else:
            return fib(index-1) + fib(index-2)


    # 获取整个过程
    def fib2(index):
        ret_list = []
        n, a, b = 0, 0, 1
        while n < index:
            ret_list.append(b)
            a, b = b, a + b
            n += 1
        return ret_list


    # yield
    def gen_fib(index):
        n, a, b = 0, 0, 1
        while n < index:
            yield b
            a, b = b, a + b
            n += 1


    print(fib(10))
    print(fib2(10))
    for value in gen_fib(10):
        print(value)


斐波拉契 1 1 2 3 5 8 ...

- 根据位置获取对应值
- 根据位置获取所有值
