#!/usr/bin/env python

# List - extend() vs append()

one = ['abc', 123, 'efg']
two = [3, 5, 'xyz']

# use extend() to merge two lists
one.extend(two)
print one
# ['abc', 123, 'efg', 3, 5, 'xyz']
print two
# [3, 5, 'xyz']

# use append() to add a single item to a list (even if that single item is a list!)
two.append(one)
print two
# [3, 5, 'xyz', ['abc', 123, 'efg', 3, 5, 'xyz']]
