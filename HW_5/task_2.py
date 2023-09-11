# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
import os


def split_path(file_path: str):
    """
    Разделяет путь на каталог и имя файла, затем разделяет имя файла на имя и расширение

    """
    directory, file_name = os.path.split(file_path)

    name_file, type_file = os.path.splitext(file_name)
    return directory, name_file, type_file


file_path = r'C:\Users\Никита\Desktop\ПОГРУЖЕНИЕ В ПАЙТОН\лекция_5.pptx'
path, name_file, type_file = split_path(file_path)
print("Путь:", path)
print("Имя файла:", name_file)
print("Расширение файла:", type_file)
