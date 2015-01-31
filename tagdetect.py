import re

N = int(raw_input())

if N >= 1 and N <= 100:
	c = re.compile('<(\s*\w+)\s*(?:\w+=".+")*/?\s*>|(\[.*\]\s*\(.*\))')
	result = []
	for i in range(0,N):
		W = raw_input()
		R = c.findall(W)
		if R != None:
			for tag in R:
				if tag[0] != '' and tag[1] == '' and tag[0] not in result:
					result.append(tag[0])
				elif tag[0] == '' and tag[1].startswith('[') and 'a' not in result:
					result.append('a')

	output = ''
	for r in sorted(result):
		output = output+r+';'
	print output[0:len(output)-1]
