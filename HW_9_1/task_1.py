# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
import random
import csv
import math
from typing import Callable
from HW_9 import generate_random_csv, read_csv_file


def number_of_csv(l: list):
    def deco(func):
        counter = []

        def wrapper(*args, **kwargs):
            for i in range(0, len(l), 3):
                a, b, c = l[i:i + 3]
                result = func(a, b, c)
                counter.append(result)
            return counter

        return wrapper

    return deco


def write_json(func):
    def wrapper(*args, **kwargs):
        result = func()
        with open('new_json', 'w+', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)

    return wrapper


my_list = read_csv_file()


@write_json
@number_of_csv(my_list)
def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "Нету истинных корней"


if __name__ == '__main__':
    generate_random_csv()
    read_csv_file()
    quadratic()
