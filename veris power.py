import httplib, base64
from settings import veris_host, veris_port, veris_uname, veris_password

error_dict = {
	1 : "Operation not permitted",
	2 : "No such file or directory",
	3 : "No such process",
	4 : "Interrupted system call",
	5 : "Input/output error",
	6 : "No such device or address",
	9 : "Bad file descriptor",
	11 : "Resource temporarily unavailable",
	12 : "Cannot allocate memory",
	13 : "Permission denied",
	16 : "Device or resource busy",
	19 : "No such device",
	23 : "Too many open files in system",
	24 : "Too many open files",
	26 : "Text file busy",
	28 : "No space left on device",
	32 : "Broken pipe",
	101 : "Network is unreachable",
	110 : "Connection timed out",
	111 : "Connection refused",
	113 : "No route to host",
	129 : "Illegal Function (function was not allowed by the slave device)",
	130 : "Illegal Data Address (the data address is not allowed by the slave device)",
	131 : "Illegal Data Value",
	132 : "Illegal Response Length",
	139 : "Device Failed to Respond (the modbus device may be off or disconnected)",
	140 : "Received invalid modbus data checksum",
	141 : "Received response from unexpected device",
	142 : "Received unsolicited query, assume another modbus master device is present.",
	143 : "Modbus device probe function received some good responses and some failures.",
	160 : "Start log (Entry in log file after AcquiSuite starts up)",
	161 : "Stop log (Entry in log file if AcquiSuite is shut down properly)",
	162 : "System time changed, caused logger to restart logging for intervals.",
	163 : "System auto-restart",
	164 : "Log entry corrupt.",
	165 : "Modbus device restart detected.",
	192 : "Modbus device does not match the device type in the configuration file.",
	193 : "Modbus device's serial number changed. (could be two devices with the same Modbus address)"
}

def get_data(channel, connection=None):
	if not connection:
		connection = httplib.HTTPConnection(veris_host, veris_port)
	header = {
		"Authorization" : "Basic %s" % base64.encodestring("%s:%s" % (veris_uname, veris_password))
	}
	req = connection.request("GET", "/setup/devicexml.cgi?ADDRESS=%d&TYPE=DATA" % channel, headers=header)
	return connection.getresponse().read()

if __name__ == '__main__':
	print get_data(3)
	print get_data(4)