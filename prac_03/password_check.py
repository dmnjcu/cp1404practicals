"""
CP1404/CP5632 - Practical
Get a password with minimum length and display asterisks
"""
MINIMUM_PASSWORD_LENGTH = 8


def main():
    """
    Get a password of valid size and prints asterisks based on its length
    """
    password = get_password()
    asterisks = get_asterisks(password)
    print(asterisks)


def get_password():
    """
    Asks the user for a password, with error-checking to and repeat if the password doesn't meet a minimum length.
    """
    password = input(f"Please enter your password, password must be at least {MINIMUM_PASSWORD_LENGTH} characters: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password is too short")
        password = input(f"Please enter your password, password must be at least {MINIMUM_PASSWORD_LENGTH} characters: ")

    return password


def get_asterisks(password):
    """
    Print asterisks as long as the word.
    """
    asterisks = '*' * len(password)
    return asterisks


main()
