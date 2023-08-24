from foundation.Particle import Particle
from foundation.Shape import Shape
from foundation.Vector import Vector
import random

class ParticleSystem:

    def __init__(self, x, y, r, color):
        self.particles = []
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.add_particle()

    def add_particle(self):
        self.particles.append(
            Particle(
                Shape.circle(
                    Vector(
                        self.x + random.randint(-10, 10),
                        self.y,
                    ),
                    self.r,
                    self.color
                )
            )
        )

    def run(self):
        self.add_particle()
        for particle in self.particles:
            particle.move_particle()
            if particle.lifetime < 0:
                particle.shape.destroy()
                self.particles.remove(particle)
