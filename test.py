#!/usr/bin/python
#-*- coding: UTF-8 -*-

# import os
from os import system
import sys
import time
import logging
import multiprocessing
from multiprocessing import Pool
# from concurrent import futures
########################################################################################################################
########################################################################################################################
########################################################################################################################
import myutil.util


sys.excepthook = myutil.util.my_excepthook
ver = sys.version_info


# def test(value):
#     print("thread=%s, time=%s, value=%s" % (os.getpid(), time.time(), value))
#
#     try:
#         value = 1
#         return value
#     finally:
#         value = 0
#         print("value %s" % value)
#
#     time.sleep(2)
#     return value


# def test2(value):
#     print("thread=%s, time=%s, value=%s" % (os.getpid(), time.time(), value))
#
#     # time.sleep(4)
#     command = "echo '123123' >> %s.txt" % value
#     os.system(command)
#     return value

import math
import concurrent.futures

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(is_prime, PRIMES)
    print([ ret for ret in result ])
        # for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        #     print('%d is prime: %s' % (number, prime))

# class AMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         print("A new args name %s" % name)
#         return type.__new__(cls, name, bases, attrs)
#
# class B(dict, metaclass=AMetaclass):
#     def __init__(self, **kwargs):
#         super(B, self).__init__(**kwargs)
#
# class C(B):
#     pass

# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, object):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#         attrs['__table__'] = name # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)

def test(str):
    return str and str.strip()



if __name__ == "__main__":
    myutil.util.init_log_config()
    logging.info("the Python version %s, cpu count %s" % (sys.version, multiprocessing.cpu_count()))
    # ####################################################################################################################
    # # exec_success_exit(__file__+" like 0%%", a=1, b=1)

    print(test("123   "))

    # L = [1, 3, 5, 7, 9, 8, 6, 4, 2]
    # L2 = ["python test2.py 1",  "python test2.py 2", "python test2.py 3", "python test2.py 4", "python test2.py 5"]
    # result_list = list()
    # print("start time %s" % time.time())
    # with futures.ProcessPoolExecutor() as pool:
    #     # ret1 = pool.submit( test, 1 )
    #     # ret2 = pool.submit( test2, 3 )
    #     #
    #     # r_ret1 = ret1.result()
    #     # r_ret2 = ret2.result()
    #     # print("%s %s ==" % (r_ret1, r_ret2))
    #     for ret in pool.map( os.system, L2 ):
    #         result_list.append(ret)
    # import concurrent_run
    # concurrent_run.concurrent_run(system, L2)
    # print("end time %s" % time.time())
    # print("result_list=%s" % result_list)
    ####################################################################################################################
    # add new line for test git

    # from simple_tcp import tcp_server
    # tcp_server.start()
    # logging.info("%s running over", __file__)
