""" exercise15_1.py
This module is an assignment.
-Anton Lundmark TE2B 2019
"""
import math


class Point:
    """ Class for objects that represent points on a 2D-grid. """
    def __init__(self, x, y):
        self.x_cor = x
        self.y_cor = y

    def __str__(self):
        return f"({self.x_cor}, {self.y_cor})"

    def move(self, new_x, new_y):
        """ Method that moves a point, takes a new
            coordinate as parameters. """
        self.x_cor = new_x
        self.y_cor = new_y


class Circle:
    """ Class for objects that represent circles on a 2D-grid. """
    def __init__(self, center, radius):
        self.center = (center.x_cor, center.y_cor)
        self.x_cor = center.x_cor
        self.y_cor = center.y_cor
        self.radius = radius

    def __str__(self):
        return f"{self.center} : {self.radius}"

    def diameter(self):
        """ Method that returns the diameter of
            a given circle object. """
        return self.radius * 2


class Rectangle:
    """ Class for objects that represent rectangles on a 2D-grid. """
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.corner} : {self.width} x {self.height}"

    def get_bl_corner(self):
        """ Method for getting the bottom-left corner
            of a rectangle object. """
        return self.corner

    def get_tl_corner(self):
        """ Method for getting the top-left corner
            of a rectangle object. """
        return Point(self.corner.x_cor, self.corner.y_cor + self.height)

    def get_tr_corner(self):
        """ Method for getting the top-right corner
            of a rectangle object. """
        return Point(self.corner.x_cor + self.width, self.corner.y_cor + self.height)

    def get_br_corner(self):
        """ Method for getting the bottom-right corner
            of a rectangle object. """
        return Point(self.corner.x_cor + self.width, self.corner.y_cor)


def distance(obj_1, obj_2):
    """ Function to calculate distance
        between two point objects. """
    return math.sqrt((obj_1.x_cor - obj_2.x_cor) ** 2 + (obj_1.y_cor - obj_2.y_cor) ** 2)


def point_in_circle(circle, point):
    """ Function to determine whether a point is
        contained within a given circle. """
    if distance(circle, point) <= circle.radius:
        return True
    return False


def rect_in_circle(circle, rectangle):
    """ Function to determine whether a rectangle is
        fully contained within a given circle. """
    if distance(circle, rectangle.get_bl_corner()) <= circle.radius and \
       distance(circle, rectangle.get_tl_corner()) <= circle.radius and \
       distance(circle, rectangle.get_tr_corner()) <= circle.radius and \
       distance(circle, rectangle.get_br_corner()) <= circle.radius:
        return True
    return False


def rect_circle_overlap(circle, rectangle):
    """ Function to determine whether a rectangle is
        overlapping a given circle, be it edge or corner. """
    combinations = []
    for y_cor in range(rectangle.get_bl_corner().y_cor, rectangle.get_tl_corner().y_cor+1):
        combinations.append([int(rectangle.get_bl_corner().x_cor), y_cor])
    if check_list(combinations, circle):
        return True

    combinations = []
    for y_cor in range(rectangle.get_br_corner().y_cor, rectangle.get_tr_corner().y_cor+1):
        combinations.append([int(rectangle.get_br_corner().x_cor), y_cor])
    if check_list(combinations, circle):
        return True

    combinations = []
    for x_cor in range(rectangle.get_tl_corner().x_cor, rectangle.get_tr_corner().x_cor+1):
        combinations.append([x_cor, int(rectangle.get_tl_corner().y_cor)])
    if check_list(combinations, circle):
        return True

    combinations = []
    for x_cor in range(rectangle.get_bl_corner().x_cor, rectangle.get_br_corner().x_cor+1):
        combinations.append([x_cor, int(rectangle.get_bl_corner().y_cor)])
    if check_list(combinations, circle):
        return True
    return False


def check_list(combos, circle):
    """ Child function to rect_circle_overlap
        that converts list item to Point object,
        then proceeds to compare that value to the
        circle radius. """
    for x_cor, y_cor in combos:
        if distance(circle, Point(x_cor, y_cor)) <= circle.radius:
            return True
    return False


if __name__ == "__main__":
    CIRCLE_INIT = Point(150, 100)
    CIRCLE_BOB = Circle(CIRCLE_INIT, 75)

    TEST_POINT = Point(150, 100)
    print(point_in_circle(CIRCLE_BOB, TEST_POINT))

    RECT_INIT = Point(150, 100)
    RECT_JOSEF = Rectangle(RECT_INIT, 20, 30)
    print(rect_in_circle(CIRCLE_BOB, RECT_JOSEF))

    RECT_INIT2 = Point(0, 100)
    RECT_MENGELE = Rectangle(RECT_INIT2, 100, 10)
    print(rect_circle_overlap(CIRCLE_BOB, RECT_MENGELE))
