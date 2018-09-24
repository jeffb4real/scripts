#!/usr/bin/python

var = (1, 2, 3)

try:
    assert var[2]
    assert var[5]
except IndexError:
    print 'Houston, we have IndexError!'


