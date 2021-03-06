#!/usr/bin/python
#-*- coding: UTF-8 -*-

import itertools
import time
import logging
from myutil.singleton import singleton
from myutil.singleton import Singleton
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define
import tornado.web

def handle_msg( session_id, msg ):
    GameServer().send_msg(session_id, "server send: {}".format(msg))

@singleton
class GameServer(TCPServer):
    def __init__(self):
        # super(GameServer, self).__init__()
        TCPServer.__init__(self)
        self.session_id = itertools.count(1)
        self.m_stream_dict = {}
        self.m_session_dict = {}

    def _on_connect(self, stream):
        if (stream not in self.m_stream_dict):
            next_session_id = next(self.session_id)
            self.m_stream_dict[stream] = next_session_id
            self.m_session_dict[next_session_id] = stream
            logging.info("[%d] new connect", next_session_id)
            return next_session_id

    def _on_disconnect(self, session_id):
        if(session_id in self.m_session_dict):
            stream = self.m_session_dict[session_id]
            del self.m_session_dict[session_id]
            del self.m_stream_dict[stream]
        else:
            logging.error("_on_disconnect error")

    # @gen.coroutine
    def send_msg(self, session_id, msg):
        if(session_id in self.m_session_dict):
            # yield self.m_session_dict[session_id].write(msg.encode("utf-8"))
            self.m_session_dict[session_id].write(msg.encode("utf-8"))
            logging.info("[%d] send msg: %s", session_id, msg)
        else:
            logging.error("[%d] send msg error, msg: %s", session_id, msg)

    @gen.coroutine
    def close(self, session_id, code=1, reason="normal"):
        if (session_id in self.m_session_dict):
            stream = self.m_session_dict[session_id]
            yield stream.write("[{}] close, code = {}, reason = {}\n".format(session_id, code, reason))
            yield stream.close()
        else:
            logging.error("[%d] connect close error, code = %d, reason = %s", session_id, code, reason)

    @gen.coroutine
    def handle_stream(self, stream, address):
        session_id = self._on_connect(stream)
        while True:
            try:
                data = yield stream.read_until(b"\n")
                data_utf8 = data.decode("utf-8")
                logging.info("[%d] recv msg: %s" % (session_id, data_utf8))
                # data = yield stream.read_bytes(read_len)
                handle_msg(session_id, data_utf8)
            except StreamClosedError:
                self._on_disconnect(session_id)
                logging.warning("[%d] disconnect at host %s, port %d", session_id, address[0], address[1] )
                break
            except Exception as e:
                logging.error(e)
            finally:
                pass

@singleton
class call_later_callback(object):
    def __init__(self):
        self.counter = itertools.count(1)

    def heartbeat(self):
        if(next(self.counter) % 60 == 0):
            logging.info("time:%s " % time.strftime('%m-%d %H:%M:%S', time.localtime()))
        IOLoop.current().call_later(1, self.heartbeat)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GET: Hello, world")

    def post(self, *args, **kwargs):
        self.write("POST: Hello world")

def start(*, tcp_port=8899, web_port=8888):
    define("tcp_port", default=tcp_port, help="Tcp port to listen on")
    define("web_port", default=web_port, help="Web port to listen on")
    options.parse_command_line()

    server = GameServer()
    server.listen(options.tcp_port)
    server.listen(8800)
    logging.info("Listening on TCP port %d", options.tcp_port)

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(options.web_port)
    logging.info("Listening on Web port %d", options.web_port)

    # IOLoop.current().call_later(1, call_later_callback().heartbeat)
    IOLoop.current().start()



