#!/usr/bin/python3
from random import randint
import dice
import sys
import os
'''Chad AND KEN'S Ongoing RPG Game'''

bestiary = [{'name' : 'A bandit', 'health' : 10, 'damage' : '1d5'},
            {'name' : 'The Corrupt Sheriff', 'health' : 15, 'damage' : '1d8'},
            {'name' : 'Bad Chad', 'health' : 20, 'damage' : '1d12'}]
armory = {'knife': {'damage': '1d12'},'brass_knuckles':{'damage':'1d12'}}
gun_lookup = {'pistol': {'damage': '4d6'}, 'shotgun':{'damage': '6d8'}}
player_health = 20
inventory = []
holster = []

def combat():
    monster_ID= randint(0,2)

    global player_health, inventory, armory, bestiary
    round = 1
    monster_health = bestiary[monster_ID]['health']

    print(f"{bestiary[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Villain Health: [" + str(monster_health) + "]")

        print("Type: RUN, SHOOT [gun], or USE [weapon]") # gotta write code for cast
        move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
        monster_damage = sum(dice.roll(bestiary[monster_ID]['damage']))
        print("\n=========================")


        if move[0] == 'use': #
            if move[1] in inventory: # checks if weapon is in your inventory
                player_damage = dice.roll(armory[move[1]]['damage'])
                print(f"You hit a {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory!")

        if move[0] == 'shoot': #
            if move[1] in holster: # checks if spell is in your spellbook
                if move[1].lower() == 'shotgun':
                    player_damage = sum(dice.roll(gun_lookup[move[1]]['damage']))
                    print(f"You raise the shotgun to your shoulder. You feel the kick as smoke and fire explodes from the barrell. You hit {bestiary[monster_ID]['name']} for {player_damage} damage!")
                if move[1].lower() == 'pistol':
                    player_damage = sum(dice.roll(gun_lookup[move[1]]['damage']))
                    print(f"Your hand drops to your holster. In a split second you draw and fire from your hip hitting {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in holster:
                print(f"You don't have a {move[1]}!")

        if move[0] == 'run': #
            escape_chance= randint(1,10) #+ player_speed # if I set this variable later, here's where it would work

            if escape_chance >= 10:
                print("You make a flawless escape!")
                break
            if escape_chance >= 5:
                print("You expose your back as you turn and flee- the villain takes advantage.")
                print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                player_health -= int(monster_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("Sorry Partner. Looks like you didn't make it.")
                    print("\nGAME OVER\nY'all come back now!")
                    sys.exit()
            if escape_chance >= 0:
                print("The villain out-maneuvers you and attacks! You do not escape.")

        try:
            monster_health -= int(player_damage)
        except:
            pass
        if monster_health <= 0:
            print(f"{bestiary[monster_ID]['name']} lies dead. You are victorious!\n")
            break

        print(f"{bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
        print ("=========================\n")
        round += 1
        player_health -= int(monster_damage)

        if player_health <= 0:
            print("They got the better of you this time! You are dead.")
            sys.exit()

def showInstructions():
    print('''
CHAD and KEN's RPG GAME
OBJECTIVE: Collect items and weapons - get the loot and get out alive!
--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item, gun]
    USE [item, gun]
    LOOK
    INV/INVENTORY

Type 'help' at any time! Type 'q' to quit!''')

def playerinfo():
    print('')
    print(currentRoom)
    print('=================================')
    print('Inventory :', str(inventory))
    print('Guns :', str(holster))
    print('=================================')


def showStatus(): # display the player's status
    if 'desc' in rooms[currentRoom]:
        print(rooms[currentRoom]['desc'])
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] + rooms[currentRoom]['item_status'] + '.')
    if 'gun' in rooms[currentRoom]:
        print('Out of the corner of your eye, you spot a "' + rooms[currentRoom]['gun'] + '".')
#    print('=================')

def spellreceive(incantation):
 #   print("You received a new spell scroll. Be careful... magic is dangerous!")
 #   incantation = input("Create the magic word to summon your spell! >")
 #   if incantation not in spells:
        print("\nIt feels heavier than you imagined. Cold steel in your hand.")
        print("The gun has successfully been added to your holster. Be careful... guns are dangerous!")

def random_encounter():
    if ((int(rooms[currentRoom]['randenc'])) + 5) >= 10:
        combat()

rooms = {
        'SOUTH MAIN STREET' : {
            'south' : 'SOUTH GATE',
            'east' : 'SALOON',
            'north' : 'NORTH MAIN STREET',
            'west' : 'HOTEL',
            'item' : 'knife',
            'item_status' : ' partially buried in the mud. It is rusty and dull.',
            'randenc' : '5',
            'desc' : 'You are standing on Main Street, which runs from north to south \non the southern edge of town. The road is muddy, rutted out by wagons. \nTo your south is the gate leading out of town to the dusty open prairie and vast nothingness. \nTo your north is the the northern side of town. To your east is a saloon, \nyou can hear the voices and the sound of a player piano inside. \nTo your west is the Hotel, the rooms are small and simple, but the rates are fair.',
            },
        'SOUTH GATE' : {
            'north' : 'SOUTH MAIN STREET',
            'south' : 'PRAIRIE', 
            'randenc' : '0',
            'item' : 'potion',
            'item_status' : ' lashed to a fence post. It is a small leather pouch adorned with beads and eagle feathers. \nSomething is inside.',
            'desc' : 'You stand at the edge of town. As you stare into the empty prairie, \nwatching the wagon tracks as they fade off into the distance, \nyou contemplate your life, and the decisions that brought you to this point.',
            },
        'PRAIRIE' : {
            'north' : 'SOUTH GATE',
            'desc' : 'There is nothing here, except open rolling hills of grass.',
            'randenc' : '0',
        },
        'SALOON' : {
            'gun' : 'pistol',
            'desc' : 'There is loud music coming from the player piano in the corner. \nMen are drinking whiskey and playing poker, everyone seems to be having a good time. \nThrough the back door is an alley.',
            'randenc' : '20',
            'west' : 'SOUTH MAIN STREET',
            'east' : 'EAST ALLEY',
            },
        'HOTEL' : {
            'west' : 'WEST ALLEY',
            'east' : 'SOUTH MAIN STREET',
            'desc' : ' On the west side of Main street. You are in the dining room of the hotel. \nThere are 4 tables, one of wich is occupied by a plump specticaled man reading a paper. \nThe headline reads : BANK ROBBER ESCAPES JAIL AND IS ON THE LOOSE. \nContinuing through the Hotel leads you to an alley on the west side of town.',
            'randenc' : '10',
            'item' : 'brass_knuckles',
            'item_status' : ' carelessly dropped by a cowboy on his way out.',
            },
        'EAST ALLEY' : {
            'north' : 'BANK',
            'west' : 'SALOON',
            'desc' : 'Standing in the alley, you notice no tracks on the muddy ground. To the north is the towns only bank.',
            'randenc' : '0',
            },
        'WEST ALLEY' : {
            'west' : 'GENERAL STORE',
            'east' : 'HOTEL',
            'desc' : 'Boot prints litter the muddy alley. A clear sign of the heavy foot traffic to the General Store to the west.',
            'randenc' : '5',
            },
        'NORTH MAIN STREET' : {
            'south' : 'SOUTH MAIN STREET',
            'north' : 'NORTH GATE',
            'east' : 'JAIL HOUSE',
            'west' : 'COURTHOUSE',
            'item' : 'horse',
            'item_status' : ' his reins tied to a railing in front of the Courthouse to the west. /nI guess the judge said he had to wait outside.',
            'randenc' : '15',
        },
        'JAIL HOUSE' : {
            'west' : 'NORTH MAIN STREET',
            'gun' : 'shotgun',
            'desc' : 'All the cells are empty. To the west is Main Street.',
            'randenc' : '25'
        }, 
        'COURTHOUSE' : {
          'east' : 'NORTH MAIN STREET',
          'desc' : 'You open the door, interrupting a trial. \nAngry turn and are looking at you. \Best skedaddle before you are standing at the gallows next to that poor cowboy up there in chains.',
          'randenc' : '30',
        },
        'NORTH GATE' : {
            'south' : 'NORTH MAIN STREET',
            'desc' : 'At the northen edge of town, you are faced with jagged formitable mountains. \nImmense in both their beauty and stature. There is no escape that direction.',
            'randenc' : '0',
        },
        'BANK' : {
            'south' : 'EAST ALLEY',
            'desc' : 'You burst in through the door on the south side of the building with your gun drawn. \nThe bandana over your face masks your identity. \nYou catch the teller by surprise, he has no time to react.',
            'item' : 'money',
            'item_status' : ' stuffed into a burlap sack. Sitting on the counter.',
            'randenc' : '40',
        },
        'GENERAL STORE' : {
            'east' : 'WEST ALLEY',
            'desc' : 'Dusty but neat. Everything a homesteader needs to survive on this harsh frontier. \nTo the east is the alley which leads back to the Hotel.',
            'item' : 'ham',
            'item_status' : ' sitting on the shelf amongst the other wares. \nThe cured ham seems delicious as you hear your stomach growl. \nThe shopkeep has his back turned as he helps another customer. ',
            'randenc' : '5',
        }
        }

currentRoom = 'SOUTH MAIN STREET'   # player start location

os.system('clear') # start game with a fresh screen
showInstructions()     # show instructions to the player

while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>') # so long as the move does not
        # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])
            random_encounter()
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")
    if currentRoom == rooms['PRAIRIE'] and 'money' in inventory:
        print('You made it out of town, money in hand. Congradulations Partner! \n YOU WIN!')
        sys.exit()
    if move[0] == 'use':
        if move[1].lower() == 'ham' and 'ham' in inventory:
            print('As you bite into the ham, you feel a rush of energy. Your health has been increased!')
            player_health += 10
        if move[1].lower() == 'potion' and 'potion' in inventory:
            print("You eat a small seed from the leather pouch. Your health has been restored!")
            player_health = 20
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            del rooms[currentRoom]['item'] # deletes that item from the dictionary
        elif 'gun' in rooms[currentRoom] and move[1] in rooms[currentRoom]['gun']:
                spellreceive('gun')
                holster += [move[1]]  # add spell to spells
                del rooms[currentRoom]['gun']

        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')

    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc']) # print the look description
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass               
