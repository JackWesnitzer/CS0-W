# Written by Jack K. Neckels-Wesnitzer
#Date: 2/22/23
#Kattis: Count the vowels program
#Algorithm steps: 1) input a string of input. 2) loop through string,
#check if character is a vowel. 3) if character is a vowel, increment count variable.
#4) print count

my_string = input('')
count = 0
for c in my_string:
    if( c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u'):
        count += 1
print(count)
