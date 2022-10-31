import os
import re
from datetime import datetime
from collections import defaultdict
import shutil


# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_files_route_with_mod_date(directory):
    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    directory_files = os.listdir(directory)
    file_list = []
    for file in directory_files:
        file_route = "/".join([directory, file])
        if ((not re.search(date_regex, file)) and os.path.isdir(file_route)) or os.path.isfile(file_route):
            file_info = os.lstat(file_route)
            file_date_string = datetime.fromtimestamp(file_info.st_mtime).strftime("%Y-%m-%d")
            file_list.append({'file_name': file, 'last_mod_date': file_date_string})

    files_by_date = defaultdict(list)
    for file in file_list:
        files_by_date[file['last_mod_date']].append(file)

    return files_by_date


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    dir_name = ""
    while not os.path.isdir(dir_name):
        dir_name = input("Please enter the absolute dir path: ")
        dir_name = os.path.abspath(dir_name)
        if not os.path.isdir(dir_name):
            print(f"The path: {dir_name} is not a directory")
        else:
            print(f"{dir_name} is a dir path")
            file_list = get_files_route_with_mod_date(dir_name)
            for r in file_list:
                date_dir_name = '/'.join([dir_name, r])
                try:
                    os.mkdir(date_dir_name)
                except FileExistsError as e:
                    print("os.mkdir error:", e.args[0])
                for file in file_list[r]:
                    source_file = '/'.join([dir_name, file['file_name']])
                    if ((not re.search(date_regex, file['file_name'])) and os.path.isdir(
                            source_file)) or os.path.isfile(source_file):
                        destination_file = '/'.join([dir_name, r, file['file_name']])
                        try:
                            shutil.move(source_file, destination_file)
                        except shutil.Error as e:
                            print('shutil.move error:', e.args[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# obtener archivos de un directorio os.listdir()
# obtener fecha de los archivos os.lstat('archivo'). Devuelve objeto st_ctime expresado en segundos
# shutil.move() to move files
