"""
CP1404/CP5632 Practical
Quick pick program
"""
import random


MINIMUM = 1
MAXIMUM = 45
NUMBERS_ON_EACH_LINE = 6


def main():
    """
    Get a number and then generates many lines of output.
    """
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid input")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        list_number = []
        for j in range(NUMBERS_ON_EACH_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in list_number:
                number = random.randint(MINIMUM, MAXIMUM)
            list_number.append(number)
        list_number.sort()
        print(" ".join("{:2}".format(number) for number in list_number))


main()
