import re

N = int(raw_input())

if N >= 1 and N <= 10:
    for i in range(0,N):
        W = raw_input().lower()
        if re.match('\w+(?<=hackerrank)',W) != None:
            print '1'
        elif re.search('\w+\s*(hackerrank)$',W) != None:
            print '2'
