import random

min = 1
max = 20
tries = 7
number = random.randint(min, max)

name = input("What's your name?\n")
print("Hello " + name + " . I'm thinking of a number between " + str(min) + " and " + str(max) + ".\n")
for guessesTaken in range (1, tries):
    try:
        guess = int(input("Take a guess\n"))
        if(guess < number):
            print("Your number is too low, try again.\n")
        elif(guess > number):
            print("Your number is too high, try again.\n")
        else:
            break
    except ValueError:
        print("That's not an integer.")

if(guess == number):
    print("Congratulations, you guessed the number!. \n")
    print("You took " + str(guessesTaken) + " guesses.")
else:
    print("You ran out of guesses. The number was " + str(number))