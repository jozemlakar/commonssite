class ScraperTemplate(object):
	"""
	Each of the subsystems of commons data collection (i.e. hvac, solar, veris...) is an extension of this class.
	Subclasses must define a name in __init__ and must override get_data. Writing to SQL is handled by this parent class.
	"""
	def __init__(self, name):
		self.table_name = name

	def get_name(self):
		return self.table_name

	def get_data(self):
		"""
		this is implemented by each sub class separately and should return a dict with the following format:

		data = {
			"field1" : {
				time0 : value0,
				time1 : value1,
			},
			"field2" : {
				time0 : value0,
				time1 : value1
			},
			... etc
		}
		"""
		return {} # default. should be overriden

	def write_sql(self):
		# TODO write data to the table named <self.table_name> using values in get_data
		pass