"""
CP5632 Practical 8

UnreliableCar class inheriting from Car class
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of Car class which includes reliability value"""
    def __init__(self, name, fuel, reliability):
        """Initialise the UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if the randomly generated value is less than the reliability value provided"""
        random_value = randint(0, 100)
        if random_value < self.reliability:
            distance = super().drive(distance)
        else:
            distance = 0
        return distance
