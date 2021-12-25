'''we are going to write a program that generates a random number and ask the user to guess it
if the players guess is higher than the acutual number the program displays 'lower number please'
similary the user guess is too low then it prints 'higher number please'. when the user guess the correct
display the number of guesses the player use to arrive at the number.'''

import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if (userGuess == randNumber):
        print("You guessed it right")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong, Enter a smaller number")
        else:
            print("You guessed it wrong, Enter a larger number")

print(f"Your guessed in the number in {guesses} guesses ")


