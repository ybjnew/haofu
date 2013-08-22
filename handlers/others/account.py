from common.request import BaseHandler
from common.validator import Validator

class AccountHandler(BaseHandler):
	"""description of class"""
	def get(self):
		self.render("others/account.htm", **{ 'title':'default', 'keywords':'default', 'description':'default', })

	def post(self):
		op = self.get_argument("Op", "")
		if Validator.required(op) :
			if op == "signup":
				self.signup()
			elif op == "signin":
				pass


	def signup(self):
		loginName = self.get_argument("LoginName", "")
		loginPwd = self.get_argument("LoginPwd", "")
		email = self.get_argument("Email", "")
		checked = self.get_argument("Checked", "")
		if Validator.required(loginName) and Validator.required(loginPwd) and Validator.isEmail(email):
			pass
		else:
			self.write("ddddddddd")