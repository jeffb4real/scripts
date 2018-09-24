#!/usr/bin/python

# Preparing for a Python Interview: 10 Things You Should Know
# https://youtu.be/DEwgZNC-KyE

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print 'My name is {}'.format(self.name),
        print '    (hello from base class)'

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print "...And I am {0}".format(self.hero_name),
        print '    (hello from inherited class)'

me = Person('Jeff')
me.reveal_identity()

wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()

#(venv) [12:00:05] ~/scripts $ oop_ex2.py 
# My name is Jeff     (hello from base class)
# My name is Wade Wilson     (hello from base class)
# ...And I am Deadpool     (hello from inherited class)

# Create array of SuperHero's
print

# method 1
superlist = [SuperHero(count, count) for count in xrange(3)]
for i in range(0, 3):
    superlist[i].reveal_identity()

print

# method 2
sh = []
for i in range(0, 3):
    sh.append(SuperHero(i, i))
    sh[i].reveal_identity()
print type(sh) # <type 'list'>
print len(sh) # 3
print type(sh[0]) # <class '__main__.SuperHero'>


