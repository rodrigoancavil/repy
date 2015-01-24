import re

def validate_PAN(pan):
	c = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')
        if bool(c.search(pan)):
        	return 'YES'
        else:
		return 'NO'

N = int(raw_input())

if N >= 1 and N <= 10:
	for i in range(0,N):
		pan = raw_input()
		print validate_PAN(pan)

