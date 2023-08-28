import random
import sys

# create a dictionary to store the rules of the game
rules = {
    "r": "s", # rock beats scissors
    "p": "r", # paper beats rock
    "s": "p"  # scissors beats paper
}

# start a while loop to keep the game running until the user exits
while True:
    # get the user's choice and generate a random choice for the computer
    user = input("'r' for rock, 'p' for paper, 's' for scissor: ( and 'e' for exit the program.): ")
    comp = random.choice(["r", "p", "s"])

    # compare the choices and print the result
    if user == comp:
        print(f"It's a tie. You both chose {user}.")
    elif user == "e":
        print("good bye!")
        break
    elif user not in ["r", "p", "s"]:
        print("please enter 'r', 'p' or 's' as i said.")
    elif rules[user] == comp:
        print(f"You won! {user} beats {comp}.")
    else:
        print(f"You lost. {comp} beats {user}.")
