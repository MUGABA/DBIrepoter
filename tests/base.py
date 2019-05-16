from api import create_app
from flask import current_app as app
from api.database.db import Database 
from api.Users.models import User
from werkzeug.security import generate_password_hash
import datetime
import json
import unittest

class BaseTest(unittest.TestCase):
	#this method will create setup tests
	# it also initialises the test_client where tests will be run

	def setUp(self):
		self.app = create_app('Testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.db = Database(self.app.config['DATABASE_URI'])
		self.db.create_tables()
		self.app = self.app.test_client()
		self.create_admin()

	def tearDown(self):
		self.db.drop_tables()

	def get_admin_token(self):
		admin_login_info = {
		"email":"mug@gmail.com",
		"password":"Mugaba123"
		}
		res = self.app.post('api/v1/users/login/admin',
							content_type = 'application/json',
							data = json.dumps(admin_login_info))
		data = json.loads(res.data.decode())
		return data['access_token']

	def get_user_token(self):
		user_info = {
		"firstname":"mug",
		"lastname":"rash",
		"othername":"muh",
		"username":"MUGABAMUHA",
		"email":"muh@gmail.com",
		"password":"Mugaba123",
		"phonenumber": 256705938222
		}

		user_login_info = {
		"email":"muh@gmail.com",
		"password":"Mugaba123"
		}
		self.app.post('api/v1/users', content_type = 'application/json',
						data = json.dumps(user_info))
		res = self.app.post('api/v1/users/login', content_type = 'application/json',
						data = json.dumps(user_login_info))
		data = json.loads(res.data.decode())
		return data


	def user_header(self):
		return {
		"content_type": "application/json",
		'Authorization': self.get_user_token()['access_token']
		}
	def admin_header(self):
		return {
		'content_type':'application/json',
		'Authorization': self.get_admin_token()
		}

	def create_admin(self):
		self.db.add_user('Mugaba','Muhamad','Rashid',
						'MUGABAMUHA','mug@gmail.com',
						generate_password_hash('Mugaba123'),
						25670593822, datetime.datetime.now(),
						is_admin = True)


if __name__ == '__main__':
	unittest.main()

