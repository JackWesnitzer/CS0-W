## Written by Jack K. Neckels-Wesnitzer
# Date: 2/17/23
# Kattis: FizzBuzz
# print numbers 1 to N, except if the number is divisible by X, print "Fizz",
# if it's divisible by Y. print "Buzz", if it's divisible by both, print "FizzBuzz"

X, Y, N, = input().split()
N = int(N)
Y = int(Y)
X = int(X)

for i in range(N):
    string = ""
    num = i+1
    if ( num%X == 0):
        string += "Fizz"
    if ( num%Y == 0):
        string += "Buzz"
    if ( num%X != 0 and num%Y != 0):
        string = string + str(num)
    print(string)
