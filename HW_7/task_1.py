"""
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

"""
import os
from pathlib import Path


def rename_files(desired_name, num_digits, source_extension, target_extension, name_range: list):
    """
    Функция переименовывает файлы в текущей рабочей директории.
    - desired_name: желаемое конечное имя файлов.
    - num_digit: количество цифр в порядковом номере.
    - source_extension: расширение исходного файла.
    - target_extension: расширение конечного файла.
    - name_range (необязательный): диапазон сохраняемого оригинального имени.

    """
    directory = os.getcwd()  # Текущая рабочая директория
    file_counter = 1  # Счетчик файлов

    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            original_name = filename[name_range[0]:name_range[1]] if name_range else filename
            new_name = f"{original_name}_{desired_name}{str(file_counter).zfill(num_digits)}.{target_extension}"
            Path(directory, filename).rename(new_name)
            # os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            file_counter += 1
