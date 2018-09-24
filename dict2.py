#!/usr/bin/env python

d = {}
d['a'] = {'ra':7, 'dec':8}
d['b'] = {'ra':3, 'dec':5}
d['a']['dist'] = 12

print d
print

for key in d:
    print 'key: {}\nvalue: {}'.format(key, d[key])
    print

print "d['a'].update({'dist':10})"
d['a'].update({'dist':10})

for key in d:
    print 'key: {}\nvalue: {}'.format(key, d[key])
    print

print "d['a'].pop('dec')"
d['a'].pop('dec')

for key in d:
    print 'key: {}\nvalue: {}'.format(key, d[key])
    print

print "del d['b']"
del d['b']

for key in d:
    print 'key: {}\nvalue: {}'.format(key, d[key])
    print
