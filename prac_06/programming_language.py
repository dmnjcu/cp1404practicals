"""
CP1404/CP5632 Practical
Programming Language class.
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    REFLECTION_TYPE = {
        True: 'Yes',
        False: 'No',
    }

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """
        Initialise a ProgrammingLanguage instance.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """
        Return string representation of a ProgrammingLanguage.
        """
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.REFLECTION_TYPE[self.reflection], self.year)

    def is_dynamic(self):
        """
        Determine if language is dynamically typed.
        """
        return self.typing == "Dynamic"
