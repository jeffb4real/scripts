#!/usr/bin/env python

# http://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python

class Bomb:
    def __init__(self):
        ""

    def talk(self):
        self.explode()

    def explode(self):
        print "BOOM!, The bomb explodes."

class Duck:
    def __init__(self):
        ""
    def talk(self):
        print "I am a duck, I will not blow up if you ask me to talk."    

class Kid:
    kids_duck = None

    def __init__(self):
        print "Kid comes around a corner and asks you for money so he could buy a duck."

    def takeDuck(self, duck):
        self.kids_duck = duck
        print "The kid accepts the duck, and happily skips along"

    def doYourThing(self):
        print "The kid tries to get the duck to talk"
        self.kids_duck.talk()

myKid = Kid()
myBomb = Bomb()
myKid.takeDuck(myBomb)
myKid.doYourThing()

# Kid comes around a corner and asks you for money so he could buy a duck.
# The kid accepts the duck, and happily skips along
# The kid tries to get the duck to talk
# BOOM!, The bomb explodes.
