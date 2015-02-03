"""
 inputs:
 1    # (number of lines to input)
 1 14  # (input line)
 15    # (output - the sum of 1 + 14)

 Note: solution for Python 2
"""
def solveMeSecond(a,b):
   return a+b

n = int(raw_input())
if n >=1 and n <= 1000:
    for i in range(0,n):
        a,b = str(raw_input()).split()
        a,b = int(a),int(b)
        res = solveMeSecond(a,b)
        print (res)
