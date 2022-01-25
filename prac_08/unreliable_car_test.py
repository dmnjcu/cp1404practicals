"""
CP1404/CP5632 Practical
UnreliableCar class tests
"""
from unreliable_car import UnreliableCar


def test_unreliable_car():
    """Tests for UnreliableCar class."""

    good_car = UnreliableCar("Good car", 100, 100)
    bad_car = UnreliableCar("Bad car", 100, 0)

    # Drive 2 cars multiple times and show the distancethey drove
    for i in range(1, 10):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km\n".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print("\nFinal states")
    print(good_car)
    print(bad_car)


test_unreliable_car()
