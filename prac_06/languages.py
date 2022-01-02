"""
CP1404/CP5632 Practical
Programming Language client code.
"""
from programming_language import ProgrammingLanguage


def main():
    """Run simple tests on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for item in languages:
        if item.is_dynamic():
            print(item.name)


main()
