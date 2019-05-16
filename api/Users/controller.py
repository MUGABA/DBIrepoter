from flask import jsonify, request,json,abort
from api.Users.models import User
from api.Users.utilities import validateUser,encode_token
import datetime
from validate_email import validate_email
from api.database.db import db_handler
from werkzeug.security import generate_password_hash, check_password_hash

def register_user():
	data = request.get_json()
	firstname = data.get('firstname')
	lastname = data.get('lastname')
	othername = data.get('othername')
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	phonenumber = data.get('phonenumber')
	if not firstname or not lastname or not othername or not username \
	or not email or not password or not phonenumber:
		return jsonify({'status':400, 'error':'A field is missing or not filled in'}),400

	if not validateUser.validate_name(firstname) or not validateUser.validate_name(lastname) \
	or not validateUser.validate_name(othername) or not validateUser.validate_name(username):
		return jsonify({'status':400,
			'error':'All names must be strings and thier must be no space'}),400

	if not validateUser.validate_number(phonenumber):
		return jsonify({'status':400, 'error':'phonenumber must be an integer'}),400

	if not validateUser.validate_password(password):
		return jsonify({'status':400,
			'error':'a password must be 8 characters and above and it must have both numbers and letters'}),400

	if not validate_email(email):
		return jsonify({'status': 400, 'error':'invalid email'}),400
	
	
	new_user = User(firstname,lastname,othername,username,email, 
						generate_password_hash(password),phonenumber)
	if db_handler().select_one_record('user_table','email',email):
		return jsonify({'status':200, 'message':'account already exists try log in'}),200
	# db_handler().add_user('Busolo','Emma','Amos','EmmaAmos','emma@gmail.com'
	# 			,generate_password_hash('EmmaAmos123'),25670364,datetime.datetime.now(),True)

	new_user = db_handler().add_user(new_user.firstname, new_user.lastname, new_user.othername,
							 new_user.username, new_user.email, new_user.password, new_user.phonenumber, 
							 new_user.registered, new_user.is_admin)
	data.pop('password')
	return jsonify({'status':201, 'message': 'your account has been created successfully'}),201



def login_user(user_type):
	login_info = request.get_json()
	login_email = login_info.get('email')
	login_pass =  login_info.get('password')

	if not login_email or not login_email:
		return jsonify({'status':400, 'error':'a field is missing'}),400

	if not validateUser.validate_password(login_pass):
		return jsonify({'status':400,
			'error':'a password must be 8 characters and above and it must have both numbers and letters'}),400
	if not validate_email(login_email):
		return jsonify({'status':400, 'error':'invalid email'}),400

	user_data = db_handler().select_one_record('user_table', 'email', login_email)

	if user_data:
		if user_type == 'admin':
			if user_data[9] is False:
				return jsonify({'status':401, 'error': 'you can not login as anormal user here'}),401

		if user_type == 'normal_user':
			if user_data[9] is True:
				return jsonify({'status':401, 'error': 'you can not login as an admin from here'}),401
		if user_data[5] == login_email and check_password_hash(user_data[6],login_pass):
			access_token = encode_token(login_email)
			return jsonify({'status':200, 'access_token': access_token.decode('UTF-8'),
							 'message':'You are successfully logged in'}),200

	return jsonify({'status':401, 'error': 'wrong email or password'}),401




	

