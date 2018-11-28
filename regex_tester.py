import re

pattern = r'\D(\d\d\d\d)\D'
pattern = r'^\D*(\d\d\d\d)*\D*$'
pattern = r'^|\D(\d\d\d\d)\D|$'
pattern = r'\D*(\d\d\d\d)\D*'    # <-- works 2nd best for finding year(s)
pattern = r'\b(\d\d\d\d)\b'      # <-- works best for finding year(s)

print ("Hi. I'm looking for this pattern: %s" % pattern)

while (True):
    userin = input('text: ')
    print ("You entered: ->%s<-" % userin)
    print (re.findall(pattern, userin))
    print ('')
