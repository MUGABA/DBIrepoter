from flask import jsonify,request
from api.Incidents.models import Incident
from api.Incidents.utilities import ValidateIncident
from api.database.db import db_handler

incident = ValidateIncident()

incident_records = []
inteventions_records = []

def create_incident(current_user):
	info = request.get_json()
	incident_type = info.get('incident_type')
	location = info.get('location')
	comment = info.get('comment')

	if not incident_type or not location or not comment:
		return jsonify({'status':400, 'error':'A field is missing or empty'}),400

	if not incident.validate_recordType(incident_type):
		return jsonify({
			'status':400, 
			'error':'Incident type must either be a red-flag or intervention'}),400

	if not incident.validate_comment(comment):
		return jsonify({'status': 400, 'error': 'comment must be a string'}),400

	if not incident.validate_location(location):
		return jsonify({'status': 400,
			'error': 'location must be a lat and long format'}),400

	inciden = Incident(current_user[0],incident_type,location,comment)

	db_handler().add_incident_record(inciden.createdOn, inciden.createdBy,
		inciden.record_type, inciden.location[0],inciden.location[1],
		inciden.comment,inciden.status)
	data_dict={
	"createdon": inciden.createdOn,
	"record_type": inciden.record_type,
	"incident_location": inciden.location,
	"comment": inciden.comment,
	"status": inciden.status
	}

	return jsonify({'status':201, 'data': data_dict,
					'message': f'created {incident_type} record successfully'}),201
def get_all_incidents(record_type):
	fetched_data = db_handler().select_all_incidents(record_type)
	if not fetched_data:
		return jsonify({'status':200, 'message':'No incident records yet'}),200
	keys = ["incidentid", "createdon", "createdby", "record_type","incident_location", "comment", "status"]
	incident_records = []
	for data in fetched_data:
		records = [data[0], data[1], data[2], data[3], data[4],data[6], data[7]]
		incident_records.append(dict(zip(keys, records)))
	return jsonify({'data': incident_records, 'status': 200}),200

def get_an_incident(incident_id, record_type):
	try:
		incidentId = int(incident_id)
	except:
		return jsonify({'status': 200, 'message':'incident id must be an integer'}),200

	fetched_data = db_handler().select_one_incident('incidentTable','incident_id',
										incidentId, record_type)
	if not fetched_data:
		return jsonify({'status':200, 'message':'incident is not found'}),200
	data_dict ={
            "incidentid": fetched_data[0],
                "createdon": fetched_data[1],
                "createdby": fetched_data[2],
                "record_type": fetched_data[3],
                "incident_location": fetched_data[4],
                "comment": fetched_data[6],
                "status": fetched_data[7]
            }
	return jsonify({'status': 200, 'data': data_dict}),200


def edit_incident_location(incident_id, record_type):
	data = request.get_json()
	location = data.get('location')
	try:
		incident_Id = int(incident_id)
	except:
		return jsonify({'status':400,
			'message':'incident id must be an integer'}),400

	if not location:
		return jsonify({'status':400,
			'message':'location field is empty or missing'}),400
	if not incident.validate_location(location):
		return jsonify({'status':400,
		 'error':'Location field only takes in a list of valid Lat and Long cordinates'}),400
	redflag_data_saved = db_handler().select_one_incident('incidentTable','incident_id',
							incident_Id, record_type)
	if not redflag_data_saved:
		return jsonify({'status':400,'error':'incident is not found'}),400

	if redflag_data_saved[7] != 'Draft':
		return jsonify({'status':400,
			'error':'you can not change location if the incident status is not draft'}),400
	db_handler().update_incident_record_location(incident_Id,
				location[0], location[1],record_type)
	incident_record_type = redflag_data_saved[3]
	redflag_data_saved = db_handler().select_one_incident('incidentTable','incident_id',
							incident_Id, record_type)

	data_dict = {
            "incidentid": redflag_data_saved[0],
            "createdon": redflag_data_saved[1],
            "createdby": redflag_data_saved[2],
            "record_type": redflag_data_saved[3],
            "incident_location": redflag_data_saved[4],
			'comment':redflag_data_saved[6],
			'status': redflag_data_saved[7]

	}

	return jsonify({'status':200, 'data': data_dict,
			'message':f"updated {incident_record_type} successfully"}),200

def delete_incident(incident_id, record_type):
    try:
        incident_Id=int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    delete_data = db_handler().select_one_incident('incidentTable', 'incident_id',
                                                 incident_Id, record_type)
    if not delete_data:
        return jsonify({'status': 200,
                        'message': 'incident record not found'}), 200
    db_handler().delete_incident_record(incident_Id, record_type)
    return jsonify({'status': 200,
                    'message': f"{delete_data[3]} record has been deleted"}), 200

# function for editing the comment of an incident
def edit_comment_of_incident(incident_id, record_type):
    info=request.get_json()
    comment=info.get('comment')
    #print(info)
    print(incident.validate_comment(comment))
    try:
        incident_Id=int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    if not comment:
        return jsonify({'status': 400,
                        'error': 'comment field is empty or missing'
                        }), 400
    if not incident.validate_comment(comment):
        return jsonify({'status': 400,
                        'error': 'comment must be a string'}), 400
    incident_result = db_handler().select_one_incident('incidentTable', 'incident_id',
    							int(incident_Id), record_type)
    #print(incident_result[6])
    if not incident_result:
        return jsonify({'status': 200,
                'message': 'incident record not found'}), 200
    if incident_result[7] != 'Draft':
        return jsonify({'status': 400,
                        'error': 'You cannot change the comment while the incident status is not Draft'}), 400
    db_handler().update_incident_record('comment', incident_Id, comment, record_type)
    returned_type=incident_result[3]
    incident_result=db_handler().select_one_incident('incidentTable', 'incident_id',
                                                  incident_Id, record_type)
    
    redflag_dict={
            "incidentid": incident_result[0],
            "createdon": incident_result[1],
            "createdby": incident_result[2],
            "record_type": incident_result[3],
            "incident_location": incident_result[4],
            "comment": incident_result[6],
            "status": incident_result[7]
            }
    print(redflag_dict)
    return jsonify({'status': 200, 'data': redflag_dict,
                'message': f"Updated {returned_type} record's comment"}), 200


def change_status_of_incident(incident_id, record_type):
	info = request.get_json()
	status = info.get('status')

	try:
		incident_Id = int(incident_id)
	except:
		return jsonify({'status':400,
			'error':'incident is must be a valid integer'}),400

	if not status:
		return jsonify({'status':400,
				'error':'status field is missing or not found'}),400

	if not incident.validate_status(status):
		return jsonify({'status':400, 'error':'status must be s string'}),400
	incident_to_update = db_handler().select_one_incident('incidentTable',
					'incident_id',incident_Id, record_type)
	if not incident_to_update:
		return jsonify({'status':200,
			'error': 'incident not found'}),200
	db_handler().update_incident_record('status',incident_Id,
				status, record_type)
	incident_to_update = db_handler().select_one_incident('incidentTable',
				'incident_id',incident_Id, record_type)
	incident_to = incident_to_update[3]

	data_dict = {
	'incidentId':incident_to_update[0],
	'createdon':incident_to_update[1],
	'createdby':incident_to_update[2],
	'record_type':incident_to_update[3],
	'location':incident_to_update[4],
	'comment':incident_to_update[6],
	'status':incident_to_update[7]
	}
	return jsonify({'status':200,
		'data': data_dict,
		'message':f"updated {incident_to} status"}),200








