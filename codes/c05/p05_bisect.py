# -*- coding:utf-8 -*-

import bisect

# 处理已排序 序列 升序
# 内部二分查找算法实现

l1 = list()
bisect.insort(l1, 10)
bisect.insort(l1, 3)
bisect.insort(l1, 2)
bisect.insort(l1, 6)

print(l1)
