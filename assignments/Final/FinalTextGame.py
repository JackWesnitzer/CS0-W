#Python Final

import random
    
def stealthCheck():
    sneak = random.randint(0,1)

    if sneak == 1:
        print('\nSUCCESS! You manage to move silently and swiftly to the other side, reaching the door without alerting the goblins. You carefully turn the handle and quietly pull the door open just wide enough for you to slip into the next room unnoticed.')
    elif sneak == 0:
        print('\nFAILURE! As you tiptoe your way into the room, your foot crunches on some broken glass, causing the goblins to wrench their heads around and focus their attention on you. They snarl ferociously, mouths gripping with sticky saliva. One lets out a shrill shriek, and they all begin bounding toward you, spears at the ready.')

def dexCheck():
    dexterity = random.randint(0,3)

    if dexterity == 0:
        print('\nFAILURE! You barrel down the hallway recklessly and the suits of armor start to swing their weapons. You are caught it the shoulder by the blade of an axe and tumble unceremoniously to the ground. You look up just in time to see a warhammer come down on you and collapse your skull.')
        print('\nY O U  A R E  V A N Q U I S H E D')
    if dexterity != 0:
        print('\nSUCCESS! You expertly dart, bob, and weave your way down the narrow hall. As you suspected, the suits of armor are enchanted; they animate and begin to wildly flail their weapons around. You gracefully dodge all of their attacks, passing through the battery without so much as a scratch or a hair out of place. You reach another door at the end of the hall with ease.')

def greeting():
    name = input('Greetings adventurer! What is your name?: ')
    return name
        
def intro():
    print('\nin this short text based adventure, you can explore by simply typing [north], [south], [east], or [west] to travel in that direction. If there is something worth inspecting in an area, a prompt will ask you if you would like to examine further, to which you can accept with [y] or decline with [n].')

    print('\nBe sure to remain vigilant in your quest, for many dangers lie in wait, and vicious monsters might lurk in each darkened corner. Will you bravely defend yourself? Or will you scramble away and live to fight another day? Only time will tell, so let us begin...')

    print("\nYour head is reeling as you regain consciousness. In a daze, you sit up very slowly, and your eyes gradually begin to adjust to the darkness all around you. It would appear that you were knocked out, and have been abducted! Left for dead in this large central room, perhaps within some sort of castle or keep, you have no recollection as to how you ended up here. Glancing around, you spot several doorways, one on each side of the room.")

class Player:
    def __init__(self, hp=10, damage=2):
        self.hp = hp
        self.damage = damage

    def take_damage(self, enemy):
        self.hp -= enemy.damage
    def hit(self, enemy):
        enemy.hp -= self.damage
    def __str__(self):
        return f'HP = {self.hp}, Damage = {self.damage}'

inventory = []

def addToInventory(item):
    inventory.append(item)

def startScreen():
    
    DirectChoose = input("\nWhich way will you go?: ")
    if DirectChoose == "north":
        armorTrapRoom()
    elif DirectChoose == "south":
        lockedDoor()
    elif DirectChoose == "east":
        goblinRoom()
    elif DirectChoose == "west":
        weaponStorage()
    else:
        print("Please enter a valid direction.")
        
def lockedDoor():
    print("A large ornate door towers before you. Inspect the door? [y/n]")
    inspect = input("\n")
    if inspect == "y":
        print("\nYou pull on the door handle, gently at first, and then with more gusto. It appears that it won't budge. There is an intricate locking mechanism on the face of the door... perhaps it needs to be opened through other means? You can come back to it later, but for now you return to the center of the room.")
        startScreen()
    if inspect == "n":
        print("\nYou decide that the door feels suspicious and that you had better not mess with it just yet. You have made note of the big door here, and maybe you will come back later. For now, you return to the center of the room.")
        startScreen()

def armorTrapRoom():
    print('\nYou step forth into a long and narrow hallway that is faintly illuminated by several flickering sconces. Peering into the darkness, the hall seems like it stretches on forever. Menacing suits of silver armor line the walls. Their stillness is unsettling, and it feels as if they are looking at you. Something tells you that there is more to them than meets the eye, and you had best not waste time making it through this room. Venture into the hallway? [y/n] *75% chance of success*')
    venture = input('\n')
    if venture == "y":
        dexCheck()
    if venture == "n":
        print('\nYou consider making a mad dash down the darkened corridor, but you loose your nerve as you swear you saw one of the armor sets turn its head to glare at you. Somewhat ashamed at your cowardice, you slink back into the main atrium to choose a different path.')
        startScreen(

        )
def weaponStorage():
    print("\nIt appears that this room once used housed a substantial weapons cache, as well as other armaments. It's clearly been raided, and it's likely the best stuff has already been snatched up. If armed forces ever roamed these halls, they're long gone and have been for some time now. You have no idea what might be lurking in a place like this, so you'll need a means of protecting yourself. If you are lucky, their might be something left if you search the storeroom. Inspect the storeroom? [y/n]")
    inspect = input('\n')
    if inspect == "y":
        print("\nYou turn over rotting boards, sift through heaps of scrap, and rummage through countless dilapidated chests without finding anything. Just as you are about to give up, you spy a glint of something metal. As you heave a toppled cabinet aside, a battle worn sword and shield tumble out of the wreckage.")
        addToInventory("sword")
        print("\nYOU GOT THE SWORD!")
        addToInventory("shield")
        print("\nYOU GOT THE SHIELD!")
        print("\nYou've found all you needed in this room, so you return to the atrium.")
        startScreen()
    if inspect == "n":
        print("\nWho knows how long this refuse pile has been sitting here. It could be dangerous to move the rubble and timber around, so you resolve to just leave it be for now. You really should find some sort of weapon soon though...")
        print("\nYou return to the atrium.")
        startScreen()
        
def goblinRoom():
        print("\nAs you cross the threshold into this room, you freeze immediately when you spot three creepy little goblins huddled around something in the corner. If you squint, you can barely make out the shape of a storage chest that the goblins can't seem to open. They haven't noticed you yet, and there is a door on the other side of the room you might be able to sneak over to. Sneak past the goblins? [y/n] *50% chance of success*")
        Attempt = input('\n')
        if Attempt == "y":
            stealthCheck()
        if Attempt == "n":
            print('\nThose goblins seem awfully scary, and if they notice you, you are probably done for. Better not to take your chances here. You carefully back up into the previous room. You will forge ahead on a different, and hopefull less goblin-filled path')
        
greeting()
intro()
startScreen()
