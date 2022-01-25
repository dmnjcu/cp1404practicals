"""
CP1404/CP5632 Practical
Taxi class tests
"""
from taxi import Taxi


def test_taxi():
    """Tests for Taxi class."""
    name = "Prius 1S"
    fuel = 100

    taxi_test = Taxi(name, fuel)
    taxi_test.drive(40)
    print(taxi_test)
    taxi_test.start_fare()
    taxi_test.drive(100)
    print(taxi_test)


test_taxi()
