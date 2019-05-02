import datetime

class User:
	#this holds all the attributs of a user as they sign up
	def __init__(self,firstname,lastname,othername,username,	
					email,password,phonenumber,is_admin=False):

		self.firstname = firstname
		self.lastname = lastname
		self.othername = othername
		self.username = username
		self.email = email
		self.password = password
		self.phonenumber = phonenumber
		self.registered = datetime.datetime.now()
		self.is_admin = is_admin