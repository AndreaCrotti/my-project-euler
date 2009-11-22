#!/usr/bin/env/python

# Very subtle use of EVAL ;)
# x = eval( '[' + open( 'names_prob22.txt' ).readlines()[ 0 ] + ']' )

fname = "names_prob22.txt"
names = open(fname).read()
names = map(lambda x: x.replace('"', ''), names.split(','))

# sort them and enumerate
enum = enumerate(sorted(names))
def val(char): return (ord(char) - ord('A') + 1)
def name_val(name): return sum([val(c) for c in name])

print sum([ (a[0]+1) * name_val(a[1]) for a in enum ])
