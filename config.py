

import os
import tornado.web

import handlers.default
import handlers.publish
import handlers.test
import handlers.others.account

class Config(object):

	settings = {
		"debug": True,
		"static_path": os.path.abspath("static"),
		"template_path": os.path.abspath("templates"),
		"cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
		"login_url": "/login",
		"xsrf_cookies": False,
	}

	routes = [
		(r'/favicon.ico', tornado.web.StaticFileHandler),
		(r'/robots.txt', tornado.web.StaticFileHandler),
		(r'/crossdomain.xml', tornado.web.StaticFileHandler),
		(r'/humans.txt', tornado.web.StaticFileHandler),
		(r'/static/(.*)', tornado.web.StaticFileHandler),
		(r'/others/signup/', handlers.others.account.AccountHandler),
	]

