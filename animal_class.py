#!/usr/bin/env python

class Animal(object):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)

    def bark(self, msg):
        self.msg = msg
        print self.name + ' says ' + self.msg + '!'

my_cat = Cat('Buddy')
print my_cat.name
my_cat.bark('MEOW!')
print my_cat.msg
