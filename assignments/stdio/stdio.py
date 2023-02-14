# written by Jack K Neckels-Wesnitzer
# Date 02/10/23

# standard input and output program that prints four playing cards in ASCII and/or uniCODE
# begins by greeting the player and asking their name
# player inputs their name
# program calls them by name and introduces ASCII cards

def greeting():
    name = input('Hello there, what is your name?: ')
    return name

name = greeting()
print('Hey,', name)
print('Here are a few playing cards that I created. Maybe I will make a card game!')

print(" ========")
print("| A      |")
print("|  /\\/\\  |")
print("|  \\  /  |")
print("|   \\/   |")
print("|      A |")
print(" ========")

print("Ace of Hearts")

print(" ========")
print("| A      |")
print("|   /\\   |")
print("|  /  \\  |")
print("|  \\  /  |")
print("|   \\/   |")
print("|      A |")
print(" ========")

print("Ace of Diamonds")

print(" ========")
print("| A      |")
print("|  (  )  |")
print("| (_  _) |")
print("|   /\\   |")
print("|      A |")
print(" ========")

print("Ace of Clubs")

print(" ========")
print("| A      |")
print("|   /\\   |")
print("|  /  \\  |")
print("| (_  _) |")
print("|   /\\   |")
print("|      A |")
print(" ========")

print("Ace of Spades")