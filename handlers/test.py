from common.request import BaseHandler

class TestHandler(BaseHandler):
    def get(self):
        self.render("others/account.htm", **{ 'title':'default', 'keywords':'default', 'description':'default', })