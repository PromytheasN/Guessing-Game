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
        print ("You found the number!! Congrats!!")
        return True
    elif user_guess < pc_choice:
        print("The number is larger than the one you guessed!")
        return False
    else:
        print("The number is smaller than the one you guessed!")
        return False
    

    
pc_choice = rand_num()
found = False
while not found:
    
    found = comp_feed_back(user_guess_input(), pc_choice)
