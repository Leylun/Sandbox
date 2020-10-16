"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os
from os import path
import re


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    if path.exists("temp"):
        pass
    else:
        os.mkdir('temp')

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        else:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    return_name = ""
    # print("Given Name: {}".format(filename))
    new_name = re.split('(?=[A-Z])', filename.replace(".TXT", ".txt"))
    for word in new_name:
        return_name = return_name + " " + word.title()
    # print("Camel Name: {}".format(return_name))
    new_name = return_name.replace(" ", "_").replace("__", "_").replace("(_", "(").replace(".Txt", ".txt")
    new_name = new_name[1:]
    return new_name


main()
