#!/usr/bin/env python

try:
    float(['this','is', 'a', 'list'])
except TypeError, diag:
    print 'There was an exception: %s' % str(diag)
# There was an exception: float() argument must be a string or a number


try:
    fp = open('', 'w')
except IOError, e:
    print 'There was an exception: %s' % str(e)
# There was an exception: [Errno 2] No such file or directory: ''

try:
    print foo
except NameError, e:
    print 'There was an exception: %s' % str(e)
# There was an exception: name 'foo' is not defined
