from settings import veris_host, veris_port, veris_uname, veris_password

# import xml parsing in a version-independent way
try:
	from lxml import etree
	print("running with lxml.etree")
except ImportError:
	try:
		# Python 2.5
		import xml.etree.cElementTree as etree
		print("running with cElementTree on Python 2.5+")
	except ImportError:
		try:
			# Python 2.5
			import xml.etree.ElementTree as etree
			print("running with ElementTree on Python 2.5+")
		except ImportError:
			try:
				# normal cElementTree install
				import cElementTree as etree
				print("running with cElementTree")
			except ImportError:
				try:
					# normal ElementTree install
					import elementtree.ElementTree as etree
					print("running with ElementTree")
				except ImportError:
					print("Failed to import ElementTree from any known place")

def get_data(channel):
	full_url = "http://%s:%d/setup/devicexml.cgi?ADDRESS=%d&TYPE=DATA" % (veris_host, veri_port, channel)
	req = requests.get(full_url, auth=(veris_uname, veris_password))
	return req.text

if __name__ == '__main__':
	xml_obj_1 = etree.fromstring(get_data(3))
	xml_obj_2 = etree.fromstring(get_data(4))
	print etree.tostring(xml_obj_1, pretty_print=True)
	# TODO parse fully into dict
	print xml_obj_1.find('./devices/device/name').text,
	print xml_obj_1.find('./devices/device/status').text,
	print xml_obj_1.find('./devices/device/records/record/time').text