"""CP5632 Practical 6 - Client code for ProgrammingLanguage"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Use the ProgrammingLanguage class"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    languages_list = [ruby, python, visual_basic]
    print("\nThe dynamically typed languages are:")
    for language in languages_list:
        if language.is_dynamic():
            print(language.name)


main()
