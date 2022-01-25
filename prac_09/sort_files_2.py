"""
CP1404/CP5632 Practical
Sort files based on extension and user categorisation
"""
import shutil
import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    extension_to_category = {}
    for filename in os.listdir('.'):
        # Only handle files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension)).strip()
            while category == "":
                print("Invalid category name")
                category = input("What category would you like to sort {} files into? ".format(extension)).strip()
            extension_to_category[extension] = category
        try:
            os.mkdir(extension_to_category[extension])
        except FileExistsError:
            pass
        shutil.move(filename, f'{extension_to_category[extension]}/' + filename)


main()
