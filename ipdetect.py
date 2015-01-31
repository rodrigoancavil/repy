import re

def detect_ip(w):
	ipv4_pattern = re.match('(^[1-2][0-9]{0,2})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})$',w) 
	if ipv4_pattern != None:
		a = int(ipv4_pattern.group(1))
		b = int(ipv4_pattern.group(2))
		c = int(ipv4_pattern.group(3))
		d = int(ipv4_pattern.group(4))
		if (a >= 0 and a <= 255) and (b >= 0 and b <= 255) and (c >= 0 and c <= 255) and (d >= 0 and d <= 255):
			return 'IPv4'
		else:
			return 'Neither'
	elif re.match('[0-9A-Fa-f]{1,4}:[0-9A-Fa-z]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9A-Fa-f]{1,4}$',w) != None:
		return 'IPv6'
	else:
		return 'Neither'

N = int(raw_input())
if N >= 1 and N <= 50:
	results = []
	for i in range(0,N):
		ip = raw_input()
		results.append(detect_ip(ip))
	for r in results:
		print r
