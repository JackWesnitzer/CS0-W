"""
Lab - Object Oriented Programming (OOP)
By: Jack K. Neckels-Wesnitzer

CSCI 110
Date: 4/20/23

Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math


class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCirumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi*(self.radius**2)

    def findCircumference(self):
        # FIXME1: Find and return the circumference of the circle (20 pts) - #FIXED#

        return 2*math.pi*(self.radius)

    def __str__(self):
         # FIXME2: Modify the statement to return circumference as well (20 pts) - #FIXED#

        return "Circle - radius: {:.2f} and area: {:.2f} and circumference {:.2f}".format(self.radius, self.area, self.circumference)


def main():

    # instantiate aCir object with radius 1

    aCir = Circle(1)
    print(aCir)

    # FIXME3: (20 pts) -#FIXED#
    # Instantiate another circle with radius 5
    # Print the circle

    bCir = Circle(5)
    print(bCir)

    # FIMXE4: (20 pts) - #FIXED#
    # prompt user to enter radius and store into a variable

    UserRadius = input("Enter the radius of your circle: ")
    UserRadius = int(UserRadius)
    
    # FIXME5: (20 pts) - #FIXED#
    # create a circle with the user provided radius
    # print the circle
    
    uCir = Circle(UserRadius)
    print(uCir)
    
if __name__ == "__main__":
    main()