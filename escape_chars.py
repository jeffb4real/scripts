#!/usr/bin/python

import time

# https://learnpythonthehardway.org/book/ex10.html

print "\n"
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
        time.sleep (1)

