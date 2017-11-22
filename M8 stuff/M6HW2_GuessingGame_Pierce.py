# Guessing Game
# 11/12/17
# CTI-110 
# Jamire Pierce

import random
MIN = 1
MAX = 100
stop = 0
    
def main():
    
    again = "y"
    while again == "y" or again == "Y":
        gen_number()
        again = input("Play again? (y = yes): ")


def gen_number():

    print("Generating number...")

    number = random.randint(MIN, MAX)
    #print(number)
    playing = True
    while playing:
        guess = int(input("Guess the number: "))

        if guess == number :
            print("YES CORRECT")
            playing = False
        elif guess > number :
            print("Too high, try again.")
            playing = True
        elif guess < number :
            print("Too low, try again.")
            playing = True
    

    
main()
