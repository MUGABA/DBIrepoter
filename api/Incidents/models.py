import datetime

class Incident:

	def __init__(self,createdBy, record_type, location, comment):
		self.createdOn = datetime.datetime.now()
		self.createdBy = createdBy
		self.record_type = record_type
		self.location = location
		self.comment = comment
		self.status = 'Draft'