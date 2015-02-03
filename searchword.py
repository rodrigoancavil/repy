"""
 search hackerrank word at start or end of text
	1 if the word is in the start.
	2 if the word is in the end.
        0 if the word is on the middle.
        -1 in otherwise.
"""
import re

N = int(raw_input())

if N >= 1 and N <= 10:
    for i in range(0,N):
        W = raw_input().lower()
        if re.match('\Ahackerrank',W) != None and re.search('hackerrank\Z',W) != None:
            print '0'
        elif re.search('\Ahackerrank',W) != None:
            print '1'
        elif re.search('hackerrank\Z',W) != None:
            print '2'
        else:
           print '-1'
