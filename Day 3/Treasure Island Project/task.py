print(r'''
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
direction = input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right".').lower()
if direction == "left":
    print("you've made it safely to an island")
    direction_2 = input("You realize that the island is sinking. What do you do? Type 'Swim' or 'Wait'.").lower()
    if direction_2 == "wait":
        print("The island has started to emerge from the water. You notice a large box with 3 sides sticking out of the wet sand on the shore")
        direction_3 = input("Each side of the box is a different color; Red, Blue and Yellow. Type which color you open").lower()
        if direction_3 == "red":
            print("You are burned by fire. GAME OVER")
        elif direction_3 == "blue":
            print("You've been eaten by beasts. GAME OVER")
        elif direction_3 == "yellow":
            print("YOU WIN")
        else:
            print("GAME OVER!")
    else:
        print("you've been devoured by sea snakes. GAME OVER")
else:
    print("you got hit by a bus foo")
    #pushing this as a test
