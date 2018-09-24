__author__ = 'Bryan Cairns'

#Conditions

# make an if statement

x = 9
if x == 9:
    print("9 is here")

#Change X to show inequality
x = 8
if x != 9:
    print("9 no more")

#Remember x == 8
if x > 10:
    print("greater then 10")
else:
    print("less then 10")

#Boolean operators
name = "Bryan"
age = 40
if name == "Bryan" and age == 40:
    print("there can be only one")
else:
    print("You are not Bryan")

age = 21
if name == "Bryan" or age == 40:
    print("You and I have something in common")
else:
    print("We have nothing in common")

#List checking
x = ("dog","cat","fish")
if "cat" in x:
    print("We have a cat")
else:
    print("No cats how sad")

#Comparison
a  = (1,2,3,4,5)
b  = (1,2,3,4,5)

if a == b:
    print("They are the same")
else:
    print("They are not the same")

if a is b:
    print("They are the same object")
else:
    print("They are not the same object")


# Nestled If statements
name = "Bryan"
age = 40
pet = "cat"

if name == "Bryan":
    print("Hello bryan")

    if age == 40:
        print("You are 40 years old")

        if pet == "cat":
            print("You have a pet cat")
        else:
            print("Go get a cat")

    else:
        print("You are not 40 years old")

else:
    print("You are not bryan")
