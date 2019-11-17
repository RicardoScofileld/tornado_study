'''
@Author: your name
@Date: 2019-11-17 16:14:45
@LastEditTime: 2019-11-17 16:24:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tornado_study/chapter1/hello_errors.py
'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import define, options

define('port', default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ", friendly user!")

    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error." % status_code)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop().instance().start()