"""
CP1404/CP5632 - Practical
Program to determine score status, with function
"""
import random


def main():
    """
    Get score from user and show its status.
    """
    score = get_score()
    print(get_result(score))
    random_score = get_random_score()
    print(f"Random score: {random_score}")
    print(get_result(random_score))


def get_score():
    """
    Get score from user
    """
    score = float(input("Enter score: "))
    return score


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


def get_random_score():
    """
    Get random score
    """
    score = round(random.uniform(0, 100), 2)
    return score


main()
