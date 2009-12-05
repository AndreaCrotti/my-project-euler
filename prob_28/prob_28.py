from itertools import cycle, count, izip
#  four possible directions
#  right, down, left, up
r = (0, 1)
d = (1, 0)
l = (0, -1)
u = (-1, 0)

dimension = 1001
directions = cycle([r, d, l, u])
# good idea to allocate the whole matrix?

def next_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def gen_seq(init, dim):
    "Generates a sequence of repeating numbers"
    for i in count(init):
        for j in range(dim):
            yield i

movement = izip(gen_seq(1, 2), directions)

def gen_matrix(dim):
    matrix = [[-1]*dim for x in range(dim)]

    # starting point of the spiral, coordinates are given in tuples (x, y)
    cx, cy = [len(matrix) / 2] * 2
    pos = (cx, cy)
    value = 1
    done = False
    for c, mov in movement:
        if done:
            break
        for x in xrange(c):
            try:
                matrix[pos[0]][pos[1]] = value
            except IndexError:
                print "reaching the end of the matrix"
                done = True
                break
            value += 1
            pos = next_pos(pos, mov)
        # the direction is changed only here
    return matrix

def diag_sum(mat):
    right = sum(mat[x][x] for x in xrange(len(mat)))
    left = sum(mat[len(mat)-1-x][x] for x in xrange(len(mat)))
    return left + right

# -1 is to remove the 1 in the middle that would be counted twice (even matrix)
print diag_sum(gen_matrix(dimension))
