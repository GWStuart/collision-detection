import pygame
import math

class Point:
    def __init__(self, pos):
        self.pos = pos
        self.collide = False
        self.shape_type = "point"

    def render(self, win):
        colour = (255, 0, 0) if self.collide else (255, 255, 255)
        pygame.draw.circle(win, colour, self.pos, 1)

class Circle:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
        self.collide = False
        self.shape_type = "circle"

    def render(self, win):
        colour = (255, 0, 0) if self.collide else (255, 255, 255)
        pygame.draw.circle(win, colour, self.pos, self.radius)

class Line:
    def __init__(self, p1, p2, width):
        self.p1 = p1
        self.p2 = p2
        self.width = width
        self.collide = False
        self.shape_type = "line"

    def render(self, win):
        colour = (255, 0, 0) if self.collide else (255, 255, 255)
        Line.draw_line(win, colour, self.p1, self.p2, self.width/2)
        # pygame.draw.line(win, colour, self.p1, self.p2, self.width)
        # pygame.draw.circle(win, colour, self.p1, self.width/2)
        # pygame.draw.circle(win, colour, self.p2, self.width/2)

    def draw_line(win, colour, p1, p2, radius):
        a = math.pi if p2[0] == p1[0] else math.atan((p2[1] - p1[1]) / (p2[0] - p1[0])) + math.pi/2
        cos = radius * math.cos(a)
        sin = radius * math.sin(a)
        pygame.draw.polygon(win, colour, ((p1[0] - cos, p1[1] - sin), (p1[0] + cos, p1[1] + sin), (p2[0] + cos, p2[1] + sin), (p2[0] - cos, p2[1] - sin)))
        pygame.draw.circle(win, colour, p1, radius)
        pygame.draw.circle(win, colour, p2, radius)

class Rect:
    def __init__(self, pos, length, height):
        self.pos = pos
        self.length = length
        self.height = height
        self.collide = False
        self.shape_type = "rect"

    def render(self, win):
        colour = (255, 0, 0) if self.collide else (255, 255, 255)
        pygame.draw.rect(win, colour, (*self.pos, self.length, self.height), 5) 

