import json
import os


class User:
    def __init__(self, name: str, the_id: int, level: int = 1):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self.the_id = the_id
        if not isinstance(level, int) or level not in range(1, 8):
            raise ValueError('Уровень доступа должен быть целым числом от 1 до 7')
        self.level = level

    def __eq__(self, other):
        return all((self.name == other.name, self.the_id == self.the_id))

    def __str__(self):
        return f'{self.name = }, {self.the_id = }, {self.level = }'


def worker():
    while True:
        try:
            name = input('Введите имя: ')
            the_id = int(input('Введите личный идентификатор: '))
            level = int(input('Введите уровень доступа: '))
            return User(name, the_id, level)
        except ValueError as e:
            print(e)


def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def save_json(path, user_db):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_db, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    PATH = 'my_json.json'
    USER_DB = load_json(PATH)
    NEW_USER = worker()
    if str(NEW_USER.the_id) in USER_DB:
        raise Exception('Пользователь с этим ID уже записан в базу')
    else:
        USER_DB[NEW_USER.the_id] = {'name': NEW_USER.name, 'level': NEW_USER.level}
        save_json(PATH, USER_DB)