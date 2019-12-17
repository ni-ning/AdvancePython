# -*- coding:utf-8 -*-


def gen_func():
    address = 'China'
    yield 1
    name = 'linda'
    yield 2
    age = 20
    return 'done'


gen = gen_func()

import dis
print(dis.dis(gen))

print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

print('\nfirst value: %s' % next(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

print('\nsecond value: %s' % next(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)


# 控制整个生成器函数暂定和继续前进 gen.gi_frame.f_lasti
# 整个生成器函数作用域逐渐变化 gen.gi_frame.f_locals

