#!/usr/bin/python

# OOP in python

class people_class(object):
    ''' This is the people_class '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print 'My name is', self.name
        print 'And I am %i years old' % self.age

class employee(people_class):
    ''' employee class is a subclass of people_class '''
    def __init__(self, name, age):
        super(employee, self).__init__(name, age)
        #self.var = 'hello world'

jeff = people_class('Jeff', 32)
jeff.print_info()

emp1 = employee('Larry', 32)
emp1.print_info()

