from collision import Collision
from shapes import *
import pygame
pygame.init()

LENGTH, HEIGHT = 800, 600
win = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Collision Detection")

clock = pygame.time.Clock()


def update():
    global mouse_collision
    mouse_collision = False

    mouse = pygame.mouse.get_pos()
    for shape in shapes:
        if shape.shape_type == "circle":
            if mouse_shape.shape_type == "dot":
                shape.collide = Collision.circle_x_dot(mouse, shape.pos, shape.radius)
            elif mouse_shape.shape_type == "circle":
                shape.collide = Collision.circle_x_circle(mouse, mouse_radius, shape.pos, shape.radius)
            elif mouse_shape.shape_type == "line":
                shape.collide = Collision.xline_x_circle(shape.pos, shape.radius, mouse_p1, mouse, mouse_width)
        elif shape.shape_type == "line":
            if mouse_shape.shape_type == "dot":
                # shape.collide = Collision.line_x_dot(mouse, shape.p1, shape.p2, shape.width)
                shape.collide = Collision.xline_x_dot(mouse, shape.p1, shape.p2, shape.width)
            elif mouse_shape.shape_type == "circle":
                shape.collide = Collision.xline_x_circle(mouse, mouse_radius, shape.p1, shape.p2, shape.width)
            elif mouse_shape.shape_type == "line":
                # shape.collide = Collision.line_x_line(mouse_p1, mouse, shape.p1, shape.p2)
                shape.collide = Collision.xline_x_xline(mouse_p1, mouse, mouse_width, shape.p1, shape.p2, shape.width)
        elif shape.shape_type == "rect":
            if mouse_shape.shape_type == "dot":
                shape.collide = Collision.rect_x_dot(mouse, shape.pos, shape.length, shape.height)
            elif mouse_shape.shape_type == "circle":
                shape.collide = Collision.rect_x_dot(mouse, shape.pos, shape.length, shape.height)
            elif mouse_shape.shape_type == "line":
                points = [shape.pos, (shape.pos[0] + shape.length, shape.pos[1]), (shape.pos[0] + shape.length, shape.pos[1] + shape.height), (shape.pos[0], shape.pos[1] + shape.height)]
                shape.collide = Collision.poly_x_line(mouse_p1, mouse, points)

        if shape.collide:
            mouse_collision = True


def render():
    win.fill((30, 30, 30))

    for shape in shapes:
        shape.render(win)
    
    mouse = pygame.mouse.get_pos()
    mouse_shape.collide = mouse_collision
    if mouse_shape.shape_type == "point" or mouse_shape.shape_type == "circle":
        mouse_shape.pos = mouse 
    if mouse_shape.shape_type == "line":
        mouse_shape.p2 = mouse
    
    mouse_shape.render(win)

    pygame.display.update()


mouse_collision = False
mouse_radius = 10
mouse_p1 = (400, 400)
mouse_width = 29 

shapes = [Circle((430, 30), 50), Line((50, 30), (180, 300), 29), Rect((500, 500), 100, 80), Circle((500, 400), 30)]
# mouse_shape = Point((0, 0))
# mouse_shape = Circle((0, 0), mouse_radius)
mouse_shape = Line(mouse_p1, (0, 0), mouse_width)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            run = False
    
    update()
    render()
    clock.tick(60)
