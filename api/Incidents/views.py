from flask import jsonify
from api.database.db import db_handler
from api.Incidents.contraller import create_incident,get_all_incidents,\
	get_an_incident,edit_incident_location,\
	delete_incident,edit_comment_of_incident,\
	change_status_of_incident
from api.Users.utilities import check_is_admin,protected_route,\
	restrict_admin_access,restrict_normal_user_access

from api.Incidents import incident_bp
# route for creating both redflags and interventions
@incident_bp.route('/red-flags', methods = ['POST'])
@incident_bp.route('/interventions',methods = ['POST'])
@protected_route
@restrict_admin_access
def make_an_incident(current_user):
	return create_incident(current_user)

#route for getting all redflags
@incident_bp.route('/red-flags', methods = ['GET'])
@protected_route
def fetch_all_redflags(current_user):
	return get_all_incidents('red-flag')

#route for getting all interventions
@incident_bp.route('/interventions', methods= ['GET'])
@protected_route
def fetch_all_interventions(current_user):
	return get_all_incidents('intervention')

#route for getting specific redflag
@incident_bp.route('/red-flags/<int:incident_id>', methods = ['GET'])
@protected_route
def fetch_a_redflag(current_user, incident_id):
	return get_an_incident(incident_id, 'red-flag')

#route for getting specific interventions
@incident_bp.route('/interventions/<int:incident_id>', methods = ['GET'])
@protected_route
def get_an_intervention(current_user, incident_id):
	return get_an_incident(incident_id, 'intervention')

#route for editting locaton of a redflag
@incident_bp.route('/red-flags/<int:incident_id>/location', methods = ['PATCH'])
@protected_route
@restrict_admin_access
def change_redflag_location(current_user, incident_id):
	check_info = db_handler().select_one_record('incidentTable', 
			'incident_id',incident_id)
	if int(check_info[2]) != current_user[0]:
		return jsonify({
			'message':'You can edit location of an incident you did not create'})

	return edit_incident_location(incident_id, 'red-flag')

@incident_bp.route('/interventions/<int:incident_id>/location', methods = ['PATCH'])
@protected_route
@restrict_admin_access
def change_intervention_location(current_user, incident_id):
	check_info = db_handler().select_one_record('incidentTable', 
			'incident_id',incident_id)
	if int(check_info[2]) != current_user[0]:
		return jsonify({
			'message':'You can edit location of an incident you did not create'})

	return edit_incident_location(incident_id, 'intervention')

@incident_bp.route('/red-flags/<int:incident_id>/comment', methods = ['PATCH'])
@protected_route
@restrict_admin_access
def change_redflag_comment(current_user, incident_id):

	check_data = db_handler().select_one_record('incidentTable', 
			'incident_id',incident_id)
	if check_data:
		if int(check_data[2]) != current_user[0]:
			return jsonify({
				'message':'You can not edit comment of an incident you did not create'})

	return edit_comment_of_incident(incident_id, 'red-flag')


@incident_bp.route('/interventions/<int:incident_id>/comment', methods = ['PATCH'])
@protected_route
@restrict_admin_access
def change_intervention_comment(current_user, incident_id):

	check_data = db_handler().select_one_record('incidentTable', 
			'incident_id',incident_id)

	if int(check_data[2]) != current_user[0]:
		return jsonify({
			'message':'You can not edit comment of an incident you did not create'})

	return edit_comment_of_incident(incident_id, 'intervention')
#route to 
@incident_bp.route('/red-flags/<int:incident_id>', methods = ['DELETE'])
@protected_route
@restrict_admin_access
def delete_redflag(current_user,incident_id):
	delete = db_handler().select_one_record('incidentTable','incident_id',
				incident_id)
	if delete:
		if int(delete[2]) != current_user[0]:
			return jsonify({
				'message':'You can not delete an a redflag you did not create'})

	return delete_incident(incident_id, 'red-flag')

@incident_bp.route('/interventions/<int:incident_Id>', methods = ['DELETE'])
@protected_route
@restrict_admin_access
def delete_intervention(current_user, incident_Id):
	delete = db_handler().select_one_record('incidentTable','incident_id',
					incident_Id)
	if delete:
		if int(delete[2]) != current_user[0]:
			return jsonify({
				'message':'You can not delete an intervention you did not create'})

	return delete_incident(incident_Id, 'intervention')

@incident_bp.route('/red-flags/<incident_id>/status', methods=['PATCH'])
@protected_route
@restrict_normal_user_access
def change_redflag_status(current_user, incident_id):
    return change_status_of_incident(incident_id, 'red-flag')


@incident_bp.route('/interventions/<incident_id>/status', methods=['PATCH'])
@protected_route
@restrict_normal_user_access
def change_intervention_status(current_user, incident_id):
    return change_status_of_incident(incident_id, 'intervention')
