#!/usr/bin/env python

# Print out names in modules
# https://docs.python.org/2/py-modindex.html
import os, sys, re, subprocess, platform, shutil, argparse, test, xml, time, urllib2, getopt
import importlib

# From Django tutorial05
from django.test import TestCase

def print_modules(module_list):
    for mod in module_list:
        print '------------'
        print mod
        print '------------'
        module = importlib.import_module(mod, package=None)
        print str(dir(module)).replace("'", '')
        print

# Print string names
print '------------'
print 'String'
print '------------'
print str(dir('abc')).replace("'", '')
print

# Print list names
print '------------'
print 'List'
print '------------'
print str(dir([1,2,3])).replace("'", '')
print

# Print list names
print '------------'
print 'os.path'
print '------------'
print str(dir(os.path)).replace("'", '')
print

# Use split() on a string to create a list (the lazy way!)
module_list = 'os sys re subprocess platform shutil argparse test xml time urllib2 getopt'.split()
print_modules (module_list)
#print_modules('TestCase')
