#!/usr/bin/env python

# http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Stacks%2C%20Queues%20and%20Deques/Implementation%20of%20Stack.ipynb

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s = Stack()
print s.isEmpty()
# True
print s.push(1)
# none
print s.push('two')
# none
print s.peek()
# 'two'
print s.push(True)
# none
print s.size()
# 3
print s.isEmpty()
# False
print s.pop()
# True
print s.pop()
# two
print s.size()
# 1
print s.pop()
# 1
print s.isEmpty()
# True
