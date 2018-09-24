#!/usr/bin/env python

# https://www.packtpub.com/books/content/basics-jupyter-notebook-and-python
# When passing a parameter to a Python function, a reference to the object is actually passed (passage by assignment):

# If the passed object is mutable, it can be modified by the function
# If the passed object is immutable, it cannot be modified by the function

def add(some_list, value):
    some_list.append(value)

print 'list:'
my_list = [1, 2]
add(my_list, 3)
print my_list

print 'tuple:'
my_tup = (1, 2)
add(my_tup, 3)
print my_tup

# Traceback (most recent call last):
#   File "./pass_by_assignment.py", line 19, in <module>
#     add(my_tup, 3)
#   File "./pass_by_assignment.py", line 10, in add
#     some_list.append(value)
# AttributeError: 'tuple' object has no attribute 'append'
