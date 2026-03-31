import random

print("Welcome to RPS")
choice = int(input("Choose 0 for rock, 1 for scissors 2 for paper:"))

game_choice = ["rock","scissors","paper"]

comp_choice = random.randint(0,2)

if comp_choice==choice:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. It's a draw")

elif choice==0 and comp_choice==1:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. You win")

elif choice==0 and comp_choice==2:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. You lose")

elif choice==1 and comp_choice==2:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. You win")

elif choice==1 and comp_choice==0:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. You lose")

elif choice==2 and comp_choice==0:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. You win")

elif choice==2 and comp_choice==1:
    print(f"You chose {game_choice[choice]}. The computer chose {game_choice[comp_choice]}. You lose")

else:
    print("Invalid numbers entered")