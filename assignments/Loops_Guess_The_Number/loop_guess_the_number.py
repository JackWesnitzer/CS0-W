import random

def generator():
    return random.randint(1,20)

def rand_guess():

    rand_int = generator()
    
    guesses_left = 6

    while guesses_left > 0:
        guess = int(input('Take a guess: '))
        if guess > rand_int:
            guesses_left -= 1
            print('Your guess is too high!')
            
        if guess < rand_int:
            guesses_left -= 1
            print('Your guess is too low!')
            
        if guess == rand_int:
            print('Congratulations {}! You WIN!!'.format(name))
            guesses_left = -1

        if guesses_left == 0:
            print('Sorry {}! You LOSE'.format(name))

def main():

    while True:   
        
        print('I am thinking of a number between 1 and 20.')
        print('You get 6 tries to guess the number.')

        rand_guess()

        answer = input("Would you like to play again? Enter y to continue; anything else to quit: ")
        
        if answer == 'y':
            continue
        if answer != 'y':
            print('Thanks for using the program! Goodbye!')
            break      
        
print("Welcome to the -- Guess The Number -- game!")

name = input('What is your name?: ')
print('Hello {}.'.format(name))

main()
