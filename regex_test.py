#!/usr/bin/python
import os
import sys
from sys import version_info
import time
import re

# Function decorators

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
    	print
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

def do_stuff():
	return "{0}"

my_person = Person()
my_person.name = 'Jerry'

#print my_person.get_fullname()
#print
#print do_stuff()

py3 = version_info[0] > 2 # Creates boolean value for test that Python major version > 2
print py3 == 0,
print
if py3:
  sometext = str(input('Please enter some text: '))
else:
  sometext = str(raw_input('Please enter some text: '))
print 'Hello, {}!'.format(sometext)
#print int(sometext)*int(sometext)

foo=3
bar='help'
print foo
print bar
print

x='there are %d types of people in the world' % 10
print x

sys.exit()
#re.match(var, 'hell')
#print match.group(0)
#print match.group(1)
#print match.group(2)

# OOPS: inheritance, polymorphism (compile time: overloading; run time: override), encapsulation, abstraction)

# JAVA: == is comparison operator, compares reference/address; .equal compares the contents, e.g. string vs. string

