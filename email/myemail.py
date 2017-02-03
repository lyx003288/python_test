#!/usr/bin/python
#-*- coding: UTF-8 -*-

import sys
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

if(__name__ == '__main__'):
    path = sys.path
    path.append("C:/Program Files/Anaconda3/envs/python27/Lib")
    sys.path = path
    msg = MIMEText('hello 刘亚新, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'Python爱好者 <%s>' % 'lyx003288@163.com')
    msg['To'] = _format_addr(u'管理员 <%s>' % 'lyx003288@163.com')
    msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

    server = smtplib.SMTP("smtp.163.com")
    server.set_debuglevel(1)
    server.login("lyx003288", "722197yxh")
    server.sendmail("lyx003288@163.com", "lyx003288@163.com", msg.as_string())
    server.quit()


