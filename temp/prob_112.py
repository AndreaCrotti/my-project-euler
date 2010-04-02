#!/usr/bin/env python

def is_bouncy(num):
    s = str(num)
    seq = zip(s[:-1], s[1:])
    sign = 0
    for x, y in seq:
        if x != y:
            nsign = cmp(x,y)
            if sign != 0 and nsign != sign:
                return True
            else:
                sign = nsign

    return False
        
def count(start, end):
    return len(filter(is_bouncy, range(start, end+1)))

def prob_112():
    high = None
    low = num = 21780

    percent = lambda x, y: (float(x) / y) * 100
    counted = count(0, num)
    print counted

    assert(percent(count(0, 21780), 21780) == 90.0)

    while True:
        p = percent(counted, num)
        print num, counted, p

        # very stupid approach but the tree was not working
        if p < 99.0:
            num += 1
            if is_bouncy(num):
                counted += 1

    return num
       
print prob_112()
