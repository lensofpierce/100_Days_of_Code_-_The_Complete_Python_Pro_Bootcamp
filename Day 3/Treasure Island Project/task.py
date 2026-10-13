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
path1 = input("You find two paths after you. Choose between left or right: ").lower()
if path1 == "left":
    path2 = input("You see a lake between you and the next land. Do you swim or wait? ").lower()
    if path2 == "wait":
        path3 = input("Wtf? A boat suddenly appeared! You have reached the next land with three doors waiting for you. "
                      "Choose between the red, yellow, or blue door: ").lower()
        if path3 == "yellow":
            print("You found the treasure. You win!")
        elif path3 == "red":
            print("So that's why it's red. It's hiding a huge fire. You're burnt toast. Game over.")
        elif path3 == "blue":
            print("The blue door is where you're due. "
                  "A pack of hungry beasts made you their meal with unli rice. Game over.")
        else:
            print("Game over.")
    else:
        print("A monster trout is waiting for you. You got devoured. Game over.")
else:
    print("Oh no! All roads sank other than the left road. Unfortunately, you fell. Game over.")