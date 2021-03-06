from itertools import permutations, count

def prob_38(dim = 10):
    pandigs = permutations(map(str, xrange(dim-1, 0, -1)))
    # this appears the fastest way to do it
    pan_numbers = (''.join(x) for x in pandigs)
    for n in pan_numbers:
        #print "checking ", n
        if is_constructable(n):
            return n

def is_constructable(n):
    s = str(n)
    for k in xrange(1, len(s) / 2 -1):
        num = int(s[:k])
        #print "setting n to ", num
        idx = k
        for counter in count(2):
            # exiting when the whole num is visited
            if idx == len(s):
                #print "number is constructable with n %d ,reaching index %d = " %(num, idx)
                return True

            st = s[idx:]
            mul = str(num * counter)
            found = st.find(mul)
            #print "sub = %s, mul = %s" % (st, mul)
            # check if we are out of boundaries
            if len(mul) > len(st):
                break

            if found == 0:
                #print "found a substring %s in %s" % (mul, st)
                idx += len(mul)
            else:
                break

def is_constructable_num(n):
    "numerical way, needs maybe also logarithms in this case"
    from math import log, floor

    get_dim = lambda x: int(floor(log(x, 10)))
    dim = get_dim(n)
    for l in xrange(dim, dim / 2, -1):
        divis = 10 ** l
        num = n / divis
        # get the new number with the % operator
        #newnum = 
        num_len = get_dim(num)
        
        for idx in count(2):
            mul = num * idx * divis
            # find with the logarithm the right value
        # check if we are able to construct the number

# other slower ways are
#########################################################################
# pands = permutations(imap(str, xrange(9, 0, -1)))                     #
# pands = permutations(str(x) for x in xrange(9, 0, -1))                #
# pands = permutations(sorted(map(str, xrange(1, 10)), reverse = True)) #
#########################################################################
