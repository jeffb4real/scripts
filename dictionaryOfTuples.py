#!/usr/bin/env python

ng = {}
ng[(1,2,4)] = 8
ng[(4,2,1)] = 10
ng[(1,2)] = 12

sum = 0
for k in ng:
    sum += ng[k]

print len(ng) + sum

# output: this is a dictionary of tuples
# 33
