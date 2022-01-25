"""
CP1404/CP5632 Practical
SilverServiceTaxi class tests
"""
from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """Tests for SilverServiceTaxi class."""

    taxi_test = SilverServiceTaxi("Taxi", 100, 13)
    print('Before driving')
    print(taxi_test)
    taxi_test.drive(13)
    print('\nAfter driving')
    print(taxi_test)
    print('Fare: ${:.2f}'.format(taxi_test.get_fare()))


test_silver_service_taxi()
