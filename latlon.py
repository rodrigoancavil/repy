import re

N = int(raw_input())

if N >= 1 and N <= 100:
	for i in range(0,N):
		text = raw_input()
		coord = re.search('\('+
				  '\s*([+|-]?[1-9]+[0-9]*(?:\\.[0-9]+)*),'+
				  '\s*([+|-]?[1-9]+[0-9]*(?:\\.[0-9]+)*)'+
				  '\)',text)
		if coord != None:
			lat = float(coord.group(1))
			lon = float(coord.group(2))
			if (lat >= float(-90) and lat <= float(90)) and (lon >= float(-180) and lon <= float(180)):
				print 'Valid'
			else:
				print 'Invalid'
		else:
			print 'Invalid'
