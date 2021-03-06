#!/usr/bin/python
#-*- coding: UTF-8 -*-

'''
    单例类
'''

# 使用装饰器(decorator),这是一种更pythonic,更elegant的方法
def singleton(cls):
    instances = {}
    from functools import wraps
    @wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

# 实现__new__方法
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

