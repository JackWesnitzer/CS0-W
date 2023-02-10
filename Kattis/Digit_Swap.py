# Written bu Jack K. Neckels-Wesnitzer
# Kattis Digit Swap
# 2/10/23
# Algorithm: input two digit number, swap the digits, print the swapped number

digits = input()

r_digits = ""
r_digits += digits[1]
r_digits += digits[0]

print( r_digits)