import re

N = int(raw_input())

if N >= 1 and N <= 100:
	c = re.compile('<(\s*\w+\s*)(\w+=["|\'].+["|\']\s*)*/?>(?:\[.*\]\(.*\))')
	for i in range(0,N):
		W = raw_input()
		R = c.findall(W)
		if R != None:
			print R
