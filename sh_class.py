#!/usr/bin/env python

class Person(object):
    def __init__(self, name):
        self.name = name

class Superhero(Person):
    def __init__(self, name, hero_name):
        super(Superhero, self).__init__(name)
        self.hero_name = hero_name

me = Person('Jeff')
sh = Superhero('Wade', 'Deadpool')

print me.name
print sh.name,
print ' aka '
print sh.hero_name
