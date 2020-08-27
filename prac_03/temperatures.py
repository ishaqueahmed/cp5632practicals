"""
CP5632 Practical 3

Program to convert between Celsius and Fahrenheit temperatures
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_input("Celsius: ")
            fahrenheit = convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = get_input("Fahrenheit: ")
            celsius = convert_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_input(prompt):
    """Get input from the user"""
    value = float(input(prompt))
    return value


def convert_to_celsius(fahrenheit):
    """Calculate celsius from fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius):
    """Calculate fahrenheit from celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
