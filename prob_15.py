
def quad(dim):
    if dim < 1:
        print "not possible"
        return None
    dic = {}
    # setting first values
    for i in xrange(dim):
        dic[(dim - 1, i)] = 1
        dic[(i, dim - 1)] = 1

    # going from last to first cell of the matrix
    for j in xrange(dim-2, -1, -1):
        for i in xrange(dim-2, -1, -1):
            dic[(j, i)] = dic[(j + 1, i)] + dic[(j, i + 1)]

    return dic[(0,0)]

print quad(21)
