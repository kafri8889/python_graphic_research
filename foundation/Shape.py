import pygame
from foundation.Vector import Vector
from enum import Enum

class Shape:

    class ShapeType(Enum):
        Circle = 1
        Rect = 2

    def __init__(self, rect, color, type, r = 0):
        self.display = pygame.display.get_surface()
        self.color = color
        self.type = type
        self.rect = rect
        self.vector = Vector(rect.x, rect.y)

        # for circle
        self.r = r

    @classmethod
    def circle(cls, vector: Vector, r, color):
        rect = pygame.draw.circle(
            surface=pygame.display.get_surface(),
            color=color,
            radius=r,
            center=(vector.x,vector.y)
        )

        return Shape(rect, color, Shape.ShapeType.Circle, r)

    def print_coordinate(self):
        print('(' + str(self.rect.centerx) + ', ' + str(self.rect.centery) + ')')

    def move(self, vector: Vector):
        # update koordinat
        self.vector = vector

        # redraw shape
        self.display.fill((0,0,0), self.rect)
        if self.type == Shape.ShapeType.Circle:
            self.rect = pygame.draw.circle(
            surface=pygame.display.get_surface(),
            color=self.color,
            radius=self.r,
            center=(vector.x, vector.y)
        )

    def destroy(self):
        self.display.fill((0, 0, 0), self.rect)

