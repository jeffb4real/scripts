#!/usr/bin/python
# https://pymotw.com/2/glob/

import glob

myfiles = glob.glob('./*.py')
print 'Files that end in .py\n---------------------'
for eachfile in myfiles:
	print eachfile
print

myfiles = glob.iglob('./*.py')
print myfiles[0]
exit()
print 'Files that end in .py\n---------------------'
for ifile in myfiles:
	print ifile
print

