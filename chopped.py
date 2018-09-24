#!/usr/bin/python

# https://www.toptal.com//python/python-class-attributes-an-overly-thorough-guide

class Chopped(object):

    def __init__(self, some_data):
        self.data = [3,5,7]
        self.some_data = some_data

    def dump(self):
        print self.some_data

onion = Chopped('and chopped liver\n')
onion.dump()
