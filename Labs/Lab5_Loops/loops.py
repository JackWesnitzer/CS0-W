"""
Lab - Playing with Loops
Updated By: Jack K. Neckels-Wesnitzer - #fixed#
CSCI 110
Date: 2/28/23 - #fixed#
Program prints geometric shapes of given height with * using loops
"""
import os
import sys

def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of that height with *
    """
    i = 1
    while i <= height:
        print('*  '*i)
        i += 1
    print()  # print an empty line

def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    i = height
    while i >= 0:
        print('*  '*i)
        i -= 1
    print()

    # FIXME3 ... - #fixed#

# FIXME4 - #fixed#
# Design and implement a function that takes a number as height and
# prints square of the given height with *.
# Square of height 5, e.g., would look like the following.

def printSquare(height):

    i = height
    while i >= 0:
        print('*  '*height)
        i -= 1
    print()

"""
*  *  *  *  *  
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
"""

def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    
    # FIXME8 call clearScreen function to clear the screen for each round of the loop - #fixed#
    
    while True:

        clearScreen()

        # FIXME9 - #fixed#
        # prompt user to enter y/Y to continue anything else to quit

        print('Program prints geometric shapes of given height with * ...')
        
        height = int(input('Please enter the height of the shape: '))

        # call printTriangle function passing user entered height

        printTriangle(height)

        # FIXME5 - #fixed#
        # Call printFlippedTriangle passing proper argument
        # Manually test the function
        
        printFlippedTriangle(height)

        # FIXME6 - #fixed#
        # Call the function defined in FIXME4 passing proper argument
        # Manually test the function
        
        printSquare(height)

        # FIXME7 add a loop to make the program to continue to run until the user wants to quit - #fixed#

        answer = input("Would you like to check another number? Enter y to continue; anything else to quit: ")

        if answer == 'y':
                continue
        if answer != 'y':
                clearScreen()
                print('Thanks for using the program! Goodbye!')
                break

        # FIXME8 call clearScreen function to clear the screen for each round of the loop - #fixed#
        
        # FIXME10 - #fixed#
        # Use conditional statements to break the loop or continue in the loop

if __name__ == "__main__":
    main()