import random 

def rand_num():
    """
    Function that picks a random number between 0, 100
    """
    return random.randint(0,100)
    
def user_guess_input():
    """
    Function that asks for an integer input from the user
    """
    guess =""
    while True:
        guess = input("Please input your guess number between 0 - 100! ")
        if guess.isnumeric():
            return int(guess)

def comp_feed_back(user_guess, pc_choice):
    """
    Function that checks if users input match pc's choice, and gives a feed back if not
    """
    if user_guess == pc_choice:
        found = True
        return "You found the number!! Congrats!!"
    elif user_guess < pc_choice:
        return "The number is larger than the one you guessed!"
    else:
        return "The number is smaller than the one you guessed!"
