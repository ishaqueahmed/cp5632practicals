"""
CP5632 Practical 3

Program to get password from user and display it as asterisks
"""


def main():
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    """Replace password characters with asterisks"""
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    """Validate password given by user"""
    password = input("Enter your password: ")
    while len(password) < 6:
        print("Password must have 6 or more characters")
        password = input("Enter your password: ")
    return password


main()
