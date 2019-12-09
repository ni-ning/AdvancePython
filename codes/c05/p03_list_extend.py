# -*- coding:utf-8 -*-

# + 加新增
l1 = [1, 2]
l2 = l1 + [3, 4]
print("type(l1): %d, and l1: %s" % (id(l1), l1))
print("type(l2): %d, and l2: %s" % (id(l2), l2))

# += 就地加
l1 += ['3', '4']
l1 += ('5', '6')
l1 += range(2)
print("type(l1): %d, and l1: %s" % (id(l1), l1))


# + 两边类型需相同
# += 只需要可迭代的就行，__iadd__ 魔法函数实现




