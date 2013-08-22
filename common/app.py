'''
Created on 2013-6-28

@author: Administrator
'''

import tornado.web

class App(tornado.web.Application):
    def __init__(self, routes, **settings):
        tornado.web.Application.__init__(self, routes, **settings)