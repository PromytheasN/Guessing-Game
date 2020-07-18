import random 

def rand_num():
    return random.randint(0,100)
    
def user_guess_input():
    guess =""
    while True:
        guess = input("Please input your guess number! ")
        if guess.isnumeric():
            return int(guess)
