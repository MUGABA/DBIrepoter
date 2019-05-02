from api.Users.models import User
from api.database.db import db_handler
from flask import request, jsonify, current_app as app 
from functools import wraps
import jwt
import re
import datetime


class validateUser:

	@staticmethod
	def validate_name(name):
		#this validates the names input by the user
		return isinstance(name, str) and not re.search(r'[\s]', name)

	@staticmethod
	def validate_number(numb):
		return isinstance(numb,int)

	@staticmethod
	def validate_password(password):
		return isinstance(password,str) and len(password)>=8 and re.search(r'[0-9]',password) \
		and re.search(r'[a-z]',password)
#This is check whether the user is an admin
def check_is_admin(current_user):
	return current_user[9] is True
	# current_user = db_handler().select_one_record('user_table', 'is_admin', is_admin)
	# if current_user == True:
	# 	return current_user


def encode_token(email):

	try:
		payload = {
		#Expirely time of the token
		'exp': datetime.datetime.utcnow() + datetime.timedelta(hours= 24),
		#Time at which the token is isseud
		'iat': datetime.datetime.utcnow(),
		#the token will be issued on the email validattion
		'sub': email
		}
		return jwt.encode(payload, app.config['SECRET'],algorithm='HS256')

	except Exception as e:
		return e

def protected_route(f):

	@wraps(f)
	def inner_func(*args,**kwargs):
		token = None
		if 'Authorization' in request.headers:
			token = request.headers['Authorization']
		if not token:
			return jsonify({'status':401,'error': 'token is invalid or missing'}),401
		try:
			data = jwt.decode(token,app.config['SECRET'], algorithms = ['HS256'])
			current_user = db_handler().select_one_record('user_table', 'email', data['sub'])
		except jwt.ExpiredSignatureError:
			return jsonify({'status': 401,'error':'The token has expired please login again'}),401

		except jwt.InvalidTokenError:
			return jsonify({'status': 401,'error' : 'Invalid token. please login again'})

		return f(current_user, *args, **kwargs)
	return inner_func


def restrict_admin_access(f):
    """ 
    Decorator fuction restricts an admin from accessing
    endpoints that are only to be used by normal users
    """
    @wraps(f)
    def restrict_access(*args, **kwargs):
        if check_is_admin(args[0]):
            return jsonify({'status': 403,
                            'error': 'You do not have permission to perform this action'
                            }), 403
        return f(*args,**kwargs)
    return restrict_access


def restrict_normal_user_access(function):
    """
    Restrict normal user from accessing endpoints that require
    admin previledges
    """
    @wraps(function)
    def restrict_normal_user(*args, **kwargs):
        if not check_is_admin(args[0]):
            return jsonify({'status': 403,
                            'error': 'You do not have permission to perform this action'
                            }), 403
        return function(*args,**kwargs)
    return restrict_normal_user
