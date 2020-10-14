"""
CP5632 Practical 8

Client code to test out SilverServiceTaxi class
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Code to test out SilverServiceTaxi class"""
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)
    print("Fare: ${:.2f}".format(hummer.get_fare()))


main()
