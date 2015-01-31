import re

ip = raw_input('Input ip : ')

"""
We have created 4 groups for each number of an ip address.
"""

result = re.match('([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})$',ip)
if result != None:
	A = int(result.group(1))
	B = int(result.group(2))
	C = int(result.group(3))
	D = int(result.group(4))
	if (A >= 0 and A <= 255) and (B >= 0 and B <= 255) and (C >= 0 and C <= 255) and (D >= 0 and D <= 255):
		print A
		print B
		print C
		print D
	else:
		print 'The ip <<%s>> is not valid'%ip
else:
	print 'The ip <<%s>> is not valid'%ip
