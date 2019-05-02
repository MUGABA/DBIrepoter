class ValidateIncident:

	@staticmethod
	def validate_recordType(record_type):
		# validating record type
		return isinstance(record_type, str) and record_type == 'red-flag' or \
				record_type == 'intervention'

	@staticmethod
	def validate_comment(comment):
		return isinstance(comment, str)

	@staticmethod
	def validate_status(status):
		#validating status of the incident done by the admin
		return isinstance(status, str) and status == 'under investigation' or \
				status == 'rejected' or status == 'resolved'

	@staticmethod
	def validate_image_and_videos(image_or_video):

		title_key = 'title'
		url_key = 'url'
		store_keys = []
		store_values = []

		for keys, values in image_or_video.item():
			store_keys.append(keys)
			store_values.append(values)
		return title_key in store_keys and url_key in store_keys and \
				isinstance(store_keys[0], str) and \
				isinstance(store_keys[1], str)

	@staticmethod
	def validate_location(location):

		return isinstance(location, list) and len(location) == 2 and \
			isinstance(location[0], float) and isinstance(location[1], float)
