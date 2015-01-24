import re

def parse_tweet(tweet):
	return bool(re.search('hackerrank',tweet.lower()))

N = int(raw_input())

if N >= 1 and N <= 10:
	count = 0
	for i in range(0,N):
		tweet = raw_input()
		if parse_tweet(tweet):
			count += 1

	print count
