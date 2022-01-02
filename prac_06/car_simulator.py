"""
CP1404/CP5632 Practical
Car Driving Simulator
"""
from car import Car


MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():
    """Car simulator program, demonstrating use of Car class."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(100, name)
    print(car)
    print(MENU)

    choice = input("Enter your choice: ").strip().lower()
    while choice != "q":
        if choice == "d":
            distance = int(input("How many km do you wish to drive? ").strip())
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive? "))
            actual_distance = car.drive(distance)
            if car.fuel == 0:
                print("The car drove {}km and ran out of fuel".format(actual_distance))
            else:
                print("The car drove {}km".format(actual_distance))
        elif choice == "r":
            fuel_to_add = int(input("How many units of fuel do you want to add to the car? ").strip())
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input("How many units of fuel do you want to add to the car? ").strip())
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel.".format(fuel_to_add))
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").strip().lower()

    print()
    print("Good bye {}'s driver.".format(car.name))


main()
