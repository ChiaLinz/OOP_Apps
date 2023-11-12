"""Add a new distance method to the Point class. The method should calculate the distance from the coordinates of the current point (i.e., the self.x and self.y coordinates) to the coordinates of any other given point, and such coordinates can be provided as x and y arguments to the distance method."""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance_from_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5