#!/usr/bin/python

# How does regex work in Python??


import os, sys, re

result = []
p = re.compile('abc|123')
#p = re.compile('abc')
names = ['jabceff', 'j123eff', 'baker', 'ABC']
for name in names:
    print name
    if p.search(name):
        result.append(name)

print '--------'
print result

# output:
# -------
# jabceff
# j123eff
# baker
# ABC
# ['jabceff']