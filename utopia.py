import re

pattern = '[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}'

N = int(raw_input())

if N >= 1 and N <= 100:
	results = []
	for i in range(0,N):
		wid = raw_input()
		if re.match(pattern, wid) != None:
			results.append('VALID')
		else:
			results.append('INVALID')

	for r in results:
		print r
		
			
