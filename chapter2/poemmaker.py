'''
@Author: your name
@Date: 2019-11-17 16:27:45
@LastEditTime: 2019-11-17 16:50:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tornado_study/chapter2/poemmaker.py
'''
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", help="run on the given port", default=8000, type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class PoemPageHandler(tornado.web.RequestHandler):

    def post(self):
        noun1 = self.get_argument("nonu1")
        noun2 = self.get_argument('nonu2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('nonu3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)
    

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", IndexHandler),
        (r"/poem", PoemPageHandler)
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
