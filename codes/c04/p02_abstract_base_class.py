# -*- coding:utf-8 -*-


# 场景一：检查某个类是否有某种方法
class Company:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)


company = Company('Linda Process Ltd.')
print(hasattr(company, '__len__'))

# 某些情况下，想判断某个对象的类型
from collections.abc import Sized
print(isinstance(company, Sized))


# 场景二：强制子类必须实现某些方法
class CacheBase:
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    pass


# 只有调用的时候才抛异常
redis = RedisCache()
# redis.get('key')


import abc


class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class MemoryCache(CacheBase):
    pass


# 初始化时就抛异常
memory = MemoryCache()