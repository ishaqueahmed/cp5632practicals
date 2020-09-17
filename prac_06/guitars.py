"""CP5632 Practical 6 - Client code for Guitar class"""

from prac_06.guitar import Guitar


def main():
    """Code to add guitars from user to a list and display the result"""
    print("My guitars!")
    guitars = []
    is_loop_running = True
    while is_loop_running:
        name = input("\nName: ")
        year = input("Year: ")
        cost = input("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, " added")
        add_another = input("\nDo you want to add another guitar? (y/n) ").lower()
        if add_another == "n":
            is_loop_running = False

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print("Guitar {}: {} ({}), worth $ {:,.2f} {}".
              format(i, guitar.name, guitar.year, guitar.cost,
                     "(vintage)" if guitar.is_vintage() else ""))


main()
