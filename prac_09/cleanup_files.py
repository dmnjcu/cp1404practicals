"""
CP1404/CP5632 Practical
Cleanup inconsistent song lyrics file names
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            try:
                os.rename(full_name, new_name)
            except FileNotFoundError:
                pass


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    len_filename = len(filename)
    count = 0
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = filename
    for index, value in enumerate(filename):
        if index <= len_filename - 2:
            if value == '_':
                new_name = new_name[:index + count + 1] + new_name[1 + count + index:].capitalize()
            elif value.islower() and filename[index + 1].isupper():
                new_name = new_name[:index + count + 1] + "_" + new_name[1 + count + index:].capitalize()
                count += 1
    return new_name


main()

