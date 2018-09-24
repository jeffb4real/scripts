__author__ = 'Bryan Cairns'

#Classes and Objects

# what is an object???

# A Class - it's a blue print
class Animal(object):
    name = ""

    def eat(self):
        print("%s eating..." % self.name)

    def sleep(self):
        print("%s sleeping..." % self.name)

class Mammal(Animal):
    hasBackBone = True
    hasHair = True

    def growHair(self):
        print("%s grow hair..." % self.name)

snake = Animal()
cat = Mammal()
dog = Mammal()

cat.name = "Shakes"
dog.name = "Molly"

cat.eat()
dog.sleep()

cat.growHair()
dog.growHair()


