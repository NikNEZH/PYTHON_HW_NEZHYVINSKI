import csv
import random




filename = 'random_numbers.csv'
def generate_random_csv():
    # filename = 'random_numbers.csv'  # Имя файла для сохранения
    rows = random.randint(100, 1000)  # Случайное количество строк от 100 до 1000
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


my_list = []


def read_csv_file():
    """
    Принимает на вход csv файл и из него записывает данные в лист
    :param filename:
    :return:
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:  # Проверяем, что в строке есть три числа
                num1, num2, num3 = map(int, row)
                my_list.append(num1)
                my_list.append(num2)
                my_list.append(num3)
        return my_list



