"""
CP5632 Practical 4

Program to ask the user to enter their username and grant/deny access.
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username_input = input("Enter your username: ")
    if username_input in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
