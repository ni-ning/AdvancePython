# -*- coding:utf-8 -*-

# 生成器函数，函数里只要有 yield 关键字
# - yield
# - 不再是普通的函数


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
    pass
