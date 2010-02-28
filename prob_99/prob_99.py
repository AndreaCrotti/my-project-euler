# the formula used to compare big exponential is
# a^b > c^d <-> a^(b/d) > c

# get the lines, sort them with my compare given the formula above and look for the matching line

lines = open("base_exp.txt").readlines()
s = map(lambda x: x.strip(), lines)
s = [map(int, x.split(',')) for x in s]

# just keep comparing until the end
max_el = s[0]

def couple_cmp(c1, c2):
    exp = float(c1[1]) / c2[1]
    return cmp(c1[0] ** exp, c2[0])

s.sort(cmp=couple_cmp)
res = ",".join(map(str, s[-1])) + "\r\n"
print lines.index(res) + 1
