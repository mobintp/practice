import random

def computer_guess(x):
    """A function that guesses a number that the user has in mind between 1 and x."""
    # Validate x
    assert isinstance(x, int) and x > 0, "x must be a positive integer"
    
    # Initialize low and high values
    low = 1
    high = x
    
    # Initialize feedback
    feedback = ''
    
    # Initialize history of guesses and feedbacks
    history = {}
    
    # Loop until feedback is C
    while feedback != 'c':
        # Generate a random guess between low and high
        guess = random.randint(low, high)
        
        # Ask for user feedback
        feedback = str(input(f"Is {guess} too high (H), too low (L) or C?: ").lower())
        
        # Validate feedback
        while feedback not in ('h', 'l', 'c'):
            print("Invalid input. Please enter H, L or C.")
            feedback = str(input(f"Is {guess} too high (H), too low (L) or C?: ").lower())
        
        # Check if user lied
        if feedback == 'c':
            # Check if guess matches previous feedbacks
            for key in history:
                if (history[key] == 'h' and guess >= key) or (history[key] == 'l' and guess <= key):
                    print(f"You lied! I think the number was {guess}.")
                    return
            # Print success message
            print(f"Yay! The computer guessed your number {guess}.")
        elif feedback == 'h':
            # Check if guess is within previous range
            if guess < low or guess > high:
                print(f"You lied! I think the number was {guess}.")
                return
            # Check if low and high are both equal to 1
            if low == high == 1:
                print(f"You lied! I think the number was {guess}.")
                return
            # Check if low and high are both equal to the number that the user has in mind
            if low == high == guess:
                print(f"You lied! I think the number was {guess}.")
                return
            # Update high value
            high = guess - 1
            # Update history
            history[guess] = 'h'
        elif feedback == 'l':
            # Check if guess is within previous range
            if guess < low or guess > high:
                print(f"You lied! I think the number was {guess}.")
                return
            # Check if low and high are both equal to x
            if low == high == x:
                print(f"You lied! I think the number was {guess}.")
                return
            # Check if low and high are both equal to x - 1
            if low == high == x - 1: # added condition here
                print(f"You lied! I think the number was {guess}.")
                return
            # Update low value
            low = guess + 1
            # Update history
            history[guess] = 'l'
    
computer_guess(100)
