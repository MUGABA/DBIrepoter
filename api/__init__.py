from flask import Flask 
from api.Users.views import users_bp
from Instance.config import app_config
from api.Incidents.views import incident_bp


def create_app(config_name):
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py', 'r')
	# registering blueprints
	app.register_blueprint(incident_bp, url_prefix = '/api/v1')
	app.register_blueprint(users_bp, url_prefix= '/api/v1')
	return app
