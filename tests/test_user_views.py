from tests.base import BaseTest
from api.Users import views
import json
import datetime

class UserTestCase(BaseTest):
    def test_returns_error_if_firstname_is_not_valid(self):
        data = {
            "firstname":"",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber":256785687486,
            "username":"mugbamuh",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or not filled in")
    def test_returns_error_if_lastname_is_not_valid(self):
        data = {
            "firstname":"muga",
            "lastname":"",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber":256785687486,
            "username":"mugbamuh",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or not filled in")

    def test_returns_error_if_othername_is_not_valid(self):
        data = {
            "firstname":"Shidie",
            "lastname":"Muga",
            "othername":"",
            "email":"muga@gmail.com",
            "phonenumber":256785687486,
            "username":"mugbamuh",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or not filled in")

    def test_returns_error_if_username_is_not_valid(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber":256785687486,
            "username":"",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        #self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or not filled in")

    def test_returns_error_if_username_is_missing(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber":"256785687486",
            "username":"",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or not filled in")

    def test_returns_error_if_firstname_contains_white_space(self):
        data = {
            "firstname":"hello muga",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        print(data)
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
        	"All names must be strings and thier must be no space")


    def test_returns_error_if_lastname_contains_white_space(self):
        data = {
            "firstname":"hellomuga",
            "lastname":"Muga muha",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        #self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
        	"All names must be strings and thier must be no space")

    def test_returns_error_if_othername_contains_white_space(self):
        data = {
            "firstname":"hellomuga",
            "lastname":"Mugamuha",
            "othername":"Shidie muga",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
        	"All names must be strings and thier must be no space")

    def test_returns_error_if_username_contains_white_space(self):
        data = {
            "firstname":"hello muga",
            "lastname":"Muga muha",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"mugaba muhanad",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
        	"All names must be strings and thier must be no space")

    def test_returns_error_if_phone_number_is_not_an_integer(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": "25670759645",
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"phonenumber must be an integer")

    def test_returns_error_when_password_is_invalid(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssqwaAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
            "a password must be 8 characters and above and it must have both numbers and letters")

    def test_returns_error_when_email_is_invalid(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"mugagmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"invalid email")

    def test_returns_message_account_exists(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],"account already exists try log in")

    def test_returns_message_account_created_successfully(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],
            "your account has been created successfully")

    def test_returns_error_if_login_email_is_missing(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "login_email":"",
        "login_passw":"ssq1waAwx"
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"a field is missing")

    def test_returns_error_if_login_password_is_missing(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "login_email":"muga@gmail.com",
        "login_passw":""
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"a field is missing")

    def test_returns_error_if_login_password_is_invalid(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "email":"muga@gmail.com",
        "password":"shdhc1gh"
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
            "a password must be 8 characters and above and it must have both numbers and letters")

    def test_returns_error_if_login_password_is_invalid(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "email":"mugagmail.com",
        "password":"ssq1waAwx"
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"invalid email")

    def test_returns_error_if_normal_user_logs_in_as_admin(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "email":"muga@gmail.com",
        "password":"ssq1waAwx"
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login/admin', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,401)
        self.assertEqual(response_data['status'], 401)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"you can not login as anormal user here")

    def test_returns_error_if_admin_logs_in_as_a_normal_user(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"mu@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"Mugaba123",
            #"registered":datetime.datetime.now(),
            "is_admin":True
            }
        login_data= {
        "email":"mug@gmail.com",
        "password":"Mugaba123"
        }
        #self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code,401)
        self.assertEqual(response_data['status'], 401)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"you can not login as an admin from here")

    def test_returns_message_if_you_logged_in_successfully(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "email":"muga@gmail.com",
        "password":"ssq1waAwx"
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],"You are successfully logged in")

    def test_returns_error_if_you_logged_in_unsuccessfully(self):
        data = {
            "firstname":"hello",
            "lastname":"Muga",
            "othername":"Shidie",
            "email":"muga@gmail.com",
            "phonenumber": 25670759645,
            "username":"hfkzjsd",
            "password":"ssq1waAwx"
            }
        login_data= {
        "email":"muga@gmail.com",
        "password":"ssq2waAwx"
        }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,401)
        self.assertEqual(response_data['status'], 401)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"wrong email or password")