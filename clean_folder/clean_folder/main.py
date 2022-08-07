import sys
import os
from pathlib import Path
from move_and_copy import sort_folder


def main():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            sort_folder(sys.argv[1])
        else:
            print('THER IS NO FOLDER, ENTER CORRECT FOLDER!')
    else:
        print('PLEASE ENTER SOME FOLDER TO SORT')


if __name__ == '__main__':
    main()
