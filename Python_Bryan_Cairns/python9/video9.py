__author__ = 'Bryan Cairns'

# https://docs.python.org/3.4/library/

import sys
import os

from myModule import Person
from myPackage.Car import *

#Modules and Packages
#Module ends in .py

person1 = Person()
person1.name = "Bryan"
person1.sayHello()

myCar = Car()
myCar.setSpeed(100)

myTruck = Truck()
myTruck.setSpeed(90)

print(sys.version)

print(dir(os))