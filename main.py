from collision import Collision
from shapes import *
import pygame
pygame.init()

LENGTH, HEIGHT = 800, 600
win = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Collision Detection")

clock = pygame.time.Clock()


def update():
    mouse_shape.collide = False
    mouse = pygame.mouse.get_pos()
    if mouse_shape.shape_type == "point" or mouse_shape.shape_type == "circle" or mouse_shape.shape_type == "rect":
        mouse_shape.pos = mouse 
    if mouse_shape.shape_type == "line":
        mouse_shape.p2 = mouse
    if mouse_shape.shape_type == "rect":
        mouse_poly = [mouse, (mouse[0] + mouse_length, mouse[1]), (mouse[0] + mouse_length, mouse[1] + mouse_height), (mouse[0], mouse[1] + mouse_height)]

    for shape in shapes:
        if shape.shape_type == "circle":
            if mouse_shape.shape_type == "point":
                shape.collide = Collision.circle_x_dot(mouse, shape.pos, shape.radius)
            elif mouse_shape.shape_type == "circle":
                shape.collide = Collision.circle_x_circle(mouse, mouse_radius, shape.pos, shape.radius)
            elif mouse_shape.shape_type == "line":
                shape.collide = Collision.xline_x_circle(shape.pos, shape.radius, mouse_p1, mouse, mouse_width)
            elif mouse_shape.shape_type == "rect":
                shape.collide = Collision.poly_x_circle(shape.pos, shape.radius, mouse_poly)
        elif shape.shape_type == "line":
            if mouse_shape.shape_type == "point":
                # shape.collide = Collision.line_x_dot(mouse, shape.p1, shape.p2, shape.width)
                shape.collide = Collision.xline_x_dot(mouse, shape.p1, shape.p2, shape.width)
            elif mouse_shape.shape_type == "circle":
                shape.collide = Collision.xline_x_circle(mouse, mouse_radius, shape.p1, shape.p2, shape.width)
            elif mouse_shape.shape_type == "line":
                # shape.collide = Collision.line_x_line(mouse_p1, mouse, shape.p1, shape.p2)
                shape.collide = Collision.xline_x_xline(mouse_p1, mouse, mouse_width, shape.p1, shape.p2, shape.width)
            elif mouse_shape.shape_type == "rect":
                # shape.collide = Collision.poly_x_line(shape.p1, shape.p2, mouse_poly)
                shape.collide = Collision.poly_x_xline(shape.p1, shape.p2, shape.width, mouse_poly)
        elif shape.shape_type == "rect":
            if mouse_shape.shape_type == "point":
                shape.collide = Collision.rect_x_dot(mouse, shape.pos, shape.length, shape.height)
            elif mouse_shape.shape_type == "circle":
                points = [shape.pos, (shape.pos[0] + shape.length, shape.pos[1]), (shape.pos[0] + shape.length, shape.pos[1] + shape.height), (shape.pos[0], shape.pos[1] + shape.height)]
                shape.collide = Collision.poly_x_circle(mouse, mouse_radius, points)
            elif mouse_shape.shape_type == "line":
                points = [shape.pos, (shape.pos[0] + shape.length, shape.pos[1]), (shape.pos[0] + shape.length, shape.pos[1] + shape.height), (shape.pos[0], shape.pos[1] + shape.height)]
                # shape.collide = Collision.poly_x_line(mouse_p1, mouse, points)
                shape.collide = Collision.poly_x_xline(mouse_p1, mouse, mouse_width, points)
            elif mouse_shape.shape_type == "rect":
                shape.collide = Collision.rect_x_rect(mouse, mouse_length, mouse_height, shape.pos, shape.length, shape.height)

        if shape.collide:
            mouse_shape.collide = True


def render():
    win.fill((30, 30, 30))

    for shape in shapes:
        shape.render(win)

    mouse_shape.render(win)

    pygame.display.update()


mouse_radius = 10
mouse_p1 = (400, 400)
mouse_width = 30 
mouse_length = 100
mouse_height = 50

shapes = [Circle((430, 30), 50), Line((50, 30), (180, 300), 30), Rect((500, 500), 100, 80), Circle((500, 400), 30), Line((200, 400), (200, 500), 5), Line((400, 200), (500, 200), 3), Line((750, 50), (650, 500), 16), Circle((80, 550), 8), Rect((200, 50), 50, 150)]
# shapes = [Line((50, 30), (180, 300), 3)]
# shapes = [Line((50, 330), (580, 330), 3)]

print("~~~~~ Collision Detection ~~~~~")
print("Choose a cursor type")
print("(1): a single point")
print("(2): a circle")
print("(3): a line")
print("(4): a rectangle")
shape_type = int(input("-> "))
if shape_type == 1:
    mouse_shape = Point((0, 0))
elif shape_type == 2:
    mouse_shape = Circle((0, 0), mouse_radius)
elif shape_type == 3:
    mouse_shape = Line(mouse_p1, (0, 0), mouse_width)
else:
    mouse_shape = Rect((0, 0), mouse_length, mouse_height) 

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
