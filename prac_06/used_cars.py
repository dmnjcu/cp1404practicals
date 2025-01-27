"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""
from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "First car")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo_car = Car(100, "limo")
    limo_car.add_fuel(20)
    print(limo_car.fuel)
    limo_car.drive(115)
    print(limo_car.odometer)


main()
