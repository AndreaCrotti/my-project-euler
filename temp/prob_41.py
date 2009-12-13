# a pandigital prime is a prime with all digits in

from itertools import permutations
from utils import is_prime

def prob_41():
    def inner(digits):
        perms = permutations(digits)
        # filtering and sorting can make it even slower
        #    print "filtering even"
        for idx, p in enumerate(perms):
            num = int(''.join(p))
            if is_prime(num):
                print "after %d checks found %d" % (idx, num)
                return num
        return False

    for dim in xrange(9, 2, -1):
        #print "analyzing dim = %d" % dim
        maxnum = inner(map(str, xrange(dim, 0, -1)))
        if maxnum:
            return maxnum

if __name__ == '__main__':
    prob_41()
