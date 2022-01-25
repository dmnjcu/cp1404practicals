"""
CP1404/CP5632 Practical
Sort files based on extension
"""
import shutil
import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Only handle files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, f'{extension}/' + filename)


main()
