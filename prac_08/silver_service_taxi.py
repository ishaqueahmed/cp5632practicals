"""
CP5632 Practical 8

SilverServiceTaxi class inheriting from Taxi class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Child of Taxi class, which has fanciness and flagfall values"""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string similar to Taxi object with flagfall information"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return fare same as Taxi object but with flagfall added"""
        return super().get_fare() + self.flagfall
