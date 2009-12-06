#!/usr/bin/env/python
# -*- coding: iso-8859-15 -*-

from itertools import imap
# Very subtle use of EVAL ;)
# x = eval( '[' + open( 'names_prob22.txt' ).readlines()[ 0 ] + ']' )

fname = "names_prob22.txt"
names = imap(lambda x: x.replace('"', ''), open(fname).read().split(','))

# sort them and enumerate
enum = enumerate(sorted(names))
def val(char):
    return (ord(char) - ord('A') + 1)

def name_val(name):
    return sum([val(c) for c in name])

print sum([ (a[0]+1) * name_val(a[1]) for a in enum ])

    
    

    
