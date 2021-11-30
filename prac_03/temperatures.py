"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
OPERATION = """
Select operation:
[C] Convert Celsius to Fahrenheit
[F] Convert Fahrenheit to Celsius
[B] Back to menu
[X] Exit
"""


def main():
    """
    Temperature conversion program
    """
    print(OPERATION)
    user_choice = input('Operation: ')
    user_choice = user_choice.upper()

    while user_choice != 'X':
        if user_choice == 'C':
            celsius = float(input('Celsius: '))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f} C corresponds to {fahrenheit:.2f} F")
        elif user_choice == 'F':
            fahrenheit = float(input('Fahrenheit: '))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f} F corresponds to {celsius:.2f} C")
        elif user_choice != 'B':
            print("Invalid operation")
        else:
            print(OPERATION)
        user_choice = input('Operation: ')
        user_choice = user_choice.upper()
    print('Exiting...')


def convert_celsius_to_fahrenheit(celsius):
    """
    Convert celsius to fahrenheit.
    """
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert fahrenheit to celsius.
    """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
