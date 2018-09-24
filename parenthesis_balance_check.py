#!/usr/bin/python

# Python for data structures, algorithms and interviews
# Balanced parenthesis check - section 13, lecture 77
'''Given a string of opening and closing parenthesis (assume no other characters),
check whether it's balanced.
For example, '([])' is balanced but '([)]' is not.'''
#import sets

def balance_check (paren_string):

    if len(paren_string)%2 != 0:
        return False

    # set of char
    opening = set('([{')
    # set of lists
    matches = set([ ('(', ')'), ('{', '}'), ('[', ']') ])

    print '->%s<-   ' % paren_string,

    stack = []
    for paren in paren_string:

        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            # (last_open, paren) is a list
            if (last_open,paren) not in matches:
                return False

            return len(stack) == 0

print balance_check('(')
print balance_check('[')
print balance_check('{')
print balance_check('[[[')
print balance_check('[({})')
print balance_check('[]')
print balance_check('{}')
print balance_check('{()}')
print balance_check('{[()]}')
print balance_check('{([[[()]]])}')
print balance_check('{[(((((())))))]}')



