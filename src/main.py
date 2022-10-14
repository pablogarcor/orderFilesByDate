import os
from datetime import datetime
from collections import defaultdict
import shutil


# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_files_route_with_mod_date(directory):
    print(directory)
    directory_files = os.listdir(directory)
    file_list = []
    for file in directory_files:
        file_route = "/".join([directory, file])
        file_info = os.lstat(file_route)
        file_date_string = datetime.fromtimestamp(file_info.st_mtime).strftime("%Y-%m-%d")
        file_list.append({'file_name': file, 'last_mod_date': file_date_string})

    files_by_date = defaultdict(list)
    for file in file_list:
        files_by_date[file['last_mod_date']].append(file)

    return files_by_date


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir_name = os.path.abspath('test')
    file_list = get_files_route_with_mod_date(dir_name)
    for r in file_list:
        date_dir_name = '/'.join([dir_name, r])
        os.mkdir(date_dir_name)
        for file in file_list[r]:
            source_file = '/'.join([dir_name, file['file_name']])
            destination_file = '/'.join([dir_name, r, file['file_name']])
            try:
                shutil.move(source_file, destination_file)
            except shutil.Error as e:
                for src, dst, msg in e.args[0]:
                    print(dst, src, msg)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# obtener archivos de un directorio os.listdir()
# obtener fecha de los archivos os.lstat('archivo'). Devuelve objeto st_ctime expresado en segundos
# shutil.move() to move files
