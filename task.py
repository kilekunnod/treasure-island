print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go?"
                'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\n'
                    'Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There\'s a house with three doors.\n'
                        'One red, one yellow, and one blue. Which colour do you choose?\n'
                        'Type "red", "yellow" or "blue" to select a colour: ').lower()
        if choice3 == "red":
            print("You've entered a house filled with fire, and you have been burned by it. Game over!")
        elif choice3 == "yellow":
            print("You have found the treasure. You win!")
        elif choice3 == "blue":
            print("You've entered a house filled with beasts, and they have devoured you. Game over!")
        else:
            print("You chose a door that doesn't exist!")
    else:
        print("You have chosen to swim, and hence, you were attacked by angry trouts. Game over!")
else:
    print("You have decided to go left, and hence, fallen into a hole. Game over!")