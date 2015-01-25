import re

N = int(raw_input())

if N>=1 and N <=100:
	for i in range(0,N):
		W = raw_input()
		fragment = re.split('<',W)
		print
		if len(fragment) > 10000:
			break
		else:
			for tag in fragment:
				print re.findall('\w+',tag)	
