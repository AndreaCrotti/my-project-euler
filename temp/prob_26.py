def get_period(n):
    def period(seq):
        "Find the period from a given sequence"
        print "checking %s" % seq
        for i in xrange(1, len(seq)):
            per = seq[:i]
            print "check period %s" % per
            print seq.find(per)
            if seq.find(per, i) == 0:
                return per
        return False

    seq = str(1.0 / n).split('.')[1]
    return period(seq)

            
