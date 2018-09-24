#!/usr/bin/python

# Let's Learn Python #23 - Regular Expressions
# https://youtu.be/ZdDOauFIDkw

import re

print re.split(r'\s*', 'hello world how are you?')
print re.split(r'(\s*)', 'hello world how are you?')

print re.split(r'[a-f]', 'hello world how are you?')

var = 'jeff baker is great'
if re.search(r'jeff', var):
    print repr(var), ': ', True

m = re.search(r'jeff', var)
m.groups()
