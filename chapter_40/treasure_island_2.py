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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
____/______/______/______/______/_____=._o._;o_.--""___/______/______/______/_
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice: Left or Right
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right":\n').lower()
if choice1 == "left":
    # Second choice: Swim or Wait
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across:\n').lower()
    if choice2 == "wait":
        # Third choice: Which door
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # Additional choices for swimming path
        choice2b = input("You chose to swim across. Halfway through, you see a shark. Do you want to 'fight' or 'flee'?\n").lower()
        if choice2b == "fight":
            print("The shark overpowered you. Game Over.")
        elif choice2b == "flee":
            choice2c = input("You managed to swim back to shore. Do you want to 'wait' for a boat or 'build' a raft?\n").lower()
            if choice2c == "wait":
                print("You waited too long and the sun set. Game Over.")
            elif choice2c == "build":
                print("Your raft was successful, and you reached the island safely. You found the treasure! You Win!")
            else:
                print("Invalid choice. Game Over.")
        else:
            print("Invalid choice. Game Over.")
else:
    # Additional paths for right direction
    choice1b = input("You fell into a hole. It's dark and you can either 'climb' out or 'explore' the tunnel. Which do you choose?\n").lower()
    if choice1b == "climb":
        print("The walls are too steep. You couldn't make it. Game Over.")
    elif choice1b == "explore":
        choice1c = input("You found a hidden passage. Do you want to 'follow' it or 'stay'?\n").lower()
        if choice1c == "follow":
            print("The passage led to the treasure room. You Win!")
        elif choice1c == "stay":
            print("You stayed too long, and the air ran out. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid choice. Game Over.")
