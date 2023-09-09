# Напишите функцию для транспонирования матрицы
import pprint

matrix = [[1, 2],
          [3, 4],
          [5, 6]]
print(matrix)


def transport_matrix(matrix):
    trance_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trance_matrix[j][i] = matrix[i][j]

    def print_matrix(trance_matrix):
        for row in trance_matrix:
            print(row)

    return print_matrix(trance_matrix)

transport_matrix(matrix)
