#!/usr/bin/env python

__author__ = 'Bryan Cairns'

#Lists

mList = [5,2,1,4,3,"dog","cat","bird"]

print(mList)

#count the number of cats
print("There are %d cats " % mList.count("cat"))

#number of objects in the list
print("There are %d objects in the list" % len(mList))

#Find the index of the cat
print("The cat is at index: %d" % mList.index("cat"))

#insert into the list
mList.insert(2,"fish")
print(mList)

#Append an object
mList.append("snake")
print(mList)

#Remove the fish
mList.remove("fish")
print(mList)

#Reverse the list
mList.reverse()
print(mList)
print("The cat is at index: %d" % mList.index("cat"))

#Slice and sort
#newList = mList.copy()
newList = mList
newList.reverse()
newList = newList[0:5]
newList.sort()
print(newList)

#Modify an item in the list
newList[0] = "LOL"
print(newList)

##############################################

#Tuple
# """
# Tuples


# MyList = [1,2,3,4,5]
# MyTuple = (1,2,3,4,5)

# """

myTuple = (1,2,3,4,5,"TUPLE")
print(myTuple)

print("The index of 3 is %d" % myTuple.index(3))

#BAD - will not work
#myTuple[0] = "LOL"
#print(myTuple)

#Dictionaries
print '\nDictionaries\n-----------------'
ages = {"Bryan":40, "Heather":22}
print(ages)

print(ages.keys())
print(ages.values())
print(ages.items())

print(ages["Bryan"])

#Delete an item
del ages["Bryan"] # can use POP
print(ages)

#Add an item in
ages["Bryan"] = 40
print(ages.items())

#Modify a value
ages["Bryan"] = 99
print(ages)
