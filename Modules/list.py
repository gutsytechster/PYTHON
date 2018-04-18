#!/usr/bin/env python3

import os
import sys
def view_dir(path='.'):
    """
    This function prints all files and directories in the given directory.
    :args path: Path to the directory, default is the current directory
    """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end = ' ')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Only one argument is required!\nCurrent directory is listed.")
        view_dir()
    else:
        view_dir(sys.argv[1])

