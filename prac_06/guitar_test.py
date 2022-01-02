"""
CP1404/CP5632 Practical
Basic manual tests for Guitar class
"""
from guitar import Guitar


def test():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 8, other.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


test()
