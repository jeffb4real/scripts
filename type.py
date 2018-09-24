#!/usr/bin/env python

a = 5
if type(a) is int:
    print 'a = {} and it is an int'.format(a)
else:
    print 'a = {} and it is not an int'.format(a)

a = '5'
if type(a) is int:
    print 'a = {} and it is an int'.format(a)
else:
    print 'a = {} and it is not an int'.format(a)

a = int(a) + 2
if type(a) is int:
    print 'a = {} and it is an int'.format(a)
else:
    print 'a = {} and it is not an int'.format(a)




