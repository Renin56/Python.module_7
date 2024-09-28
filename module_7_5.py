import os
import time

a = 150
total_files = 0
directory = os.getcwd()

for i, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(i, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print('=' * a)
        print(f'Обнаружен файл: "{file}"')
        print(f'        Путь до файла: {filepath}')
        print(f'        Размер: {filesize} байт')
        print(f'        Время изменения: {formatted_time}')
        print(f'        Родительская дирекория: {parent_dir}')

        total_files += 1

print('=' * a)
print(f'Обнаружено фйлов: {total_files}')
