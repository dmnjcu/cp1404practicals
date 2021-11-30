"""
CP1404/CP5632 - Practical
Program to determine score status, with function
"""
import random


def main():
    """
    Ask the user for a number of scores and generate that many random numbers and write them to a file
    """
    number_scores = int(input("Number of scores: "))
    while number_scores <= 0:
        print("Invalid number of scores")
        number_scores = int(input("Number of scores: "))
    write_file(number_scores)


def get_result(score):
    """
    Determine the status of the given score.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def write_file(number_scores):
    """
    Write a file to save scores and their status
    """
    file = open('results.txt', 'w')
    for i in range(number_scores):
        score = random.randint(0, 100)
        result = get_result(score)
        file.write(f"{score} is {result}\n")
    file.close()
    return file


main()
