from flask import Blueprint
from flask_cors import CORS 
#creating blueprint for users
users_bp = Blueprint('users_bp', __name__)
#enabling cors for the users
CORS(users_bp)
