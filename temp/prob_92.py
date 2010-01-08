def square_digits(i):
    res = 0
    while i > 9:
        aux = i % 10
        res += aux * aux
        i //= 10
    res += i * i
    return res

def prob_92(lim = 10 * 1000 * 1000):
    tot = 0
    # checking over a set is much faster
    set1 = set([])
    set89 = set([])
    for x in xrange(1, lim):
        #print "checking %d" % x
        val = x
        chain = [val]
        while True:
 #           print "chain = %s" % str(chain)
            # the cheapest operation goes first
            if val == 1 or val in set1:
               set1 = set1.union(chain)
               #print "stopping after %d steps" % len(chain)
               break

            if val == 89 or val in set89:
                set89 = set89.union(chain)
                #print "stopping after %d steps" % len(chain)
                tot += 1
                break

            val = square_digits(val)
            #val = sum(int(x)**2 for x in str(val))
            chain.append(val)

    #print set89
    print tot
