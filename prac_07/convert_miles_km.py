"""
CP5632 Practical 7

Kivy GUI program to convert from miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder

CONVERSION_FACTOR = 1.609


class MilesToKilometres(App):
    """Kivy App for squaring a number"""

    def build(self):
        """Build the app from the .kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_result(self):
        """Convert from miles to kilometres"""
        input_value = self.get_validated_input()
        result = input_value * CONVERSION_FACTOR
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment_value):
        """Increment the input by a given value"""
        input_value = self.get_validated_input()
        input_value += increment_value
        self.root.ids.input_value.text = str(input_value)

    def get_validated_input(self):
        """Validate the input"""
        try:
            input_value = float(self.root.ids.input_value.text)
            return input_value
        except ValueError:
            return 0


MilesToKilometres().run()
