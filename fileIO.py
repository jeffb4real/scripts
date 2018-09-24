#!/usr/bin/python

import re

print '*'*40

# open; strip \n
fp = open('ipadd.txt', 'r')
for line in fp.readlines():
    print line.strip()
fp.close()

print '*'*40
# open and print
fp = open('ipadd.txt', 'r')
for line in fp.readlines():
    print line,
fp.close()

# slurp entire file into memory
fp = open('ipadd.txt', 'r')
data = fp.readlines()
fp.close()

# write file out with changes
fp = open('ipadd_new.txt', 'w')
fp.writelines(data)
fp.close

print '*'*40
data = ['blue', (1, 4, 'text', 6), 3, 'a', 'abc', ['d','e','f'], 'ghi', {'color': 'red', 'girl': 'blonde'}]
with open('ipadd2.txt', 'w') as fp:
    for d in data:
        print type(d)
        print d
        # string, int, tuple, list, dict: all can be converted to string!
        fp.write(str(d) + '\n')
