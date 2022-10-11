import os
from datetime import datetime


# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_files_route_with_mod_date(directory):
    directory_files = os.listdir(directory)
    files_list = []
    for file in directory_files:
        file_route = "/".join([directory, file])
        file_info = os.lstat(file_route)
        file_date_string = datetime.fromtimestamp(file_info.st_mtime).strftime("%Y/%m/%d")
        files_list.append({'file_route': file_route, 'last_mod_date': file_date_string})
        print(f'El fichero: {file}\nTiene esta fecha: {file_date_string}')
    print(files_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_files_route_with_mod_date('../test')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# obtener archivos de un directorio os.listdir()
# obtener fecha de los archivos os.lstat('archivo'). Devuelve objeto st_ctime expresado en segundos
# shutil.move() to move files
