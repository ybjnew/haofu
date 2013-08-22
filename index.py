'''
Created on 2013-6-19

@author: LH520
'''

import tornado.ioloop
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from common.app import App
import config

define("port", default=8888, help="run on the given port", type=int)

class Index(object):

	@staticmethod
	def main():
		tornado.options.parse_command_line()
		http_server = tornado.httpserver.HTTPServer(App(config.Config.routes, **config.Config.settings))
		http_server.listen(options.port)
		tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
	Index.main()