# Rock \ Paper Scissor games

import random

user_wins = 0
computer_wins =0

game_list = ["rock", "paper", "scissors"]

#Rock: Represented by a closed fist. It crushes scissors but is covered by paper.
#Paper: Represented by an open hand. It covers rock but is cut by scissors.
#Scissors: Represented by a fist with the index and middle fingers extended, forming a V.
# It cuts paper but is crushed by rock

print("**************************************")
print("**** Rock - Paper - Scissors Game ****")
print("**************************************\n")


options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose between Rock, Paper, Scissors or Q to quit:  ").lower()

    if user_input.lower() == 'q':

        break

    elif user_input not in options:
        print("incorrect choice")
        continue

    else:
        random_number = random.randint(0,2)

        computer_input = options[random_number]

        print(f"Computer chooses {computer_input}\n")

        if user_input =="Rock" and computer_input == "scissors":
            print("You won\n")
            user_wins += 1
        elif user_input =="paper" and computer_input == "rock":
            print("You won\n")
            user_wins += 1
        elif user_input =="scissors" and computer_input == "paper":
            print("You won\n")
            user_wins += 1
        elif user_input == computer_input:
            print("Tie\n")
        else:
            print("Computer won")
            computer_wins += 1


print(f"\nYou have won {user_wins} time(s) and Computer has won {computer_wins} time(s)")

print("\nGoodbye")









