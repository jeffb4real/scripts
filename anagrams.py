#!/usr/bin/env python

import string
import collections
import timeit
# http://www.ardendertat.com/2011/11/17/programming-interview-questions-16-anagram-strings/

# solution #1
def isAnagram1(str1, str2):
    return sorted(getLetters(str1))==sorted(getLetters(str2))
 
def getLetters(text):
    return [char.lower() for char in text if char in string.letters]

str1 = 'Eleven plus two'
str2 = 'Twelve plus one' 
isAnagram1(str1, str2)

# solution #2: linear time
def isAnagram2(str1, str2):
    str1, str2 = getLetters(str1), getLetters(str2)
    if len(str1)!=len(str2):
        #print False
        return
    counts=collections.defaultdict(int)
    for letter in str1:
        counts[letter]+=1
    for letter in str2:
        counts[letter]-=1
        if counts[letter]<0:
            #print False
            return
    #print True
    return

if __name__ == '__main__':
    str1 = 'Eleven plus two'
    str2 = 'Twelve plus one'
    print 'string1: ', str1
    print 'string2: ', str2
    print "\nisAnagram1:"
    print(timeit.timeit("isAnagram1('Eleven plus two', 'Twelve plus one')", setup="from __main__ import isAnagram1"))
    print "\nisAnagram2:"
    print(timeit.timeit("isAnagram2('Eleven plus two', 'Twelve plus one')", setup="from __main__ import isAnagram2"))
    # output:
    #isAnagram1:
    #12.7596487999
    #isAnagram2:
    #16.2050049305

