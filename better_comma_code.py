def print_as_string(list):
    if len(list) == 1:
        print(list[0])
    print('{}, and {}'.format(', '.join(list[:-1]), list[-1]))

spam = ['apples', 'bananas', 'tofu','cats']
print_as_string(spam)