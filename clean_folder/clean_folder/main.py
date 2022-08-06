import sys
import os
from pathlib import Path
from move_and_copy import sort_folder, unpack_arc, show_unknown_extension, show_all_known_extensions


def main():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            main_directory = Path('C:\\SORT_FOLDER\\')
            unknown_directory = Path('C:\\SORT_FOLDER\\unknown')
            if not os.path.isdir(main_directory):
                os.makedirs(main_directory)
            sort_folder(sys.argv[1])
            unpack_arc()
            print(
                f'IT WAS SORTED IN C:\\SORT FOLDER\\\nALL ADDED FOLDERS IS:\n {os.listdir(main_directory)}\nAND ALL FILES IN THIS FOLDERS IS :')
            for f in main_directory.iterdir():
                print(os.listdir(f))
            print(show_all_known_extensions(main_directory))
            print(show_unknown_extension(unknown_directory))
        else:
            print('THER IS NO FOLDER, ENTER CORRECT FOLDER!')
    else:
        print('PLEASE ENTER SOME FOLDER TO SORT')


if __name__ == '__main__':
    main()
