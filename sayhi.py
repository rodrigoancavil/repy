import re

def count_words(w):
	return len(re.split('\s+',w))

N = int(raw_input())

if N >= 1 and N <= 10:
	results = []
	for i in range(0,N):
		W = raw_input()
		C = count_words(W)
		if C >= 1 and C <= 10:
			c = re.compile('^[H|h][I|i]\s{1}(?![D|d])\w+')
			if c.search(W) != None:
				results.append(W)

	for w in results:
		print w
