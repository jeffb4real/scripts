#!/usr/bin/python
import os
from subprocess import Popen, PIPE

exclude=[]
for a in os.listdir('.'):
    process = Popen(['grep', '-n', 'usr', '%s' % a], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stdout:
        print a
        print stdout
        print '-------'
    else:
        exclude.append(a)

if exclude:
    print 'excluded files: '
    for f in exclude:
        print f