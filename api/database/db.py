from urllib.parse import urlparse
import psycopg2
from flask import current_app as app

class Database:
	# We are creating a database for both the users and incidents, pass in urls for the respectiv 
	#configurations of the the database created called ireporter

	def __init__(self,Database_url):
		parsed_url = urlparse(Database_url)
		db = parsed_url.path[1:]
		username = parsed_url.username
		password = parsed_url.password
		hostname = parsed_url.hostname
		port = parsed_url.port
		self.conn = psycopg2.connect(database = db,user = username, 
									  password = password, host = hostname,
									  port = port)
		self.conn.autocommit= True
		self.cursor = self.conn.cursor()

	def create_tables(self):

		commands = (
			"""
				CREATE TABLE IF NOT EXISTS user_table(
				user_id SERIAL PRIMARY KEY,
				firstname VARCHAR(50) NOT NULL,
				lastname VARCHAR(50) NOT NULL,
				othername VARCHAR(50) NOT NULL,
				username VARCHAR(50) NOT NULL,
				email VARCHAR(50) NOT NULL,
				password TEXT NOT NULL,
				phonenumber bigint NOT NULL,
				registered TEXT NOT NULL,
				is_admin BOOL NOT NULL
				)""",

				"""CREATE TABLE IF NOT EXISTS incidentTable(
				incident_id SERIAL PRIMARY KEY,
				createdOn TEXT NOT NULL,
				createdBy VARCHAR(50) NOT NULL,
				record_type VARCHAR(50) NOT NULL,
				location TEXT [] NOT NULL,
				incident_image TEXT,
				comment VARCHAR(70) NOT NULL,
				status VARCHAR(50) NOT NULL
				
				)"""
			)
		for command in commands:
			self.cursor.execute(command)
	def select_all_incidents(self,record_type):
		sql = ("""SELECT * from incidentTable where record_type = '{}'""".format(record_type))
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	def select_one_record(self,table_name, criteria, input_data):
		sql = ("""SELECT * FROM {} WHERE {} = '{}'"""
				.format(table_name, criteria, input_data))
		self.cursor.execute(sql)
		return self.cursor.fetchone()
	def select_one_incident(self,table_name,criteria, input_data,record_type):
		sql = ("""SELECT * FROM {} WHERE {} = '{}' AND record_type = '{}'"""
			.format(table_name,criteria,input_data,record_type))
		self.cursor.execute(sql)
		return self.cursor.fetchone()

	def add_incident_record(self,createdOn, createdBy,record_type, location_lat,
							location_long, status, comment):
		sql = ("""INSERT INTO incidentTable(createdOn, createdBy, record_type, location,
				comment,status)
		VALUES('{}', '{}', '{}', ARRAY['{}', '{}'], '{}', '{}');"""
				.format(createdOn,createdBy,record_type,location_lat,location_long,
					status,comment))
		return self.cursor.execute(sql)

	def add_user(self,firstname,lastname,othername,username,email,password,
					phonenumber,registered,is_admin):
		sql = (""" INSERT INTO user_table(firstname,lastname,othername,username,
				email,password,phonenumber,registered,is_admin)
		VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}');"""
		.format(firstname,lastname,othername,username,email,
			password,phonenumber,registered,is_admin))
		return self.cursor.execute(sql)
	def update_incident_record(self, field_to_update, incident_id_in,input_data, record_type):
		
		sql = ("""UPDATE incidentTable SET {} = '{}' WHERE incident_id = '{}' AND record_type = '{}'"""
			.format(field_to_update, input_data, incident_id_in, record_type))
		print(field_to_update)
		return self.cursor.execute(sql)

	def update_incident_record_location(self, incident_id_in, input_data1, input_data2, record_type):
		sql = (""" UPDATE incidentTable SET location[1] = '{}',
			location[2] = '{}' WHERE 	incident_id = '{}' AND record_type = '{}'"""
			.format(input_data1, input_data2,incident_id_in,  record_type))
		return self.cursor.execute(sql)

	def delete_incident_record(self, incident_id, record_type):
		sql = (""" DELETE from incidentTable where incident_id = '{}' and record_type = '{}'"""
			.format(incident_id,record_type))
		return self.cursor.execute(sql)

	def drop_tables(self):
		command = (""" DROP TABLE user_table""", """ DROP TABLE incidentTable""")
		for comm in command:
			self.cursor.execute(comm)

def db_handler():
	database_obj = Database(app.config['DATABASE_URI'])
	return database_obj


