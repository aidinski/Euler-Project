#!/usr/bin/python
def primeFactor(n):
    for i in range(2,n-1):
        while (n % (i) == 0):
            n = n/i
            print(i)

 
primeFactor(600851475143)
#primeFactor(100)