# напишите функцию которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 4 семинара.
# # Функция должна извлекать ключи словаря для заголовков столбца из переданного файла
import csv
import pickle


# Создание списка словарей
data = [
    {'Name': 'John', 'Age': 28, 'City': 'New York'},
    {'Name': 'Emma', 'Age': 32, 'City': 'London'},
    {'Name': 'Michael', 'Age': 45, 'City': 'Paris'}
]


def creat_pickle(data: dict):
# Запись данных в файл pickle
    pickle_file = 'data.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)


def pickle_to_csv(pickle_file, csv_file):
    # Чтение данных из файла pickle
    with open(pickle_file, 'rb') as f:
        data_csv = pickle.load(f)

    # Получение заголовков столбцов из ключей первого словаря
    headers = list(data_csv[0].keys())

    # Запись данных в CSV файл
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_csv)

    print("Преобразование завершено. Файл CSV создан.")


creat_pickle(data)

pickle_file = 'data.pickle'  # Путь к файлу pickle
csv_file = 'data.csv'  # Путь к файлу CSV

pickle_to_csv(pickle_file, csv_file)


res = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
print(res)