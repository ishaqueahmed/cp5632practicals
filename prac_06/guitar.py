"""CP5632 Practical 6 - Guitar class code"""


class Guitar:
    """Represent a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return string information about a Guitar instance"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of the guitar"""
        return 2020 - self.year

    def is_vintage(self):
        """Return whether guitar age is 50 or more"""
        return self.get_age() >= 50
