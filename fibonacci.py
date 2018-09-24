#!/usr/bin/python

# Fibonacci sequence

a, b = 0, 1
for i in xrange(0, 10):
    print a
    a_tmp = a
    a = b
    b = a_tmp + b
    #a, b = b, a + b
    