'''
Say you want to create a point.
A point has x, y coordinates or
A point has rho, theta polar coordinates.

You cannot create two constructors (impossible).
You can have options in the constructor itself.
'''

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y