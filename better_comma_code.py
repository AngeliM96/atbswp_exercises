'''
This is a better version of the exercise 'comma code'. Using the format and join functions
'''
def print_as_string(list):
    # If the list only has one element, it prints it
    if len(list) == 1:
        print(list[0])
    # Else, it joins all the elements but the last one, separating each of them with a comma, and then adds the last one using format
    print('{}, and {}'.format(', '.join(list[:-1]), list[-1]))

# The list of elements that we want to print in a string
spam = ['apples', 'bananas', 'tofu', 'cats']
# We call the function
print_as_string(spam)