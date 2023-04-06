"""
File I/O Lab
By: Jack K. Neckels-Wesnitzer

CSCI 110
Date: 4/4/23

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

totalInts = 10

def readData():
    intList = []
    FileName = input('Enter a file name to open: ')
    with open(FileName) as file:
        while True:
            line = file.readline()
            if(line == ""):
                break
            intList.append(int(line))
    print(intList)
    return intList

    # FIXME1 (20 points): - #FIXED#
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    
def sortListInAscendingOrder(lstInts):
    lstInts.sort()
    print(lstInts)

    # FIXME2 - #FIXED#
    # sort lstInts list in ascending order

def sortListInDescendingOrder(lstInts):
    lstInts.sort()
    lstInts = lstInts.reverse()

    # FIXME3 - #FIXED#
    # sort lstInts in descending order


def printList(printFile, lstInts):
    for i in lstInts:
       
        printFile.write(str(i)+'\n')
    printFile.write('\n')
    
 # FIXME4 - #FIXED#
        # write each value one line at a time to file
        # handled by printFile object.

def main():
    
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers

    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)
    
    sortListInDescendingOrder(integers)
    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)

    # FIXME5 - #FIXED#
    # Call sortListInDescendingOrder function

    # FIXME6 - #FIXED#
    # Write the sorted list in descending order to the output file

    printFile.write("The largest number is:\n")
    printFile.write(str(max(integers)))
    printFile.write('\n')
    printFile.write('\n') #spaces

    # FIXME7 - #FIXED#
    # Print the largest number to the output file

    printFile.write("The smallest number is:\n")
    printFile.write(str(min(integers)))

    # FIXME8 - #FIXED#
    # Print the smallest number to the output file
    
    printFile.close()
    print('Done executing the program! Check the output file for results.')

if __name__ == "__main__":
    main()

# FIXME9 - #FIXED#
# Call main function if this module is run as the main module