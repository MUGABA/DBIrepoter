from flask import Blueprint
from flask_cors import CORS

incident_bp = Blueprint('incident_bp',__name__)
#enabling cors for incidents
CORS(incident_bp)