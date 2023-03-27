# input the number of test cases

# for each test case:
#   input the number of cities
#   for each city name:
#       if city exists, add one to value
#       if city doesn't exist, creat item in list and set value to one
#   print(length of the dictionary) = number of unique city names

tests = int(input())
cities = {}
for t in range(tests):
    num_cities = int(input())
    for n in range(num_cities):
        city = input()
        if city in cities:
            cities[city] = cities[city] + 1
        else:
            cities[city] = 1
    print(len(cities))
    cities = {}