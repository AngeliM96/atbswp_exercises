'''
Program that chooses a number randomly and makes the user try to guess it
'''

# Random library to generate the number to guess
import random

# Variables so we dont have to hardcode any number
min = 1
max = 20
tries = 7
number = random.randint(min, max)

# We prompt the user for his/her name
name = input("What's your name?\n")
# We greet the user and say from which to which number it is the number we are thinking of
print("Hello " + name + " . I'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")

# While there's still guesses left we say if the guess was to high or too low
for guessesTaken in range (1, tries):
    try:
        guess = int(input("Take a guess\n"))
        if(guess < number):
            print("Your number is too low, try again.\n")
        elif(guess > number):
            print("Your number is too high, try again.\n")
        else:
            break
    # We check that the answer is an integer
    except ValueError:
        print("That's not an integer.")

# If the user guessed the number we congratulate him/her
if(guess == number):
    print("Congratulations, you guessed the number!. \n")
    print("You took " + str(guessesTaken) + " guesses.")
# Else, we tell him/her what number we're thinking
else:
    print("You ran out of guesses. The number was " + str(number))