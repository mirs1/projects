# MS February 2, 2019
# "Guess the number!" game
# The purpose of this program/game is to have the player correctly guess a randomly generated number.


# Notes
# Feb. 03 2019 - Complete
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Generate random number for player to guess.
import random

# Ask player's name and have player guess the number.
welcomePlayer = input("Hi, welcome to 'Guess a Number!'. Please tell us your name ")
playerName = str(welcomePlayer)

number = random.randint(1, 20)
print(number)

# Cycle through player's guesses until player enters correct number. Player must enter an integer. Program
# will let player know if the guess is higher or lower than the randomly generated number.
# Player is given the option to play again once he or she guesses correctly.
while True:
    try:
        playerGuess = int(input("Hello " + playerName + ". Please guess a number between 1 - 3 "))
    except ValueError:
        print("Sorry, you must enter a numeric value")
        continue
    if playerGuess > number:
        print("You've guess too high, please try again ")
        continue
    elif playerGuess < number:
        print("You've guessed too low, please try again ")
        continue
    else:
        playAgain = input("Congratulations " + playerName + "! " +
                          "You've guessed correctly! Would you like to play again? ").lower()
        if playAgain.lower() == "Yes".lower() or playAgain.lower() == "Y".lower():
            number = random.randint(1, 20)
            print(number)
            continue
        else:
            print("Thanks for playing!")
            break


