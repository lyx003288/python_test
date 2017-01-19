#!/usr/bin/python
#-*- coding: UTF-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import httplib

class HttpMsgHandler(BaseHTTPRequestHandler):
    m_data = []

    def do_GET(self):
        try:
            print(self.path)
            print(self.headers.headers[0])
            message = json.dumps(self.m_data)
            self.send_response(httplib.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(message)
        except Exception as e:
            print(e)
        finally:
            print("===============================================================")

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if(ctype != 'application/json'):
            self.send_error(httplib.UNSUPPORTED_MEDIA_TYPE, "Only json data is supported")
            return

        length = int(self.headers['content-length'])
        post_values = self.rfile.read(length)
        try:
            print("recv post data: %s" % post_values)
            parse_values = json.loads(post_values)
            self.m_data.append(parse_values)

            self.send_response(httplib.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(post_values)
        except Exception as e:
            print(e)
        else:
            print("handler post data ok")
        finally:
            print("===============================================================")

def start_http_server( ip, port ):
    try:
        from BaseHTTPServer import HTTPServer
        http_server = HTTPServer((ip, port), HttpMsgHandler)
        print("simple http server started ...")
        http_server.serve_forever()
    except Exception as e:
        print(e)

if(__name__ == "__main__"):
    # 测试指令: curl -H "Content-type: application/json;charset=UTF-8"  localhost:8899 -d "{\"key\":\"value\"}"
    start_http_server( "localhost", 8899 )
