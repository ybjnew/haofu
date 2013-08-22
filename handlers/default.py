

from common.request import BaseHandler

class DefaultHandler(BaseHandler):
    def get(self):
        self.render("others.htm", **{ 'title':'default', 'keywords':'default', 'description':'default', })