
"""
    CS110 Lab
    Dictionary Lab

    Updated By: Jack K. Neckels-Wesnitzer

    CSCI 110
    Date: 3/28/23

    Working with Python dictionary (dict) data structure.
"""
from collections import namedtuple
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Colorado' : 'CO',
    'Wyoming' : 'WY',
    'Utah' : 'UT'   
}
# FIXME3 – add codes for the rest of the states - #FIXED#

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee',
    'OR': 'Salem',
    'NY': 'Albany',
    'CO': 'Denver',
    'WY': 'Cheyenne',
    'UT': 'Salt Lake City'
}

# add some more entires to capitalCity dictionary
capitalCity['NY'] = 'Albany'
capitalCity['OR'] = 'Salem'
capitalCity['CA'] = 'Sacramento'
capitalCity['MI'] = 'Lansing'
capitalCity['FL'] = 'Tallahassee'
capitalCity['CO'] = 'Denver'
capitalCity['WY'] = 'Cheyenne'
capitalCity['UT'] = 'Salt Lake City'

# FIXME4: Add rest of the states’ capital cities to capitalCity dictionary - #FIXED#

def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)

def main():
    while True:
        # clear screen
        os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                code = states[state]
                print('Code for {} is {}.'.format(state, code))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))

        elif option == '2':
            code = input('Enter a US state code: ')
            if code in capitalCity:
                print('The capital city of {} is {}.'.format(code, capitalCity[code]))
            else:
                print("Sorry! The US state code '{}' NOT found!".format(code))

        # FIXME5 - complete menu option 2 - #FIXED#

        elif option == '3':
            state = input('Enter a US state name: ')
            if state in states:
                code = states[state]
                print('The capital city of {} is {}.'.format(state, capitalCity[code]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))

        # FIXME6 - complete menu option 3 - #FIXED#

        else:
            print('Invalid input. Please try again.')
        
        # FIXME7 - handle the case where user enters invalid menu option - #FIXED#

        print('Enter to continue...')
        input()

if __name__ == "__main__":
    main()