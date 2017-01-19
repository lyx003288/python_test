#!/usr/bin/python
#-*- coding: UTF-8 -*-

import httplib
import urllib

def request(method, ip, port, cmd, params):
    try:
        headers = {'Content-type':'application/json;charset=UTF-8'}
        http_client = httplib.HTTPConnection(ip, port, timeout=5)
        http_client.request(method, cmd, params, headers)
        response = http_client.getresponse()
        print("head: %s" % response.getheaders())
        print("status: %s, reason: %s" % (response.status, response.reason))
        content = response.read()
        print("content %s" % content )
    except Exception as e:
        print(e)
    finally:
        if(http_client):
            http_client.close()
        print("====================== finale ===========================")

if(__name__ == '__main__'):
    #　get method
    get_params = urllib.urlencode({'name': 'airy', 'age': '25'})
    request("GET", "localhost", 8899, "/index.jsp?"+get_params, "")
    # post method
    post_params = "{\"key\":\"value\"}"
    request("POST", "localhost",  8899, "/index.jsp", post_params)

