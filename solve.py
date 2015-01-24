def solveMeSecond(a,b):
   return a+b

n = int(input())
if n >=1 and n <= 1000:
    for i in range(0,n):
        a, b = str(input()).split('+')
        a,b = int(a),int(b)
        res = solveMeSecond(a,b)
        print (res)
