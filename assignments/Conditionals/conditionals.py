# Written by Jack K. Neckels-Wesnitzer
# Date: 3/8/23
# program takes five user inputs and adds, multiplies, and averages them.
# also determines the largest and smallest numbers


def add(a,b,c,d,e):
        return a + b + c + d + e

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))

sum_of_numbers = add(a, b, c, d, e)

print("The sum of these numbers is {}".format(sum_of_numbers))

def multiply(a,b,c,d,e):
    return a * b * c * d * e
product_of_numbers = multiply(a, b, c, d, e)

print("The product of these numbers is {}".format(product_of_numbers))

def average(a,b,c,d,e):
    return (a + b + c + d + e)/5
average_of_numbers = average(a, b, c ,d, e)

print("The average of these numbers is {}".format(average_of_numbers))

def LargestValue(a,b,c,d,e,):
    return a or b or c or d or e
largest_number = 0

if a > b and a > c and a > d and a > e:
        largest_number = a
if b > a and b > c and b > d and b > e:
        largest_number = b
if c > a and c > b and c > d and c > e:
        largest_number = c
if d > a and d > b and d > c and d > e:
        largest_number =  d
if e > a and e > b and e > c and e > d:
        largest_number = e

print("The largest number is {}".format(largest_number))

def SmallestValue(a,b,c,d,e,):
    return a or b or c or d or e
smallest_number = 0

if a < b and a < c and a < d and a < e:
        smallest_number = a
if b < a and b < c and b < d and b < e:
        smallest_number = b
if c < a and c < b and c < d and c < e:
        smallest_number = c
if d < a and d < b and d < c and d < e:
        smallest_number =  d
if e < a and e < b and e < c and e < d:
        smallest_number = e

print("The smallest number is {}".format(smallest_number))

def testFunction():
    assert(add(1,2,3,4,5)) == 15
    assert(add(2,3,4,5,6)) == 20
    assert(multiply(2,4,6,8,5)) == 1920
    assert(multiply(3,5,7,9,1)) == 945
    assert(average(3,4,5,6,7)) == 5
    assert(average(12,3,14,5,16)) == 10
    assert(LargestValue(9,8,7,6,5)) == 9
    assert(LargestValue(50,40,30,20,10)) == 50
    assert(SmallestValue(1,2,3,4,5)) == 1
    assert(SmallestValue(2,4,6,8,10)) == 2
    
print("All test cases passed.")

def main():
    if __name__ == "__main__":
        
        add(a,b,c,d,e)
        multiply(a,b,c,d,e)
        average(a,b,c,d,e)
        LargestValue(a,b,c,d,e)
        SmallestValue(a,b,c,d,e)
        testFunction()
main()
