def print_as_string(list):
    string = ""
    for i in range(len(list)):
        if(i+1 == len(list)):
            string += 'and ' + list[i]
        else:
            string += list[i] + ', '
    print(string)

spam = ['apples', 'bananas', 'tofu','cats']
print_as_string(spam)