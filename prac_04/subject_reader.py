"""
CP5632 Practical 4

Program to read the data from file subject_data.txt, format it, and display the results
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_details(data)


def display_details(data):
    for values in data:
        print("{} is taught by {:^12} and has {:>3} students".format(values[0], values[1], values[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data


main()
