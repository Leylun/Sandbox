import os
import shutil
from os import path


def main():
    os.chdir('FilesToSort')
    list_of_dirs = ['xlsx', 'xls', 'txt', 'png', 'jpg', 'gif', 'docx', 'doc']
    for direct in list_of_dirs:
        if path.exists(direct):
            pass
        else:
            os.mkdir(direct)
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        else:
            for direct in list_of_dirs:
                if filename[-3:] == direct[-3:]:
                    shutil.move(filename, direct)
                    # or os.rename() (but more typing expensive)


main()
