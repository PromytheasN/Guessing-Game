import random 

"""
Function that picks a random number between 0, 100
"""
def rand_num():

    return random.randint(0,100)


"""
Function that asks for an integer input from the user
"""    
def user_guess_input():

    guess =""
    while True:
        guess = input("Please input your guess number between 0 - 100! ")
        if guess.isnumeric():
            return int(guess)

"""
Function that checks if users input match pc's choice, and gives a feed back if not
"""
def comp_feed_back(user_guess, pc_choice):

    if user_guess == pc_choice:
        found = True
        return "You found the number!! Congrats!!"
    elif user_guess < pc_choice:
        return "The number is larger than the one you guessed!"
    else:
        return "The number is smaller than the one you guessed!"

    
pc_choice = rand_num()
found = False
while found == False:
    
    found = comp_feed_back(user_guess_input(), pc_choice)
