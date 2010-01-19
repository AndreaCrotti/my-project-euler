def square_digits(i):
    res = 0
    while i > 9:
        aux = i % 10
        res += aux * aux
        i //= 10
    res += i * i
    return res

def is_89(i):
    while True:
        i = square_digits(i)
        if i == 1:
            return False
        if i == 89:
            return True

def prob_92(lim):
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
 #   print tot

def prob_92a(lim):
    from itertools import count
    tot = 0
    for i in xrange(1, lim+1):
        if is_89(i):
            tot += 1
    print tot
    
