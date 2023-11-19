"""
Creating a Class
This is the first exercise of a series of exercises during which you will practice classes and object-oriented programming.
In this series, let us suppose you have just been hired as a programmer at a company that sells paint for walls. The company gets visits from customers who want to paint their houses.

Your duty as a programmer is to create a program that calculates the number of paint buckets a customer needs to paint their wall area. To make this program, we will need to create a Paint class and a House class.
Let us take things step-by-step. Your task, for now, is to:
1. Create a House class which has an __init__ method.
2. The __init__ method should have a self and a wall_area parameter.
"""

class House:
    
    def __init__(self, wall_area):
        self.wall_area = wall_area


"""
Creating Another Class
The program we're building serves to calculate the amount of paint needed for a house. So, we're talking about houses and paints. Therefore we need a House type that creates house instances and a Paint type that creates paint instances. It's simple, isn't it?
We do have a House type already, but not a Paint type. Your task for this exercise is to:
1. Create a Paint type below the House class.
2. Paint should have an __init__ method with a buckets and color parameters.
"""

class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area
       
        
class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets


    
"""Adding One More Method
The Paint class doesn't do much for now. Let us add to the Paint class a method that calculates the price of the paint buckets needed to paint the house.
Specifically, your task is to:
1. Create a total_price method inside Paint. The method should only have a self parameter.
2. The total_price method should calculate and return the total price given the number of buckets for two scenarios - when color is 'white' and when it is not. The price of white paint is 1.99 and the price for color paint is 2.19.
"""

class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19
        

"""
The paint shop decides it's a good idea to apply paint discounts for special occasions. Therefore, your new task as a programmer is to incorporate a new type of object - DiscountedPaint. 
Your exact task is to:
1. Create a DiscountedPaint class below the existing code. The class should inherit from Paint.
2. Add a discounted_price method to that class. The method should have a discount_percentage parameter. There is no need to create an __init__ method.
3. The discounted_price method should calculate and return a discounted price based on the output of self.total_price() and the value of discount_percentage. 
   You could do this by first calculating the total price, then calculate the total discount, then subtract the total discount from the total price to get the discounted price and return it.
   """

class Paint:

    def __init__(self, buckets, color): # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19
        
class DiscountedPaint(Paint):

    def discounted_price(self, discount_percentage):
        price = self.total_price()
        discount = price * discount_percentage / 100
        return price - discount