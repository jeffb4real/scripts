__author__ = 'Bryan Cairns'

# fun with functions

def doSomething():
    print("Hello World")

def getList(max):
    x = list(range(max))
    for i in x:
        x[i] = i * 5
    return x

def printPerson(name,age = 0):
    print("The person is named %s " % name)
    print("They are %d years old" % age)

print("Start of program")
doSomething()

myList = getList(20)
print(myList)

printPerson("Bryan")

h = 2
if h > 4:
    printPerson("Bryan", 40)
else:
    printPerson("Heather",22)