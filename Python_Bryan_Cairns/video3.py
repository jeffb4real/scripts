__author__ = 'Bryan Cairns'

# Super awesome time with strings

str = "Hello World"

#Print the length of a string
print("String is %d bytes long" % len(str))

#Make upper case
print(str.upper())

#make it lower case
print(str.lower())

#Find the index of a letter
print("The index of o is %d" % str.upper().index("O"))

#Count the number of L's
print("There are %d letter L's in '%s'" % (str.upper().count("L"),str))

#Slice the string
print(str[3])
print(str[1:6])
print(str[1:len(str)])

#Split
name = "Bryan Cairns"
mylist = name.split(" ")
print(mylist)
print("My first name is %s and my last name is %s" % (mylist[0],mylist[1]))