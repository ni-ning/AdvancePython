# -*- coding:utf-8 -*-

# a 贴到 1 上面
a = 1
# a 再贴到 'abc' 上
a = 'abc'

# 先生成对象，然后贴便利贴

la = [1, 2, 3]
lb = la
# is, 本质 id(a) 与 id(b) 比较
print(lb is la)
print(id(la), id(lb))

la.append(100)
print(lb)
