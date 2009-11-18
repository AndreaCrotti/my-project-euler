#!/usr/bin/env/python

# smallest divisible by 1..20, doing another reverse loop

res = 1
for i in range(20,0,-1):
    if (res % i) != 0:
        res *= i
print res
