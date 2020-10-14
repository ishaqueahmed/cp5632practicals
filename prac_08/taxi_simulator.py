"""
CP5632 Practical 8

Taxi Simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Run the taxi simulator"""
    bill_to_date = 0
    current_taxi = None
    print("Lets drive!")
    display_options(current_taxi, bill_to_date)
    print("Taxis are now:")
    for taxi in TAXIS:
        print("{} - {}".format(TAXIS.index(taxi), taxi))


def drive_taxi(current_taxi, bill_to_date):
    """Drive the selected taxi"""
    if current_taxi is not None:
        drive_distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(drive_distance)
        bill_to_date += current_taxi.get_fare()
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
        print("Bill to date: ${:.2f}".format(bill_to_date))
        return bill_to_date
    else:
        print("You have not selected a taxi")


def display_taxis(bill_to_date):
    """List the taxis available to choose from"""
    print("Taxis available:")
    for taxi in TAXIS:
        print("{} - {}".format(TAXIS.index(taxi), taxi))
    taxi_id = int(input("Choose taxi: "))
    if taxi_id < len(TAXIS):
        current_taxi = TAXIS[taxi_id]
        print("Bill to date: ${:.2f}".format(bill_to_date))
        return current_taxi
    else:
        print("Invalid taxi id")


def display_options(current_taxi, bill_to_date):
    """Display a list of options to the user"""
    user_choice = input("q)uit, c)hoose taxi, d)rive \n>>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            current_taxi = display_taxis(bill_to_date)
        elif user_choice == "d":
            bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid choice")
        user_choice = input("q)uit, c)hoose taxi, d)rive \n>>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill_to_date))


main()
