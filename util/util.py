#-*- coding: UTF-8 -*-
import logging
import logging.handlers

def init_log_config(log_file):
    logging.basicConfig(#filename=log_file,
                        # filemode='w',
                        level=logging.DEBUG,
                        format='%(asctime)s [%(filename)s %(funcName)s %(lineno)d] %(levelname)s: %(message)s',
                        datefmt='[%m/%d %H:%M:%S]')

    #################################################################################################
    formatter = logging.Formatter('%(asctime)s [%(filename)s %(funcName)s %(lineno)d] %(levelname)s: %(message)s')


    # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    # console = logging.StreamHandler()
    # console.setLevel(logging.INFO)
    # console.setFormatter(formatter)
    # logging.getLogger().addHandler(console)

    rotating = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024*1024*10, backupCount=3, delay=True)
    rotating.setLevel(logging.DEBUG)
    rotating.setFormatter(formatter)
    logging.getLogger().addHandler(rotating)


class StringNumberParse(object):
    '''
    判读一个utf-8字符串中的中文、数据、英文、其他字符的个数
    '''
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