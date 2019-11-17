'''
@Author: your name
@Date: 2019-11-17 15:35:21
@LastEditTime: 2019-11-17 15:46:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tornado_study/chapter1/hello.py
'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


define('port', default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(slef):
        greeting = slef.get_argument('greeting', 'hello')
        slef.write(greeting + ", friendly user!")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
