__author__ = 'Bryan Cairns'

#Loops

x = []
for i in range(10):
    x.append(i)
    print(x)

for i in x:
    print("The index is %d" % x[i])

#Dictionary
ages = {"Bryan":40,"Heather":22}

for name, age in ages.items():
    print("%s is %d years old" % (name,age))


#While
n = 0
while True:
    n += 1

    #stop if ew are equal or greater then 10
    if n >= 10:
        break

    if n == 6:
        print("6 is awesome")
        continue

    print(n)

print("Finished looping")