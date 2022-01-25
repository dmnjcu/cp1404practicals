"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from random import randint
from car import Car


class UnreliableCar(Car):
    """An unreliable version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, based on reliability."""
        random_number = randint(1, 100)
        if self.reliability <= random_number:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
