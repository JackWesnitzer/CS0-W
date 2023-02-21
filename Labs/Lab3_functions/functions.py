###
# Functions Lab
# Updated By: Jack K. Neckels-Wesnitzer -fixed
#
# CSCI 110
# Date: 2/15/23 -fixed
#
# Playing with functions and variables scopes.
# There are 10 FIXMEs each worth 10 points!
###

# assign Bill Gates to someName variable
someName = "Bill Gates"  # someName is global variable

# FIXME3 - Assign your name to myName variable
myName = "Jack" #fixed#
# myName is a global variable

def printHello():
    """
    function that prints Hello World.
    doesn't take any argument and doesn't return a value
    """
    print("Hello World!")


def printHelloTwice():
    """
    # function that prints Hello World twice
    # calls printHello function twice
    """
    printHello()
    printHello()


def greetName(name):
    """ 
    function that takes one argument name and greets the name
    """
    print("Hi there {}".format(name))


def meetAndGreet():
    """
    function that greets someone
    doesn't take any argument and doesn't return any value
    """
    firstName = input("\nHey there! what's your first name?\n")
    # firstName is local variable
    greetName(firstName)  # call greetName function
    print("My name is {}. Nice meeting you.".format(someName))
    print()  # print empty line


def convertTime(seconds):
    """
    #FIXME - #fixed#
    Define a function named convertTime that takes 1 integer argument called seconds.
    The function converts and prints the seconds in hours, minute, and seconds formats.
    """
    hour = seconds//3600
    # seconds = seconds%3600
    # seconds = seconds-hour*3600;
    m = seconds//60
    m = m % 60
    sec = seconds % 60
    #seconds = seconds - m*60
    print("{} seconds = {} hours, {} minutes, {} seconds".format(seconds, hour, m, sec))
    print()

    pass

def findSeconds(hours):
    """
    #FIXME - #fixed#
    Define a function named findSeconds that takes hours as 1 integer argument.
    The function converts hours into seconds and returns it
    """
    # FIXME4 convert hours into seconds and update seconds variable
    # Hint: there are 3600 seconds in 1 hour
    
    seconds = hours*3600 
    
    print(f"hours = {hours}, seconds = {seconds}")

    pass
    
def testFunctions():
    # test1 : # for 1 hour == 3600 seconds
    assert(findSeconds(1) == 3600)
    assert(findSeconds(2) == 7200)
    assert(findSeconds(3) == 10,800)
    assert(findSeconds(4) == 14,400)
    # FIXME5 - write 3 more tests cases for findSeconds function

# FIXME6: call printHello function - #fixed#
printHello()
print()

# FIXME7 - call printHelloTwice function - #fixed
printHelloTwice()
print()

greetName(someName)  # calling function passing variable as argument
greetName("Larry Page")  # calling function passing literal value as argument

# call meetAndGreet function
meetAndGreet()

# call function convertTime passing proper argument - #fixed#
convertTime(60)

# FIXME8 - Call converTime function passing 3600 as seconds - #fixed#
hours = int(input('Enter a number of hours: '))
findSeconds(hours)

# FIXME9 - Call converTime function passing 3661 as seconds
#I didn't understand what you meant by this#
# FIXME10 - Call testFunctions -#fixed#
testFunctions
print('all test cases passed...')
#I assume this is what you wanted?#