
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        pass
