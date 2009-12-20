def get_period(n):
    def period(seq):
        "Find the period from a given sequence"
        print "checking %s" % seq
        for i in xrange(1, len(seq)):
            per = seq[:i]
            #print "check period %s" % per
            if seq[i:].find(per) == 0:
                return per
        return ""

    per = period(str(1.0 / n).split('.')[1])
    if per:
        print "period = %s" % per
    return len(per)

def prob_26(lim = 1000):
    return max(get_period(n) for n in xrange(1, lim))
