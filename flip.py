"""
 input: 1
 unsigned 32 bits for 1 is : 00000000000000000000000000000001
 flipping we get           : 11111111111111111111111111111110
 output : 4294967294 (converting the above binary to int)
"""
import string

def convert_to_int(b):
    val = 0
    p = len(b)-1
    for a in b:
        val = val + (2**p)*int(a)
        p = p - 1
    return val
   
T = int(raw_input())
if T >= 1 and  T <= 1000:
    results = []
    for i in range(0,T):
        int_number = int(raw_input())
        bin_number = string.zfill(bin(int_number)[2:],32)
        flip_number = ''
        for b in bin_number:
            if b == '1':
                flip_number = flip_number + '0'
            elif b == '0':
                flip_number = flip_number + '1'
	results.append(convert_to_int(flip_number))
for r in results:
    print int(r)
