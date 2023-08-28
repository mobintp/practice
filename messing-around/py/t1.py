import random as rd

def guess(x):
    random_num = rd.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print(f"the number is higher that {guess}")
        elif guess > random_num:
            print(f"the number is lower than {guess}")

    print(f"well guessed {random_num} correctly. have fun.")
    
guess(10)