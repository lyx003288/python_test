# import os
import sys
from multiprocessing import Pool
# import time
# from concurrent import futures
import test4
print("test2 run")

class MyLocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("  mylocker.unlock() called.")


class Lockerex(MyLocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")


def lockhelper(cls):
    """
    cls 必须实现acquire和release静态方法
    :param cls:
    :return:
    """

    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return __deco

    return _deco

abc = 1

import logging
def test(value):
    pid = 123
    global abc
    abc += 1
    info = "Value=%s, Pid=%s, abc=%s" % (value, pid, abc)
    logging.info(info)
    return info, 5


if __name__ == '__main__':
    print("test2")



