from tests.base import BaseTest
from api.Incidents import views
import json

class TestIncidentsEndPoints(BaseTest):
    def test_returns_error_if_the_record_type_redflag_is_empty(self):
        data = {
                "incident_type":"",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or empty")

    def test_returns_error_if_the_record_type_for_intevention_is_empty(self):
        data = {
                "incident_type":"",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or empty")

    def test_returns_error_if_the_location_redflag_is_empty(self):
        data = {
                "incident_type":"red-flag",
                "location":[],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or empty")

    def test_returns_error_if_the_location_for_intevention_is_empty(self):
        data = {
                "incident_type":"intervention",
                "location":[],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or empty")

    def test_returns_error_if_the_comment_redflag_is_empty(self):
        data = {
                "incident_type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": "",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or empty")

    def test_returns_error_if_the_comment_for_intevention_is_empty(self):
        data = {
                "incident_type":"intervention",
                "location":[3333.33, 444.1],
                "comment": "",
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A field is missing or empty")

    def test_returns_error_if_the_record_typeRedflag_is_invalid(self):
        data = {
                "incident_type":"redflag",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
            "Incident type must either be a red-flag or intervention")

    def test_returns_error_if_the_record_typeIntervention_is_invalid(self):
        data = {
                "incident_type":"entervention",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
            "Incident type must either be a red-flag or intervention")

    def test_returns_error_if_the_commentRedflag_is_invalid(self):
        data = {
                "incident_type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": 23456
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"comment must be a string")

    def test_returns_error_if_the_commentIntervention_is_invalid(self):
        data = {
                "incident_type":"intervention",
                "location":[3333.33, 444.1],
                "comment": 2345
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"comment must be a string")

    def test_returns_error_if_the_locationRedflag_is_invalid(self):
        data = {
                "incident_type":"red-flag",
                "location":'Hey',
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
            "location must be a lat and long format")

    def test_returns_error_if_the_locationIntervention_is_invalid(self):
        data = {
                "incident_type":"intervention",
                "location":'hello',
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
            "location must be a lat and long format")

    def test_returns_message_when_Redflag_is_created(self):
        data = {
                "incident_type":"red-flag",
                "location":[23.45,567.87],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],
            "created red-flag record successfully")

    def test_returns_message_when_Intervention_is_created(self):
        data = {
                "incident_type":"intervention",
                "location":[234.02,34.556],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],
            "created intervention record successfully")

    def test_returns_message_when_no_redflags_created_yet(self):
        data = {
                "incident_type":"red-flag",
                "location":[23.45,567.87],
                "comment": "its terrible",
                }
        res = self.app.get('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],
            "No incident records yet")

    def test_returns_message_when_no_Intervention_is_created_yet(self):
        data = {
                "incident_type":"intervention",
                "location":[234.02,34.556],
                "comment": "its terrible",
                }
        res = self.app.get('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],
            "No incident records yet")

    def test_returns_message_when_redflags_are_returned_in_list(self):
        data = {
                "incident_type":"red-flag",
                "location":[23.45,567.87],
                "comment": "its terrible",
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("its terrible", str(response_data['data']))

    def test_returns_message_when__Interventions_are_returned_in_list(self): 
        data = {
                "incident_type":"intervention",
                "location":[234.02,34.556],
                "comment": "its terrible",
                }
        self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("its terrible", str(response_data['data']))

    def test_returns_message_when_specific_redflag_is_returned_(self):
        data = {
                "incident_type":"red-flag",
                "location":[23.45,567.87],
                "comment": "its terrible",
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/red-flags/1', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("its terrible", str(response_data['data']))

    def test_returns_message_when_specific_Intervention_is_returned_(self): 
        data = {
                "incident_type":"intervention",
                "location":[234.02,34.556],
                "comment": "its terrible",
                }
        self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/interventions/1', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("its terrible", str(response_data['data']))

    def test_returns_message_when_specific_redflag_is_not_available(self):
        data = {
                "incident_type":"red-flag",
                "location":[23.45,567.87],
                "comment": "its terrible",
                }
        # self.app.post('/api/v1/red-flags', content_type="application/json",
        #     data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/red-flags/1', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],'incident is not found')

    def test_returns_message_when_specific_Intervention_is_not_available(self): 
        data = {
                "incident_type":"intervention",
                "location":[234.02,34.556],
                "comment": "its terrible",
                }
        # self.app.post('/api/v1/interventions', content_type="application/json",
        #     data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/interventions/1', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'],'incident is not found')

    def test_edits_redflag_location(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "location": [3.333, 33.3]
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/red-flags/1/location', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("updated red-flag successfully", response_data['message'])

    def test_edits_intervention_location(self):
        data = {
            "incident_type":"intervention",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "location": [33.333, 33.3]
                }
        self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/interventions/1/location', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("updated intervention successfully", response_data['message'])

    def test_edits_redflag_comment(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "comment": "corruption is rumpunt"
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/red-flags/1/comment', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("Updated red-flag record's comment", response_data['message'])

    def test_edits_intervention_comment(self):
        data = {
            "incident_type":"intervention",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "comment":"potholes are now solved but corruption"
                }
        self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/interventions/1/comment', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("Updated intervention record's comment", response_data['message'])

    def test_edits_redflag_status(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "status": "Resolved"
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/red-flags/1/status', content_type="application/json",
         data=json.dumps(data2), headers = self.admin_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("updated red-flag status", response_data['message'])

    def test_edits_intervention_status(self):
        data = {
            "incident_type":"intervention",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "status":"Resolved"
                }
        self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/interventions/1/status', content_type="application/json",
         data=json.dumps(data2), headers = self.admin_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("updated intervention status", response_data['message'])


    def test_deletes_redflag_(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.delete('/api/v1/red-flags/1', content_type="application/json",
         data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("red-flag record has been deleted", response_data['message'])

    def test_deletes_intervention(self):
        data = {
            "incident_type":"intervention",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        self.app.post('/api/v1/interventions', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.delete('/api/v1/interventions/1', content_type="application/json",
         data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        print(response_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("intervention record has been deleted", response_data['message'])