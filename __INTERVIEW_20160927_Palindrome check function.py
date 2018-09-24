#!/usr/bin/env python

# Palindrome check function: 
# abcda
# 121
# 1111
# 11433411

#  8 -> false
#  121 -> true
 
#  Test cases:
#  1) single char -> false
#  2) non-digit char(s) -> false
#  3) negative number -> false
#  4) integer -> true/false
#  5) float -> false
 
#  ===========================
#  Return next sequential palindrome function:
#  1 -> 11 
#  11 -> 22
#  120 -> 121
#  5 -> 11
#  80 -> 88
#  -12 -> 11
 
#  Next sequential palindrome tests:
#  1) non-digit char(s) -> TypeError assert
#  2) any negative number -> return 11
#  3) single digit -> return 11
#  4) multiple digits -> return next palindrome
#  5) palindrome -> return next palindrome
#  6) overflow int data type -> assert
 
#  next_palindrome.py
def next_palindrome(arg):
 
    ''' This function returns the next sequential palindrome.
    Input should be a +/- integer.'''

    if 'int' not in str(type(arg)):
        return false

    next_palindrome = 11
    if arg <= 0:
        return next_palindrome

    if arg < 11:
        return next_palindrome

    inf = 65535   # prevent overflow; max 16-bit int
    for candidate in range(arg + 1, inf):    # CHANGE: replace while with for
        if is_palindrome(candidate):   # CHANGE: break up into two lines
            return candidate 

def is_palindrome(arg):
    # arg is known to be int
    var = str(arg)    # e.g. 1221, 121    # CHANGE: MOVED LINE UP
    if len(var) == 1:   # CHANGED arg TO var
        return false

    #length = len(arg)  # CHANGE: comment out
    #x == -1  # CHANGE: comment out
    #for char in (var):  # CHANGE: comment out
    return var == var[::-1]    # CHANGED char to var; just return the comparison (i.e. True / False)
            # x -= 1    # CHANGE: comment out

for val in [1, 11, 120, 5, 80, -12, 70, 4858]:
    print val, next_palindrome(val)
# 1 11
# 11 22
# 120 121
# 5 11
# 80 88
# -12 11
# 70 77
# 4858 4884
