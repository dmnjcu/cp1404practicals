"""
CP1404/CP5632 Practical
Taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """
    Program to simulate using Taxi and SilverServiceTaxi classes.
    """
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    taxi_choice = None
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").strip()
    user_choice = user_choice.lower()
    while user_choice != 'q':
        if user_choice == 'c':
            print('Taxis available:')
            display_taxis(taxis)
            len_taxis = len(taxis)
            if len_taxis > 0:
                selected_taxi = int(input("Choose taxi: ").strip())
                while selected_taxi < 0 or selected_taxi >= len_taxis:
                    print("Invalid taxi choice")
                    selected_taxi = int(input("Choose taxi: ").strip())
                taxi_choice = taxis[selected_taxi]

        elif user_choice == 'd':
            if not taxi_choice:
                print("You need to choose a taxi before you can drive")
            else:
                taxi_choice.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                taxi_choice.drive(distance_to_drive)
                fare = taxi_choice.get_fare()
                total_bill += fare
                print("Your {} trip cost you ${:.2f}".format(taxi_choice.name, fare))
        else:
            print("Invalid choice")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        user_choice = input(">>> ").strip()
        user_choice = user_choice.lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """
    Function to display a list of taxis for users to choose from.
    """
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


main()

