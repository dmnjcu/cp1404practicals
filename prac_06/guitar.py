"""
CP1404/CP5632 Practical
Guitar program.
"""
from datetime import date


class Guitar:
    """Represent a Guitar object."""
    VINTAGE_AGE = 50

    def __init__(self, name="", year=0, cost=0):
        """
        Initialise a Guitar instance.
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """
        Get the age of a guitar
        """
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """
        Determine if a guitar is considered vintage or not.
        """
        return True if self.get_age() >= self.VINTAGE_AGE else False
