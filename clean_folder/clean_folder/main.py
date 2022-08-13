import sys
import os
from pathlib import Path
from move_and_copy import sort_folder, unpack_arc, show_unknown_extension, show_all_extensions


def main():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            sort_folder(sys.argv[1])
            folder_sort = Path(os.path.join(os.getcwd(), 'SORTED'))
            dir_unk = folder_sort / 'unknown'
            print(
                f'IT WAS SORTED IN {folder_sort}\nALL ADDED FOLDERS IS:\n {os.listdir(folder_sort)}\nAND ALL FILES IN THIS FOLDERS IS :')
            for f in folder_sort.iterdir():
                print(os.listdir(f))
            print(show_all_extensions(folder_sort))
            print(show_unknown_extension(dir_unk))
        else:
            print('THER IS NO FOLDER, ENTER CORRECT FOLDER!')
    else:
        print('PLEASE ENTER SOME FOLDER TO SORT')


if __name__ == '__main__':
    main()
