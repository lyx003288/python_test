#!/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import print_function
import util

#  练习1
# 1 2 3 4 组成没有重复数字的三位数
def combination():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if( i != j ) and ( i != k ) and ( j != k ):
                    print(i*100+j*10+k)


# combination()

# 练习2
def profit_award():
    profit = int(raw_input("净利润："))
    arr = [ 1000000, 600000, 400000, 200000, 100000, 0 ]
    rat = [ 0.01, 0.015, 0.03, 0.05, 0.075, 0.1 ]
    award = 0
    for idx in range(0,6):
        if(profit > arr[idx]):
            tmp =  profit - arr[idx]
            tmp_award = tmp * rat[idx]
            print(" 利润: ", tmp_award)
            award = award + tmp_award
            profit = profit - arr[idx]
    print('你输出的内容是', award)

# profit_award()

# 练习5
def test5():
    l = []
    for i in range(3):
        num = int(raw_input())
        l.append(num)
    l.sort()
    print(l)
    l.reverse()
    print(l)

# test5()

# 练习6
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    if(n==1):
        return [1]
    if(n==2):
        return [1,1]
    l = [ 1, 1 ]
    for i in range(2, n):
        l.append(l[-1] + l[-2])
    print (l)

# fib2(10)

# 练习7
def test7():
    l_1 = [ 1, 2, 3, 4 ]
    l_2 = list(l_1)
    print ( l_2 )

# test7()

# 练习8
def test8():
    for i in range(1, 10):
        for j in range(1, 10):
            print("%d * %d = %d" % ( i, j, i*j ))

# test8()

# 练习9
def test9():
    import time
    D = { 1 : "value1", "key2" : "value2" }
    for key, value in D.items():
        print("key=%s, value=%s" % ( key, value) )
        time.sleep(0.3)

# test9()

def test11():
    f1 = 1
    f2 = 1
    for i in range(1, 21):
        print('%12ld %12ld' % (f1, f2),)
        if (i % 3) == 0:
            print('')
        f1 = f1 + f2
        f2 = f1 + f2

# test11()

def test12():
    from math import sqrt
    leap = 1
    for i in range(101, 201):
        k = sqrt( i )
        for j in ( 2, k+1 ):
            if( i % j == 0 ):
                leap = 0
                break
        if(leap==1):
            print("%-4d" % i,)
        leap = 1
# test12()

def test13():
    for i in range(101, 999):
        m = i / 100
        n = i / 10 % 10
        k = i % 10
        if ( i == m ** 3 + n ** 3 + k ** 3 ):
            print("%5d" % i )

# test13()

def test15(n):
    score = "A"
    if n >= 100:
        score = "A"
    elif n >= 80:
        score = "B"
    elif n >= 60:
        score = "C"
    else:
        score = "D"
    print("score %s" % score)

# test15(34)
# test15(90)

class StringNumberParse(object):
    def __init__(self):
        self.init()

    def __init__(self, utf8_string):
        self.init()
        self.parse(utf8_string)

    def init(self):
        self.chinese_number = 0
        self.letter_number = 0
        self.digit_number = 0
        self.other_number = 0

    def __del__(self):
        self.init()

    def getChinesesNumber(self):
        return self.chinese_number

    def getLetterNumber(self):
        return self.letter_number

    def getDigitNumber(self):
        return self.digit_number

    def getOtherNumber(self):
        return self.other_number

    def parse(self, utf8_string):
        self.clear()
        decode_str = utf8_string.decode("utf-8")
        for char in decode_str:
            print ("char=%s, char_ascii=%d, unicode=%s" % ( char, ord(char), char.encode('unicode_escape')))
            if(char >= u'\u4e00') and (char <= u'\u9fa5'):
                self.chinese_number = self.chinese_number + 1
            elif(char.isalpha()):
                self.letter_number = self.letter_number + 1
            elif(char.isdigit()):
                self.digit_number = self.digit_number + 1
            else:
                self.other_number = self.other_number + 1

    def clear(self):
        self.init()

def test17():
    str = raw_input("please input str:")
    str_num_parse = StringNumberParse(str)
    print(str_num_parse.getChinesesNumber())
    print(str_num_parse.getLetterNumber())
    print(str_num_parse.getDigitNumber())
    print(str_num_parse.getOtherNumber())

# test17()

def test18():
    Tn = 0
    Sn = []
    n = int(raw_input("please input repeat time:"))
    a = int(raw_input("please input one digit between 1~ 9:"))
    for count in range(n):
        Tn = Tn + a
        a = a * 10
        Sn.append( Tn )
    print("Sn=%s" % Sn)
    Sn = reduce( lambda x, y: x+y, Sn )
    print( "Sn=%s" % Sn )

# test18()

def test20():
    Sn = 100.0
    Hn = Sn
    for n in range(2, 11):
        Sn = Sn + Hn
        Hn = Hn / 2
    print("Total of rold is %f, the high %f" % (Sn ,Hn/2))

# test20()

def test21():
    X = 1
    for i in range(1, 10):
        X = (X + 1) * 2
    print("X=%d" % X)

# test21()

def test22():
    for i in { 'x', 'y', 'z'} - { 'x' }:
        for j in { 'x', 'y', 'z'}:
            for k in { 'y' }:
                if (i != j ) and (i != k) and ( j != k ):
                    print('order is a -- %s\t b -- %s\tc--%s' % (i, j, k))

# test22()

def test27(s, l):
    if(l <= 0):
        return ""
    print("%s" % s[l-1])
    test27(s, l-1)

# str = raw_input("input str:")
# test27(str, len(str))

def test28(n):
    if(n == 1):
        c = 10
    else:
        c = test28(n-1)+2
    return c

# print(test28(5))

def test33():
    L = ( 1, 2, 3, 4, 5 )
    Str = "-=-".join( str(e) for e in  L )
    print("str=%s" % Str)
# test33()

def test34():
    print("test34")

def call_test34():
    test34()

class test35(object):
    Red = "red"
    Black = "black"
    White = "white"

# print(test35.Black)
# print(test35.Red)
# print(test35.White)

def test40():
    L = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
    Len = len(L)
    for i in range( Len / 2 ):
        L[i], L[Len-1-i] = L[Len-1-i], L[i]
    print(L)

# test40()
def exchange(x, y):
    return (y, x)

def test47():
    x = 10
    y = 20
    print("%d %d" % (x, y))
    x, y = exchange(x, y)
    print("%d %d" % (x, y))

# test47()

import random
def test48():
    print( random.uniform(10,20) )
# test48()


def test51():
    a = 0o21
    print(a)
# test51()

def test62():
    str = "abcdef"
    sub_str = "de"
    index = str.find( sub_str )
    print("find index %d" % index)
# test62()

def test67():
    L = [ 4, 5, 64, 2, 52, 62, 23, 41 ]
    print(L)
    MaxIndex = 0
    MinIndex = 0
    Len = len(L)
    for idx in range( 1, Len-1 ):
        if( L[idx] > L[MaxIndex] ):
            MaxIndex = idx
        elif(L[idx] < L[MinIndex]):
            MinIndex = idx
    print("MaxIndex=%d, MinIndex=%d" % ( MaxIndex, MinIndex ))
    L[0], L[MaxIndex] = L[MaxIndex], L[0]
    L[Len-1], L[MinIndex] =  L[MinIndex], L[Len-1]
    print(L)

# test67()
def peven(n):
    s = 0.0
    for i in range(2, n+1, 2):
        s = s + 1.0 / i
    return s

def podd(n):
    s = 0.0
    for i in range(1, n+1, 2):
        s = s + 1.0 / i
    return s

def pcall( fn, n ):
    s = fn(n)
    return s

from tornado.ioloop import IOLoop
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define

# define("port", default=8899, help="TCP port to listen on")
# logger = logging.getLogger(__name__)

# import time
# import thread
#
# def tcp_test( stream, data ):
#     print("todo some thing %s" % data)
#
# class EchoServer(TCPServer):
#     @gen.coroutine
#     def handle_stream(self, stream, address):
#         while True:
#             try:
#                 data = yield stream.read_until(b"\n")
#                 logger.info("thread id=%s, Received bytes: %s", thread.get_ident(), data)
#                 if not data.endswith(b"\n"):
#                     data = data + b"\n"
#                 tcp_test(stream, data)
#                 if(data != "\r\n"):
#                     g_recv_data = "hahhaha\n"
#                     yield stream.write(g_recv_data)
#                     yield stream.write("tell send over\n")
#                 else:
#                     print("send none")
#             except StreamClosedError:
#                 logger.warning("Lost client at host %s", address[0])
#                 break
#             except Exception as e:
#                 print("ssssssssss")
#                 print(e)

class A(object):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()  # new
        print("leave A")


class B(object):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()  # new
        print("leave B")


class C(A):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")


class D(A):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()
        print("leave D")


class E(B, C):
    def __init__(self):
        print("enter E")
        super(E, self).__init__()  # change
        print("leave E")


class F(E, D):
    def __init__(self):
        print("enter F")
        super(F, self).__init__()  # change
        print("leave F")

    @staticmethod
    def static_test(x):
        print("static test %s" % x)


def h():
    F()

import logging

if(__name__ == "__main__"):
    util.init_log_config("log/example.log")

    ret = hasattr(F, 'static_test')

    for i in range(10):
        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')
        logging.error('This is error message')
        logging.critical('This is critical message')

    # logging.basicConfig(
    #     filename='log/example.log',
    #     filemode='w',
    #     level=logging.DEBUG,
    #     format='%(asctime)s %(levelname)s: %(message)s',
    #     datefmt='[%m/%d %H:%M:%S]')

    # import time
    # time.sleep(10)
    # print("fffffffffffffff")

    # import tcp_server
    # tcp_server.start(8899)
    # options.parse_command_line()
    # server = EchoServer()
    # server.listen(options.port)
    # logger.info("Listening on TCP port %d", options.port)
    # IOLoop.current().start()
    # print("start .................")





