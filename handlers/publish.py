

from common.request import BaseHandler
from common.convert import Convert
from datetime import datetime

class PublishHandler(BaseHandler):
    def get(self):
        self.render("publish.htm", **{ 'pageNo': 5,  'title':'发布奇迹服务器', 'keywords':'发布奇迹服务器', 'description':'发布奇迹服务器', 'msg':[1,2,3,4] })

    def post(self):
        pass