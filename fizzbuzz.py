#!/usr/bin/python

# Fizz Buzz

for num in xrange(1, 101):

    print '%i: ' % num,

    if num % 5 == 0 and num % 3 == 0:
        print 'fizzbuzz'
    
    elif num % 3 == 0:
        print 'fizz'
    
    elif num % 5 == 0 :
        print 'buzz'

    else:
        print
