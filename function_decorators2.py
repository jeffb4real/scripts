#!/usr/bin/env python

# Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
#  Corey Schafer
# https://youtu.be/FsAPt_9Bf3U

def outer_func(msg):
    
    def inner_func():
        print msg

    return inner_func

hi_func = outer_func('Hi')
bye_func = outer_func('Bye')
hi_func()
bye_func()