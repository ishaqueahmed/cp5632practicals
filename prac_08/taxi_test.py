"""
CP5632 Practical 8

Client code to test out taxi class
"""

from prac_08.taxi import Taxi


def main():
    """Code to test out taxi class"""
    taxi = Taxi("Prius 1", 100, 1.23)
    taxi.drive(40)
    print(taxi)
    print("Fare: ", taxi.get_fare())
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Fare: ", taxi.get_fare())


main()
