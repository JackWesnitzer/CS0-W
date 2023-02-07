# Created by: Jack Neckels-Wesnitzer
# Date 2/7/23
# Program info: Calculate the area and perimeter of a triangle using Heron's formula

# Algorithm steps:
# Input 3 sides of triangle, they should probably be floats
# Use heron's formula to calculate the area
# First calculate semiperimeter as 1/2* (a+b+c)
# area = sqrt( semi*(semi-a)*(semi-b)*(semi-c) )
# Add sides to calculate perimeter
# Maybe check to see if it's a real trianlge for extra credit

import math

side1 = float(input('enter the length of side1:'))

print (math.sqrt(side1) )