"""CP5632 Practical 6 - ProgrammingLanguage class code"""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Initialise an instance for a programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string information about ProgrammingLanguage object"""
        return "{}, {} Typing, Reflection={}, First appeared in {}"\
            .format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Returns information about whether a program is dynamically typed"""
        return self.typing == "Dynamic"
