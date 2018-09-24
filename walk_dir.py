#!/usr/bin/python

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('.'):
    for a in f.extend(filenames): print a
    