# make-project [lang] > print(lista przedmiotow) > [?nazwa projektu]
# tworzy w katalogu projects/[przedmiot]/[lang]/[data]-[nazwa projektu] > print(sciezka)/open in explorer

##CREATING PROJECT DIRECTORY FOR PROGRAMMIN (OR OTHER) CLASS##
##USAGE:
## make-project.py [lang]
## choose subject
## enter project name

##PROJECT PATH IN THIS EXAMPLE: D:/Projects/[subject]/[lang]/[today-date]-[project-name]
##THE SCRIPT CREATES AND OPENS PROJECT DIRECTORY IN WINDOWS FILE EXPLORER

import sys
import os
from datetime import date
import subprocess


def main():
    args = sys.argv
    if len(args) != 2:
        return print("Usage: make-project.py [lang]")

    project_path = f"D:\\Projects\\"
    if not os.path.exists(project_path):
        os.mkdir(project_path)

    subjects = ['Subject_1', 'Subject_2']
    print("Chose subject:")

    for i, subject in enumerate(subjects):
        print(f" [{i + 1}] {subject}")
    print(f" [{len(subjects)+1}] Other")
    choice = input("> ")

    try:
        choice_int = int(choice)-1
        if choice_int == len(subjects):
            project_path += input("Enter subject name: ")
        else:
            project_path += subjects[choice_int]

        if not os.path.exists(project_path):
            os.mkdir(project_path)

        project_path += "\\" + args[1] + "\\"
        if not os.path.exists(project_path):
            os.mkdir(project_path)

    except NameError:
        print(f"Bad choice {NameError}")

    try:
        print("Enter project name[0 - \"new-project\"]: ")
        nazwa = input("> ")
        if nazwa == "0":
            nazwa = "new-project"
        today = date.today()
        project_path += f"{today}-{nazwa}"
        path_end = ""

        project_number = 2
        while os.path.exists(project_path + path_end):
            path_end = "_"+str(project_number)
            project_number += 1

        os.mkdir(project_path + path_end)
        print(f"Project path: {project_path}")
        subprocess.Popen(f'explorer "{project_path}')
    except NameError:
        print(f"Error {NameError}")


if __name__ == "__main__": main()
