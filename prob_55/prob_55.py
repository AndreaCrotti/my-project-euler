# A Lychrel number is one that doesn't form a palyndrom in less than 50 operations

def is_pal(x):
    "True if number is palyndrom"
    s = str(x)
    return s[::-1] == s

def is_lych(x):
    i = 0
    while i < 50:
        # discarding x, we need at least 1 iteration
        x += int(str(x)[::-1])
        if is_pal(x):
            return False
        i += 1

    return True

def prob_55(limit = 10000):
    lych_numbers = [ x for x in xrange(limit) if is_lych(x) ]
    print len(lych_numbers)
