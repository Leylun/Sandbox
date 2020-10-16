import os
import shutil
from os import path


def main():
    os.chdir('FilesToSort')
    list_of_dirs = ['xlsx', 'xls', 'txt', 'png', 'jpg', 'gif', 'docx', 'doc']
    user_responses = []
    for direct in list_of_dirs:
        user_responses.append(input("What category would you like to sort {} files into?".format(direct)))
    for direct_path in list(dict.fromkeys(user_responses)):
        if path.exists(direct_path):
            pass
        else:
            os.mkdir(direct_path)
    for filename in os.listdir('.'):
        for direct in list_of_dirs:
            if filename[-3:] == direct[-3:]:
                shutil.move(filename, user_responses[list_of_dirs.index(direct)])


main()
