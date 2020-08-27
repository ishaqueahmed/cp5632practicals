"""
CP5632 Practical 3

Read the list of randomly generated numbers (Fahrenheit temperatures),
convert them to Celsius and write them to temps_output.txt.
"""

import random


def main():
    temps_input = open("temps_input.txt", "r")
    temps_output = open("temps_output.txt", "w")
    for line in temps_input:
        output = convert_to_celsius(float(line))
        temps_output.write("{}\n".format(output))
    temps_output.close()
    temps_input.close()


def convert_to_celsius(fahrenheit):
    """Calculate celsius from fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius):
    """Calculate fahrenheit from celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def generate_randoms():
    """Generate random numbers between -200 and 200"""
    file = open("temps_input.txt", "w")
    for i in range(0, 15):
        num = random.uniform(-200, 200)
        file.write("{}\n".format(num))
    file.close()


main()
