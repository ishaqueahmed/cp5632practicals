"""
CP5632 Practical 1

The program requests for the user's name. Then a menu is displayed with three
options: Hello, Goodbye and Quit. Based on user selection, the name is
displayed until the user quits.
"""

name = input("Enter name: ")

menu_input = input("(H)ello \n(G)oodbye \n(Q)uit \n>>> ")
while menu_input.upper() != "Q":
    if menu_input.upper() == "H":
        print("Hello {}".format(name))
    elif menu_input.upper() == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid choice")
    menu_input = input("(H)ello \n(G)oodbye \n(Q)uit \n>>> ")
print("Finished.")
