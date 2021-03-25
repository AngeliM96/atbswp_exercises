def collatz(number):
    if (number % 2 == 0):
        numberAux = number // 2
        print(numberAux)
        return numberAux
    elif (number % 2 == 1):
        numberAux = 3 * number + 1
        print(numberAux)
        return numberAux

try:
    askNumber = int(input("Enter a number: \n"))
except ValueError:
    print("Please enter a valid integer.")

while(askNumber != 1):
    askNumber = collatz(askNumber)