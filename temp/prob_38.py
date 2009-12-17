from itertools import permutations, count

def is_pandig(num, dim = range(1,10)):
    s = str(num)
    return (len(s) == len(dim)) and (set(s) == set(dim))

# this appears the fastest way to do it
dim = 5
pandigs = permutations(map(str, xrange(dim-1, 0, -1)))
pan_numbers = (''.join(x) for x in pandigs)

for pan in pan_numbers:
    for idx in range(1, dim / 2):
        n = pan[:idx]
        # now we check that we can reconstruct the whole substring
        # by successively multiply this thing
        k = idx
        for i in count(2):
            if k == len(n):
                print "found a pandigital %s formed by %s" % (pan, n)
                break
            subs = str(int(n * i))
            if pan[k:].find(subs) == 0:
                print "found a substring %s in %s" % (subs, pan[k:])
                k += len(subs)
            else:
                break
                # not found or found at different positions
                
        

# other slower ways are
#########################################################################
# pands = permutations(imap(str, xrange(9, 0, -1)))                     #
# pands = permutations(str(x) for x in xrange(9, 0, -1))                #
# pands = permutations(sorted(map(str, xrange(1, 10)), reverse = True)) #
#########################################################################
