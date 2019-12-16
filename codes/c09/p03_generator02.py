# -*- coding:utf-8 -*-
# 斐波拉契 1 1 2 3 5 8 ...


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
