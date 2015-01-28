import re

N = int(raw_input())

if N>=1 and N<=20:
	for i in range(N):
		W = raw_input()
		phone = re.search('([0-9]{1,3})[-|\s+]([0-9]{1,3})[-|\s+]([0-9]{4,10})',W)
		if phone != None:
			country = phone.group(1)
			local = phone.group(2)
			number = phone.group(3)
			print "CountryCode=%s,LocalAreaCode=%s,Number=%s"%(country, local, number) 
