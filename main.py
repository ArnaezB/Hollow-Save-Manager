import os.path
import os
from platform import system
from re import match
from shutil import copy

def show_saves(saves: list):
    print("ORDER OF SAVES:")
    for index, value in enumerate(saves):
        print("\t{}: {}".format(index, value))


def main():
    OS_PLATFORM = system()
    SAVES_FOLDER = os.path.join("D:", "HK_Saves")
    """
    if input("Use default Windows path? [Y|n]: ") == "n":
        SAVES_FOLDER = input("Path to saves folder: ")
    """
    install_folder = os.path.expanduser("~")

    if OS_PLATFORM == "Windows":
        install_folder = os.path.join(
            install_folder, "AppData", "LocalLow", "Team Cherry", "Hollow Knight")
    elif OS_PLATFORM == "Linux":
        install_folder = os.path.join(
            install_folder, ".config", "unity3d", "Team Cherry", "Hollow Knight")

    all_dirs = [d for d in os.listdir(SAVES_FOLDER) if os.path.isdir(
        os.path.join(SAVES_FOLDER, d))]
    show_saves(all_dirs)

    pattern = 'load [0-9]$'
    while True:
        cmd = input("> ")
        if match(pattern, cmd):
            dir_to_copy = os.path.join(SAVES_FOLDER, all_dirs[int(cmd[-1])])
            files = os.listdir(dir_to_copy)
            print("Loading {} save state in slot 4...".format(
                all_dirs[int(cmd[-1])]))
            for f in files:
                copy(os.path.join(dir_to_copy, f), install_folder)

if __name__ == '__main__':
    main()