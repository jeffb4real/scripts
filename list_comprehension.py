#!/usr/bin/python

# List comprehensions

my_list = [1,2,3,4,5,6,7,8,9]
print my_list
squares = [num * num for num in my_list]
print type(squares)
print squares