import math

class Collision:
    """ 
    NOTE: xline is used to represent a line where the width is taken into account
    Whereas just line represents an infinetly thing line
    """

    @staticmethod
    def circle_x_dot(dot, circle, radius):
        # detects collisions between a circle and a dot
        return math.dist(dot, circle) <= radius

    @staticmethod
    def circle_x_circle(circle1, radius1, circle2, radius2):
        return Collision.circle_x_dot(circle1, circle2, radius1 + radius2)

    @staticmethod
    def line_x_dot(dot, p1, p2):
        # detects a collision between a line and a dot0
        t = (dot[0] - p1[0]) / (p2[0] - p1[0])
        return dot[1] == round(p1[1] + t * (p2[1] - p1[1]))

    @staticmethod
    def xline_x_dot(dot, p1, p2, width):
        # detects a collision between an xline and a dot
        d = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        t = ((dot[0] - p1[0]) * (p2[0] - p1[0]) + (dot[1] - p1[1]) * (p2[1] - p1[1])) / d
        t = max(0, min(1, t))
        x, y = p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1])
        return Collision.circle_x_dot(dot, (x, y), width/2)

    @staticmethod
    def xline_x_circle(dot, radius, p1, p2, width):
        return Collision.xline_x_dot(dot, p1, p2, width + 2*radius)

    @staticmethod
    def line_x_line(p1, p2, p3, p4):
        d = ((p4[1] - p3[1])*(p2[0] - p1[0]) - (p4[0] - p3[0])*(p2[1] - p1[1]))
        t1 = ((p4[0] - p3[0])*(p1[1] - p3[1]) - (p4[1] - p3[1])*(p1[0] - p3[0])) / d
        t2 = ((p2[0] - p1[0])*(p1[1] - p3[1]) - (p2[1] - p1[1])*(p1[0] - p3[0])) / d
        return 0 <= t1 <= 1 and 0 <= t2 <= 1

    @staticmethod
    def xline_x_xline(p1, p2, w1, p3, p4, w2):
        d = ((p4[1] - p3[1])*(p2[0] - p1[0]) - (p4[0] - p3[0])*(p2[1] - p1[1]))
        t1 = ((p4[0] - p3[0])*(p1[1] - p3[1]) - (p4[1] - p3[1])*(p1[0] - p3[0])) / d
        t2 = ((p2[0] - p1[0])*(p1[1] - p3[1]) - (p2[1] - p1[1])*(p1[0] - p3[0])) / d

        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            return True
        
        return Collision.xline_x_circle(p1, w1/2, p3, p4, w2) or Collision.xline_x_circle(p2, w1/2, p3, p4, w2) or Collision.xline_x_circle(p3, w2/2, p1, p2, w1) or Collision.xline_x_circle(p4, w2/2, p1, p2, w1)
    
    @staticmethod
    def rect_x_dot(dot, pos, length, height):
        # detects a collision between a rect and a dot
        if pos[0] <= dot[0] <= pos[0] + length:
            return pos[1] <= dot[1] <= pos[1] + height
        return False
    
    def poly_x_line(p1, p2, poly):
        poly.append(tuple(poly[0]))
        for i in range(len(poly) - 1):
            if Collision.line_x_line(p1, p2, poly[i], poly[i+1]):
                return True
        return False
    
