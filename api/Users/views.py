from api.Users import users_bp
from api.Users.controller import register_user,login_user
from flask import jsonify, make_response
from api.database.db import db_handler


@users_bp.route('/users', methods = ['POST'])
def signUp():
	return register_user()


@users_bp.route('users/login', methods = ['POST'])
def signin_normal():
	return login_user('normal_user')

@users_bp.route('/users/login/admin', methods = ['POST'])
def signin_admin():
	return login_user('admin')