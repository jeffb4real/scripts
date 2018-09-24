#!/usr/bin/python

# Let's Learn Python:
# https://youtu.be/pxbdnrjf-Uc?list=PL82YdDfxhWsAyY3iNNDC1kUKWAJibUGi6

def PART1():
    # Basic inheritance
    class BaseClass(object):
        # "object" is the base object; required when calling this class' __init__
        # function from child class (i.e. InheritingClass)
        def printHam(self):
            print 'ham'

    class InheritingClass(BaseClass):
        pass

    x = InheritingClass()
    x.printHam()

    # Inheritance with using base class init
    class Character(object):
        def __init__(self, name):
            self.health = 100
            self.name = name

        def printName(self):
            print self.name

    class Blacksmith(Character):
        def __init__(self, name, forgeName):
            super(Blacksmith, self).__init__(name)
            self.forge = Forge(forgeName)

    class Forge():
        def __init__(self, forgeName):
            self.name = forgeName

    bs = Blacksmith('Bob', 'Rick\'s forge')
    print bs.health
    bs.printName()
    print bs.forge.name

def PART2():
    # Overriding attribute
    class BaseClass(object):
        def __init__(self):
            self.x = 10

    class InClass(BaseClass):
        def __init__(self):
            super(InClass, self).__init__()
            self.x = 20

    i = InClass()
    print i.x;    # prints 20

def PART2a():
    # Overriding function
    class BaseClass(object):
        def test(self):
            print 'ham'

    class InClass(BaseClass):
        def test(self):
            print 'hammer time'

    i = InClass()
    i.test()

    print BaseClass.__subclasses__()


def main():
    #PART1()
    #PART2()
    PART2a()


if __name__ == '__main__':
    main()
