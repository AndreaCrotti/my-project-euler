from itertools import count
from operator import eq

# this code is not really used now
def same_digits(mylist):
    return reduce(eq, map(lambda x: sorted(str(x))), mylist)

def same_digits2(mylist):
    "This second versions should be faster"
    m = sorted(str(mylist[0]))
    # going backward should be a bit faster
    for els in reversed(mylist[1:]):
        if sorted(str(els))!= m:
            return False
    return True

# I can remove a great part of the possible numbers
# only going from 10^k to 2*10^k

def gen_numbers():
    "only generates numbers that could possibly lead to a solution"
    for exp in count():
        for n in xrange(10 ** exp, 1.7 * (10 ** exp)):
            yield n

def prob_52():
    for i in gen_numbers():
        #print "analyze %d" % i
        s = sorted(str(i))
        found = True
        #for x in xrange(1, 7):
        for x in xrange(6, 1, -1):
            if not found:
                break
            if sorted(str(x * i)) != s:
                found = False
        # otherwise you get here
        if found:
            print i
            break
