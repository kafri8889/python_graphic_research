from math import *

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))