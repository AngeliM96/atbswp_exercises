'''
This is an exercise called Comma Code. The objetive is to convert a list to a string formatted as 'element, element and element'
'''
def print_as_string(list):
    # We create an empty list
    string = ""
    # For each element in the list
    for i in range(len(list)):
        # If it's the last one, it add 'and' and the element to the string
        if(i+1 == len(list)):
            string += 'and ' + list[i]
        # if it isn't the last one, it adds the element and a comma to the string
        else:
            string += list[i] + ', '
    print(string)

# The list of elements that we want to print in a string
spam = ['apples', 'bananas', 'tofu', 'cats']
# We call the function
print_as_string(spam)