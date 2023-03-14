"""
CSCI 110
List Lab

By: Jack K. Neckels-Wesnitzer
Date: 3/14/23

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

totalInts = 10


def getIntegers():
     # FIXME3 add num into integers list - #FIXED#
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        intList.append(num)
        i += 1
    if i == totalInts:
        print() #space
        return intList


def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    intList.sort(reverse = True)


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    printList(integers)
    print() #space
    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)
    print() #space

    # FIXME4 (10 points) - #FIXED#
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXME5 (10 points) -#FIXED#
    # Print the sorted list in descending order
    print("numbers in descending order are: ")
    printList(integers)
    print() #space

    # FIXME6 (10 points) -#FIXED#
    # Print the largest number
    m = max(integers)
    print("The largest number is {}".format(m))

     # FIXME7 (10 points) - #FIXED#
    # Print the index of the largest number
    print("Index of the largest number = 0")
    print() #space

    # FIXME8 (10 points) - #FIXED#
    # Print the smallest number
    mI = min(integers)
    print("The smallest number is {}".format(mI))

    # FIXME9 (10 points) - #FIXED#
    # Find and print the index of the smallest number
    print(f"Index of the smallest number = ", integers.index(mI))
    print() #space
   

# FIXME10 (20 points) - #FIXED#
# Call main function if this file is run as the main module
#print('call main() function to see partial outputs of the program...')
if __name__ == "__main__":
    main()