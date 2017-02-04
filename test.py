#!/usr/bin/python
#-*- coding: UTF-8 -*-

import sys
import logging

########################################################################################################################
########################################################################################################################
########################################################################################################################
import myutil.util
sys.excepthook = myutil.util.my_excepthook

if(__name__ == "__main__"):
    myutil.util.init_log_config()

    from simple_tcp import tcp_server
    tcp_server.start(8899)
    logging.info("%s running over", __file__)

