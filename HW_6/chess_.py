"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
import random

X = 8
Y = 8
matrix_chess = [[0] * Y for _ in range(X)]


def step_(n):
    my_list = []
    for j in range(n, Y, 2):
        my_list.append(j)
    return my_list


def random_of_chess(n: int = 8) -> None:
    for _ in range(n):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
    return x, y


def creat_and_print_chess():
    """
    Эта функция специально создана для создания и возрата матричной системы шахмат
    для 8 ферзей на доске и определить, есть ли среди них пара бьющих друг друга.

    Метод все еще находиться в стадии тестирования
    :return:

    """
    for i in range(X):
        if i == 0:
            n_white = step_(0)
            n_black = step_(1)
            for j in range(len(n_white)):
                matrix_chess[0][n_white[j]] = random_of_chess()
                matrix_chess[len(matrix_chess) - 1][n_black[j]] = random_of_chess()

    for i in range(len(matrix_chess)):  # len(matrix_chess) - возвращает количество строк в матрице
        for j in range(len(matrix_chess[i])):  # len(matrix_chess[i]) - возвращает количество элементов в строке i
            print(f'{matrix_chess[i][j]}', end=' ')
        print()
    result = is_beating_queens(matrix_chess)
    result_(result)

result = False


def is_beating_queens(matrix_chess):
    global result
    for i in range(len(matrix_chess)):
        for j in range(i + 1, len(matrix_chess)):
            if matrix_chess[i][0] == matrix_chess[j][0] or \
                    matrix_chess[i][1] == matrix_chess[j][1] or \
                    abs(matrix_chess[i][0] - matrix_chess[j][0]) == abs(matrix_chess[i][1] - matrix_chess[j][1]):
                return result
            else:
                result = True

    return result


def result_(result: bool):
    if result:
        print("Ферзи не бьют друг друга")
    else:
        print("Ферзи бьют друг друга")



