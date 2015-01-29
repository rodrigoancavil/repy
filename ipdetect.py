import re

def detect_ipv4(w):
	if re.match('^[1-9][0-9]{0,2}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}',w) != None:
		print 'IPv4'

ip = raw_input()

detect_ipv4(ip)
