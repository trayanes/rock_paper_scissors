import random
from colorama import Fore

win_counter = 0
lost_counter = 0
draw_counter = 0

option_list = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(option_list)
print("Welcome to the Rock, Paper, Scissors Game!!! Enjoy!")
print("Please choose from the following: 'Rock', 'Paper' or 'Scissors'!")
while True:
    player_move = input("Write your move here->: ")
    if player_move.lower() != "rock" and player_move.lower() != "paper" and player_move.lower() != "scissors":
        print("Invalid input.Please try again")
        continue
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
    while True:
        another_try = input(Fore.MAGENTA + "Do you want to play again? yes / no: ")
        if another_try.lower() == "yes" or another_try.lower() == "y":
            invalid_input = False
            break
        elif another_try.lower() == "no" or another_try.lower() == "n":
            invalid_input = True
            print("Okay , It was a pleasure!")
            break
        else:
            while True:
                print(Fore.MAGENTA + "That was not a valid answer.Please give another answer: ")
                answer = input()
                if answer.lower() == "yes" or answer.lower() == "y":
                    invalid_input = False
                    break
                else:
                    print("Okay , It was a pleasure!")
                    invalid_input = True
                    break
            if not invalid_input:
                break
            else:
                break
    if not invalid_input:
        continue
    else:
        break
print("Some statistics:")
print(f"Wins:{win_counter}")
print(f"Loses:{lost_counter}")
print(f"Draws:{draw_counter}")