import re

c = re.compile('([a-zA-Z]{2,})://([a-zA-Z0-9]+)(?:\:([0-9]{2,}))?/?')

url = raw_input('Input a url : ')

result = c.search(url)

if result != None:
	print result.group(1)
	print result.group(2)
	print result.group(3)
else:
	print 'Invalid URL <<%s>>'%url
