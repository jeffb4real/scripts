#!/usr/bin/python

import re

# case-insensitive match
# re.M is multiline
if re.search(r'eF', 'abcdef', re.I): print True
else: print False
# True

# match at end of string
if re.search(r'cd$', 'abcdabcd'): print True
else: print False
# True

# find/count occurrences
my_list = re.findall(r'cd', 'abcdabcd')
print my_list, len(my_list)
# ['cd', 'cd'] 2

# substitution
print re.sub(r'c', 'C', 'abcdecfgchic')
# abCdeCfgChiC

# split on whitespace
print (re.split(r'\s*', 'here are some words'))
# ['here', 'are', 'some', 'words']

# capture everything, split on whitespace
print (re.split(r'(\s*)', 'here are some words'))
# ['here', ' ', 'are', ' ', 'some', ' ', 'words']

# split on ranges of case-insensitive letters
print (re.split(r'[a-fA-F]', 'asduSAhwqkjelBiuhsjgjwrhgF'))
# ['', 's', 'uS', 'hwqkj', 'l', 'iuhsjgjwrhg', '']

# non-digits
print (re.split(r'\D', 'ocinwe324 main st.asdfvce'))
# ['', '', '', '', '', '', '324', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# find all
print (re.findall(r'\d+', 'ocinwe324 main st.asdf789vce'))
# ['324', '789']

# match whole address
print (re.findall(r'\d{1,5}\s\w+\s\w+\.', 'ocinwe324 main st.asdfvce'))
# ['324 main st.']
