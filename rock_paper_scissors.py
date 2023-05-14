import random
from colorama import Fore, Back, Style

option_list = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(option_list)
invalid_input = False
print("Welcome to the Rock, Paper, Scissors Game!!! Enjoy!")
print("Please choose from the following: 'Rock', 'Paper' or 'Scissors'!")
while True:
    if invalid_input:
        player_move = input("->: ")
        if player_move.lower() == "rock":
            break
        elif player_move.lower() == "paper":
            break
        elif player_move.lower() == "scissors":
            break
        else:
            print("Invalid input.Please try again")
            invalid_input = True
            continue
    else:
        player_move = input("Write your move here->: ")
        if player_move.lower() == "rock":
            break
        elif player_move.lower() == "paper":
            break
        elif player_move.lower() == "scissors":
            break
        else:
            print("Invalid input.Please try again")
            invalid_input = True
            continue

win_counter = 0
lost_counter = 0
draw_counter = 0

if player_move.lower() == "rock" and computer_move.lower() == "scissors" or \
        player_move.lower() == "paper" and computer_move.lower() == "rock" or \
        player_move.lower() == "scissors" and computer_move.lower() == "paper":
    win_counter += 1
    print(Fore.CYAN+f"The Computer chose {computer_move}.")
    print(Fore.YELLOW + "You win")

elif computer_move.lower() == "rock" and player_move.lower() == "scissors" or \
        computer_move.lower() == "paper" and player_move.lower() == "rock" or \
        computer_move.lower() == "scissors" and player_move.lower() == "paper":
    lost_counter += 1
    print(Fore.CYAN+f"The Computer chose {computer_move}.")
    print(Fore.RED + "You lose.Better luck next time.")

else:
    draw_counter += 1
    print(Fore.CYAN + f"The Computer chose {computer_move}")
    print(Fore.GREEN + "It is a draw.")

print("Would you like to play more??")