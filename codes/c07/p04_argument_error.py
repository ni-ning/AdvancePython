# -*- coding:utf-8 -*-


def add(a, b):
    a += b
    return a


if __name__ == '__main__':
    # a, b = 1, 2
    # c = add(a, b)
    # print('a: %s, b: %s, c: %s' % (a, b, c))

    # a, b = [1, 2], [3, 4]
    # c = add(a, b)
    # print('a: %s, b: %s, c: %s' % (a, b, c))

    a, b = (1, 2), (3, 4)
    c = add(a, b)
    print('a: %s, b: %s, c: %s' % (a, b, c))