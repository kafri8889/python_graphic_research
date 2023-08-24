from foundation.Shape import Shape
from foundation.Vector import Vector
import math
import random

class Particle:

    def __init__(self, shape: Shape, lifetime = 225, gravity = 9.8):
        self.shape = shape
        self.lifetime = lifetime
        self.gravity = gravity
        self.acceleration = Vector(0, 0.05)
        self.velocity = Vector(random.randint(-1, 1), random.randint(-2, 0))


    def move_particle(self):
        self.lifetime -= 1
        # self.shape.print_coordinate()

        self.velocity.add(self.acceleration)
        self.shape.move(self.shape.vector.add(self.velocity))
