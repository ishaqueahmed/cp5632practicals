"""
CP5632 Practical 5

Program to get names and emails from the user and add them to dictionary
"""


def main():
    email_collection = {}

    email = input("Email: ")
    while email != "":
        parts = (email.split("@")[0].split("."))
        name = " ".join(parts).title()

        verify_name = input("Is your name {}? (y/n) ".format(name)).lower()
        if verify_name == "n":
            name = input("Name: ")
        email_collection[name] = email
        email = input("Email: ")

    print()
    for name, email in email_collection.items():
        print("{} ({})".format(name, email))


main()
