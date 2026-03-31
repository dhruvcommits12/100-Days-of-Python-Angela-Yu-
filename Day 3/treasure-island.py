#triple quotes are used for printing multi-line strings

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
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('''
Welcome to Treasure Island
Your mission is to find the treasure
      ''')

choice_1 = input("Where do you wanna go ? Type L for left or R for right:")

if choice_1=='L':
    print("You fell into a river")
    choice_2 = input("What do you wanna do ? Type S to swim or W to wait:")
    if choice_2=='W':
        print("A yacht came to the rescue & dropped you to a hut")
        print("You have 3 coloured doors in front of you.. which one do you wanna choose?")
        choice_3=input("Type Y for yellow, R for red, B for blue:")
        if choice_3=='R':
            print("You were burned by fire. Game over")
        elif choice_3=='B':
            print("You were eaten by beasts. Game over")
        else:
            print("Yay! You found the treasure")
    else:
        print("You were attacked by a trout. Game over")
else:
    print("You fell into a hole. Game over")
         



