#!/usr/bin/python
#-*- coding: UTF-8 -*-

import sys
import os
import logging
import time
import datetime
import ftplib
import tarfile

def generate_file_name(day_str):
    year = int(day_str[0:4])
    month = int(day_str[5:7])
    day = int(day_str[8:10])
    cur_date = datetime.date(year, month, day)
    next_date = cur_date + datetime.timedelta(days=1)
    cur_date_str = cur_date.strftime("%Y%m%d")
    next_date_str = next_date.strftime("%Y%m%d")
    return "dtl_full_pv_detail"+cur_date_str+"0000-"+next_date_str+"0000.csv"

def generate_upload_file(day_fmt):
    '''
    生成传输数据
    :param day_fmt: 数据日期，格式: YYYY-mm-dd
    :return: 传输文件名字
    '''
    file_name = generate_file_name(day_fmt)
    # sql = (r'set hive.cli.print.header=true;'
    #        'select sid, uid, vid, pid, peid, req_url, page_title, ref_url, source_type,ext_url,entry_pid,'
    #        'entry_url,entry_title,entry_peid,exit_pid, exit_url,exit_title,exit_peid,search_keyword,'
    #        'se_charset,utm_name,utm_source,utm_medium,utm_term,utm_content,browser,browser_ver,os,os_ver,'
    #        'terminal_type,terminal_maker,terminal_model,screen_width,screen_height,system_platform, '
    #        'brower_language as browser_language,b_charset,browser_resolution,ip,ucountry,uregion,ucity,'
    #        'pv_starttime,pv_endtime,case when scroll_max is not null then scroll_max else 0 end as scroll_max, '
    #        'def01 from ptmind_data.dtl_full_pv_detail where sitetz="E0800" and partdt="' + day_fmt + '" and sid = "49512ddd";')
    # cmd = "hive -e '" + sql + "' > " + file_name
    cmd = "dir > " + file_name  # todo del test
    code = os.system(cmd)
    if(code == 0):
        # 将数据压缩
        tar_file_name = file_name + ".tgz"
        tar = tarfile.open( tar_file_name, "w:gz")
        tar.add(file_name)
        tar.close()
        os.remove(file_name)    # 删除压缩源数据
        return tar_file_name
    else:
        logging.info("generate_upload_file exec code %d, args %s", code, day_fmt)
        exit("generate_upload_file error")

def ftp_upload(files):
    status = "600 Transfer error"
    ftp = ftplib.FTP()
    ftp.set_debuglevel(2)
    try:
        # 打开调试级别2，显示详细信息;0为关闭调试信息
        ftp.connect('172.16.100.15', '21')
        # 连接
        ftp.login('ftpuser', '0459223lyx')
        logging.info( ftp.getwelcome() )
        # 设置缓冲块大小
        bufsize = 1024
        # 以读模式在本地打开文件
        for file in files:
            file_handler = open(file, 'rb')
            # 上传文件
            try:
                status = ftp.storbinary('STOR %s' % os.path.basename(file), file_handler, bufsize)
                if (status[0:3] == "226"):
                    logging.info("upload file %s ok", file)
                    upload_callback(file)
                else:
                    logging.error("upload %s error, status=%s", file, status)
                    exit("upload error")
            except Exception as e:
                logging.error("%s", e)
            finally:
                file_handler.close()
    except Exception as e:
        logging.error("%s", e)
    finally:
        ftp.set_debuglevel(0)
        ftp.quit()
    return status

def upload_callback(file):
    pass

def upload_between_date(start_date, end_date):
    date_begin = datetime.date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
    date_end = datetime.date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))
    upload_files = []
    for i in range( (date_end-date_begin).days + 1):
        day = date_begin + datetime.timedelta(days=i)
        file = generate_upload_file(day.__str__())
        upload_files.append(file)
    ftp_upload(upload_files)

def which_date(argv):
    start_date = ""
    end_date = ""
    argv_len = len(argv)
    if(argv_len == 0):
        start_date = time.strftime("%Y-%m-%d", time.localtime(time.time()-86400))
        end_date = start_date
    elif(argv_len == 1):
        start_date = argv[0]
        end_date = time.strftime("%Y-%m-%d", time.localtime())
    elif(argv_len == 2):
        start_date = argv[0]
        end_date = argv[1]
    if (is_valid_date(start_date) == True and start_date <= end_date):
        return 0, start_date, end_date
    return 1, start_date, end_date

def is_valid_date(date_str):
    try:
        time.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

if(__name__ == "__main__"):
    args_num = len(sys.argv)
    if( args_num > 3 ):
        logging.error("Usage: %s [start_date [end_date]], date format: YYYY-MM-DD", sys.argv[0])
        exit("args number error")

    # 设置当前脚本所在目录为工作路径
    cur_file_path = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(cur_file_path)

    # 获得上传数据的日期范围
    status, start_date, end_date = which_date(sys.argv[1:])
    # 准备上传数据
    if(status == 0):
        upload_between_date(start_date, end_date)
    else:
        logging.error("args error %s", sys.argv)
