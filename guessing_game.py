"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

Created via VS Code IDE

"""

import random


def start_game():
    name = input("Hello, welcome to the number guessing game. Please enter your name ")
    num = random.randint(1, 15)
    attempts = 0

    while True:
        try:
            guess = int(input("{}, please select a random number between 1 through 15. ".format(name)))
            attempts += 1
            if guess < 1:
                print("Sorry, this number is outside of the stated range 1 and 15")
            elif guess > 15:
                print("Sorry, this number is outside of the stated range range 1 and 15")
            elif guess > num:
                print("It's lower")
            elif guess < num:
                print("It's higher")
            else:
                if guess == num:
                    print("Great job {} ! you have selected the correct answer in a total of {} attempts".format(name, attempts))
                break

        except ValueError:
            print("The following value is not a number. Please try again and select a number between 1 and 15")
            continue

    newgame = input("Thanks for playing {}. Would you like to play again? Yes/No ".format(name))
    if newgame.lower() == "yes":
        start_game()
    else:
        print("Good bye and have a great day!"))


    


    
start_game()