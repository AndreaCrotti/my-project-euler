# find the longest possible key from 50 succesfull login

# continue to merge substrings until you find something in common
CODES = open("../data/keylog.txt").read().splitlines()

def union(code1, code2):
    "Concatenates two string if something in common found"
    # first side
    m1, m2 = 0, 0
    max_sub = lambda c1, c2 : max([idx for idx in range(len(c1)) if c1[:idx] == c2[-idx:]])
    try:
        m1 = max_sub(code1, code2)
    except ValueError:
        try:
            m2 = max_sub(code2, code1)
        except ValueError:
            return None
        else:
            return code1 + code2[m2:]
    else:
        return code2 + code1[m1:]

temps = []
# put them in a tree

