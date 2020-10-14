"""
CP5632 Practical 8

Client code to test out UnreliableCar class
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test code for UnreliableCar class"""
    car = UnreliableCar("A useless Car", 200, 50)
    car.drive(50)
    print(car)
    another_car = UnreliableCar("Another useless car", 100, 30)
    another_car.drive(50)
    print(another_car)


main()
