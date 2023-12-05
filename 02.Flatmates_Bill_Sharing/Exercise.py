"""
Rectangle Object
Let us have some exercises to help you not forget what you learned in the videos.
For this exercise, your task is to create a Rectangle class whose __init__ method should take a self, width, and height parameter. The rectangle should have an area method that calculates and returns the area of the rectangle.
"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        area = self.width * self.height
        return area
"""
Distance
Write a method that calculates the distance from the center of the rectangle to a given point. To implement that, you need to complete these steps:
1. Add an x and y parameter to __init__ and create their corresponding self.x and self.y attributes. These are to represent the coordinates of the center of the rectangle.
2. Add a distance_to_point method to Rectangle. The method should have an x and y parameter. These are to represent the coordinates of an imaginary point. The distance_to_point method should calculate the distance from the center of the rectangle to the point given the two x, y pairs.
3. To calculate the distance you can use the formula ((self.x - x)**2 + (self.y - y)**2) ** 0.5 which is the equivalent of √((x_2-x_1)²+(y_2-y_1)²)
"""

class Rectangle:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def distance_to_point(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2) ** 0.5
        return dist
    
"""
Instantiate Rectangle
Your task for this exercise is to:
1. Create a Rectangle instance below the Rectangle class. Use whatever variable name you like to store the instance and whatever argument values.
2. Call the area method and print out its output. It doesn't matter if you store the method call in a variable and then print out the variable, or insert the method call directly inside the print function.
"""

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
rectangle = Rectangle(50,100)
print(rectangle.area())

"""
Time
Let us calculate the time it takes the center of the rectangle to reach a given point. To implement this, you need to complete the steps below:
1. Add a time_to_point method to Rectangle. The method should have an x and y parameter. These are to represent the coordinates of the point.
2. The time_to_point method should also have a speed parameter.
"""

class Rectangle:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def distance_to_point(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2) ** 0.5
        return dist
        
    def time_to_point(self, x, y, speed):
        return float(self.distance_to_point(x,y)) / float(speed)
    
"""
Add Perimeter
Add a perimeter method to Rectangle. The method should calculate and return the perimeter of a rectangle.
"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return (self.width + self.height)*2
    
"""
Call Time
Your tasks for this exercise:
1. Create an instance of Rectangle with argument values width=3, height=4, x=1, and y=2.
2. Call the time_to_point method of the instance and print out the method output. The arguments of the method should be x=2, y=3, and speed=20.
"""

class Rectangle:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def distance_to_point(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2) ** 0.5
        return dist

    def time_to_point(self, x, y, speed):
        time = self.distance_to_point(x, y) / speed
        return time

rec = Rectangle(2, 3, 1, 2)
rec_t = rec.time_to_point(2, 3, 20)
print(rec_t)