#!/usr/bin/python

# content of test_module.py
def test_something():
    x=3
    #assert x == 4

class TestSomething:
    def test_something(self):

        x=1
        assert x == 1
        x = y = 0      # with unittest.py
        #assert x       # assertTrue(x)
        assert x == 1  # assertEqual(x, 1)
        assert x != 2  # assertNotEqual(x, 2)
        assert not x   # assertFalse(x)
        assert x < 3 and y > 5 #?
