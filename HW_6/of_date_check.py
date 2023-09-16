"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.

Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
import datetime


def data_check(day: int, month: int, year: int):
    """
    Введите дату в формате DD.MM.YYYY
    в следующем порядке
    :param day: от 1 до 31
    :param month: от 1 до 12
    :param year: от 1 до 99999
    :return: Ны выходе вы получите данные формата дата либо ошибку из-за некоректного ввода даты
    """
    try:
        flag = datetime.datetime(year, month, day)
        if flag.strftime("%d") and flag.strftime("%B") and flag.strftime("%Y"):
            print()
        return print(flag.strftime("%d"), flag.strftime("%B"), flag.strftime("%Y"))
    except BaseException:
        print("Некоректный ввод даты")
    finally:
        print("Выполнено")


def year_check() -> bool:
    year = int(input("enter year: "))
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True
