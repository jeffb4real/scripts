#!/usr/bin/env python

# Example taken from: 
# https://pypi.org/project/pytest/#description

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    assert func(3) == 4

