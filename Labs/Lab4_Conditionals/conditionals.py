"""
Lab - Conditional Statements
By: Jack K. Neckels-Wesnitzer #fixed#
CSCI 110
Date: 2/21/23 #fixed#

Program prompts user to enter a number and determines whether the entered number is even or odd, positive or negative or zero.
Algorithm steps:
1. Prompt user to enter a number
2. Convert the value into integer and store it into a variable
3. Define a function that takes a number as parameter and determines whether the number is
even or odd using the following algorithm:
    3.1 If the number is divisible by 2 with the remainder 0, it is an even number
    3.2 Otherwise, it is an odd number
    3.3 The function returns True for even and False for odd number
4. Define a function that takes a number as parameter and determines whether the number is positive or not using the following algorithm:
	4.1 If the number is greater than zero, return True
	4.2 Otherwise, return False
5. FIXME1 – write algorithm steps to determine if the number is zero or not using a function. - #fixed#
6. Call the functions using the entered number and display the results with proper descriptions.
7. Test and validate the program output is correct with several different numbers
"""

import sys
import os

# FIXME2 - #fixed#
# determine whether the num is even or odd
# return True for even; False otherwise

def isEven(anum):

    even = False
    if anum%2 == 0:
        even = True
    return even
 
# FIXME3 – use your algorithm in step 4 to determin if num is 0 or not

def isPositive(anum):
    
    if anum > 0:
        return True
    else:
        return False

# Given a num, return True if num equals to zero, False otherwise
# FIXME4 - #fixed#

def isZero(anum):
    
    if anum == 0:
        return True
    else:
        return False

# FIXME5 - #fixed#
# Define a function that takes in a string name argument
# function greets the name by printing, e.g.: Hello, John! Welcome onboard...

def greeting(user):
    print(f"Howdy {user}, let's check some numbers!")

def clearScreen():
    """
    function that clears the console/terminal
    """
    if os.name == 'nt': # if os is windows
        os.system('cls') # run cls command
    else:
        os.system('clear')  # run clear command

def main():
    """
    main program
    """
    #clearScreen() # clear screen
    print("This program determines whether a given number is even or odd.")
    ans = input('Do you want to continue? Enter [y|n]: ')
    if ans != 'y':
        sys.exit()  # exit/end the program

# FIXME6: - #fixed#
# Prompt user to enter their name and update the name variable

    print('Please enter your name: ', end="")
    user = input()

    # loop until user wants to quit
    while True:
        # clear the screen for subsequent use
        #clearScreen()

# FIXME7: call function defined in FIXME5 to greet the user - #fixed#

        greeting(user)
        print("Enter a whole number")
        anum = input()
        if not anum.strip('-').isdecimal():
            print('Not a number, enter to continue...')
            input()
            continue

        anum = int(anum)
        if isZero(anum):
            print(anum, "is zero!")
        else:
            # Call isEven function and store the returned value into even variable

            even = isEven(anum)
            if even:
                print(anum, "is an even number!")
            else:
                print(anum, "is an odd number!")

# FIXME8 - #fixed#
# call isPositive function passing anum and print the result with proper description
        
        pos = isPositive(anum)
        if pos:
                print(anum, "is an positive number!")
        else:
                print(anum, "is an negative number!")
            
        answer = input(
            "Would you like to check another number? Enter y or yes; anything else to quit: ")
        if answer == 'y' or answer == 'yes':

# FIXME9 - make the progrom continue to run if user entered yes - #fixed#

            continue
        else:
            print('Thanks for using the program, {}! Good bye...'.format(user))
            break

def test():
    # test function to test other functions
    # FIXME10
    # using assert statment write at least 1 test case for
    # isEven, isPositive, isZero functions
    assert isEven(22) == True
    assert isPositive(99) == True
    assert isZero(0) == True

# FIXME10 - #fixed#
# call test function

test()
print('all test cases passed...')
print()
#For some reason, this runs at the very start of the program, but it does work

# call main function
main()