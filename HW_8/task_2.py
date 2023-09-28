import os
import json
import csv
import pickle
from pathlib import Path


def save_directory_info(directory):
    data = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        total_size += dir_size

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            data.append({
                'Name': file,
                'Type': 'File',
                'Parent Directory': root,
                'Size (bytes)': file_size
            })

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            data.append({
                'Name': dir,
                'Type': 'Directory',
                'Parent Directory': root,
                'Size (bytes)': get_directory_size(dir_path)
            })

    # Сохраните данные в файл JSON
    json_file = 'directory_info.json'
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

    # Сохраните данные в файл CSV
    csv_file = 'directory_info.csv'
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Type', 'Parent Directory', 'Size (bytes)'])
        writer.writeheader()
        writer.writerows(data)

    # Сохранить данные в файл pickle
    pickle_file = 'directory_info.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f)

    print("Информация о каталоге сохраняется в файлах JSON, CSV и Pickle.")


def get_directory_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        total_size += sum(os.path.getsize(os.path.join(root, file)) for file in files)

    return total_size

directory_path = Path('../Home_Python')  # Замените на путь к вашей директории
save_directory_info(directory_path)