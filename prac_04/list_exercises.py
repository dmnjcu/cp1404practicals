def main():
    """
    prompts the user for 5 numbers, stores each of these in a list and then output various
    interesting things.
    """
    numbers = []
    for i in range(5):
        input_number = int(input("Number: "))
        numbers.append(input_number)
    print_number(numbers)
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', \
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', \
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("\nEnter username: ")
    print(check_username(username, usernames))


def print_number(numbers):
    """
    Print out some interesting stuff about lists of numbers.
    """
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(sum(numbers)/len(numbers)))


def check_username(username, usernames):
    """
    Check if the user is authenticated.
    """
    if username not in usernames:
        return "Access granted"
    else:
        return "Access denied"


main()
