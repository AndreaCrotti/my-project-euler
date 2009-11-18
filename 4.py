#!/usr/bin/env/python

# Find largest palindrome made from the product of two 3-digit numbers

# doing a reverse cycle, from 999 and back

def is_palindrom(n):
    " Check is a number is palindrom"
    if list(str(n)) == list(reversed(str(n))):
        return True
    return False


adders = [999, 999]
idx = 0

while True:
    #print "adders now %d %d" % (adders[0], adders[1])
    prod = adders[0] * adders[1]
    if is_palindrom(prod):
        print prod
        break
    
    adders[idx] -= 1
    idx = (idx + 1) % 2
        
