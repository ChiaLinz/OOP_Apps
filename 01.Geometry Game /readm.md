Geometry Game 

    Guess the coordinates (x,y)


message -> string  "Please enter some coordinates:"
coordinate -> float 10.1, 2.55, etc
rectangle -> ?
point -> ?

Development Steps:
    1. Writing down the objects on paper
    2. Writing a class for each object
    3. Writing methods for each class
    4. Calling the classes and their method


        Creating a class 
            class Point:

                def __init__(self, x, y):
                    self.x = x
                    self.y = y

            #Object instance
            point1 = Point(10, 20)

                def falls_in_rectangle(self, lowleft, upright):
                    if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
                        return True
                    else:
                        return False

                        
